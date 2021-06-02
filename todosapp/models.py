from django.db import models

# Create your models here.
class todo(models.Model):
    taskname=models.CharField(max_length=50)
    choices=(("completed","completed"),
                ("notcompleted","notcompleted"))
    status=models.CharField(max_length=12,choices=choices,default="notcompleted")
    user=models.CharField(max_length=50)


    def __str__(self):
        return self.user

