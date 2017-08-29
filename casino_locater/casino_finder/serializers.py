from rest_framework import serializers
from casino_finder.models import Casino
from casino_finder.user_models import User
from casino_finder.exceptions import CustomValidation

class CasinoSerializer(serializers.ModelSerializer):

  def validate(self, data):
    """
    Check that the start is before the stop.
    """
    price = data['price']
    if price <= 0:
      raise CustomValidation('Value must be positive integer','price', status_code=422)	
      
    return data

  class Meta:
    model = Casino
    fields = ('id','name','address','price','created_by','modified_by')


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id','name','address')    
