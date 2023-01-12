from django.db import models

# Create your models here.


# class Level(models.Model):
#     level = models.CharField(max_length=200)
#     def __str__(self):
#         return self.level



class paper(models.Model):
    # level=models.ForeignKey(Level,on_delete=models.CASCADE ,null=True,blank=True,default="Easy")
    questions = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    right_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.questions
