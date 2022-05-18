import csv
import pydicom as dicom

from os import write

x=dicom.dcmread('./IMG\PAT034/D0001.dcm')

with open('my.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow('Group Element Description VR Value'.split())
    for elm in x:
        writer.writerow([f"{elm.tag.group:04x}",f"{elm.tag.element:04x}",elm.description(),elm.VR,str(elm.value)])



