from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
# Imports
import torch
import torch.nn as nn  # All neural network modules, nn.Linear, nn.Conv2d, BatchNorm, Loss functions
import torch.optim as optim  # For all Optimization algorithms, SGD, Adam, etc.
import torchvision.transforms as transforms  # Transformations we can perform on our dataset
import torchvision
import os
import pandas as pd
from skimage import io
from torch.utils.data import (
    Dataset,
    DataLoader,
) 

File='C:\\Users\\TEJPAL KUMAWAT\\imageclassifier\\models\\model.pth'
model2=torch.load(File)

model2.eval()


def index(request):
    context={'a':1}
    return render(request,'index.html',context)

def predictImage(request):
    print(request)
    print(request.POST.dict())
    file_obj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(file_obj.name,file_obj)
    filePathName=fs.url(filePathName)
    img_path ='.'+filePathName
    image = io.imread(img_path)

    transform = transforms.Compose([ transforms.ToPILImage(),
            transforms.Resize((224,224)),transforms.ToTensor()])
    image=transform(image)
    image.shape
    i=image.reshape(1,3,224,224)
    
    
    pred=model2(i)

    _, predictions = pred.max(1)
    
    predictedLabel=predictions.item()

    context={'filePathName':filePathName,'predictedLabel':predictedLabel}
    return render(request,'index.html',context)


