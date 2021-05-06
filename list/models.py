from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

'''
{
    'id':'',
    'user':'',
    'heading':''
}
'''

class Todoitem(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.heading}-{self.user}"