import pydicom as dicom
from matplotlib import pyplot as plt

path='C:/Users/TEJPAL KUMAWAT/OneDrive/Desktop/QURE.AI/Dicom_python/IMG/D0001.dcm'

x=dicom.dcmread(path)

# print(x) finf the data
#print(dir(x)) ( for printing the attributes)

# Lets plot image in the dicom file

plt.imshow(x.pixel_array,cmap=plt.cm.gray)

plt.show()