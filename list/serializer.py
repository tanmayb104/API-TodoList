from rest_framework import serializers
from .models import Todoitem

'''
querydict -- >> json 
serialize the data
json -->> queryd 
'''

class TodoitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todoitem
        fields = '__all__'