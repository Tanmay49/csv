import csv
import os
from pulzioon.models import pulzion
def run():
    file=open("D:\PICT\SE1\SEM2\pulzioon\Book.csv")
    read_file=csv.reader(file)


    pulzion.objects.all().delete()

    count=1

    for record in read_file:
        if count==1:
            pass
        else:
            print(record)
            pulzion.objects.create(Question=record[0],Option1=record[1],Option2=record[2]
            ,Option3=record[3],Option4=record[4],Optionans=record[5])
        count+=1