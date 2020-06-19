from .models import stock
from rest_framework import serializers
class stockserializer(serializers.ModelSerializer):
    class Meta:
        model=stock
        #fieds=('ticker','volume')
        fields = '__all__'