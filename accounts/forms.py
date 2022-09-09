from django.forms import ModelForm
from .models import Customer, Order

#import UserCreationForm for customizing
from django.contrib.auth.forms import UserCreationForm

#importing default django user model in admin panel
from django.contrib.auth.models import User

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']