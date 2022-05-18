
import pydicom as dicom
import numpy as np
from matplotlib import pyplot as plt
import os
path='./img\PAT034'
from PIL import Image
images=os.listdir(path)
#print(images)

def converter(img):
    im=dicom.dcmread('./img\PAT034/'+img)
    im=im.pixel_array.astype(float)
    rescale=(np.maximum(im,0)/im.max())*255
    final_img=np.uint8(rescale)
    final_img=Image.fromarray(final_img)
    return final_img


arr_filename=[x for x in images if x.endswith('.dcm')]

for name in arr_filename:
    image=converter(name)
    image.save('./JPG_IMG/'+name+'.jpg')

