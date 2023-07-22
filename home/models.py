from django.db import models
from django.utils import timezone
# Create your models here.

class School(models.Model):
    questions_name = models.CharField(max_length=300)
    created_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.questions_name



class menus(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ovozlar_soni = models.SmallIntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name