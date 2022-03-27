from django.db import models



from django.utils.translation import gettext as _
class pulzion(models.Model):
    Question=models.CharField(max_length=100)
    Option1=models.CharField( max_length=100)
    Option2=models.CharField(max_length=100)
    Option3=models.CharField( max_length=100)
    Option4=models.CharField( max_length=100)
    Optionans=models.CharField(max_length=100)

def __str__(self):
    return self.Optionans