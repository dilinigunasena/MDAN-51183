from django import forms
from django.core.exceptions import ValidationError
from .models import inventory

class inventoryForm(forms.ModelForm):
    class Meta:
        model = inventory
        fields = '__all__'        

        labels = {
            'model_number':'Model Number',
            'model_name':'Model Name',
            'make':'Make',
            'yom':'Year of Manufacture',
            'unit_price':'Price of a Bike',
            'quantity_avl': 'Initial Available Quantity of Model',
            'quantity_sold': 'Sold Quantity of Model'            
        }

        widgets  ={
            'model_number':forms.TextInput(attrs={'placeholder': '123ABCxxx'}),
            'model_name':forms.TextInput(attrs={'placeholder': 'ABCD'}),
            'make':forms.TextInput(attrs={'placeholder': 'YAMAHA'}),            
            'yom':forms.DateInput(format='%d/%m/%Y',attrs={'placeholder': '2020-01-01'}),
            'unit_price':forms.NumberInput(attrs={'placeholder': 'price'}),
            'quantity_avl':forms.NumberInput(attrs={'placeholder': 'quantity'}),
            'quantity_sold': forms.NumberInput(attrs={'placeholder': 'quantity'})                       
        } 

class serchForm(forms.ModelForm):
    class Meta:
        model = inventory
        fields = ['model_name','make']
        labels = {           
            'model_name':'Model Name',
            'make':'Make'                  
        }
        widgets = {
            'model_name':forms.TextInput(attrs={'placeholder': 'ABCD'}),
            'make':forms.TextInput(attrs={'placeholder': 'YAMAHA'}),    
        }

    def clean(self):
        cleaned_data = super().clean()
        model_name = cleaned_data.get('model_name')
        make = cleaned_data.get('make')

        # Check if both fields are empty
        if not model_name and not make:
            raise ValidationError("At least one of 'Model Name' or 'Make' must be provided.")

        # If this point is reached, validation is successful
        return cleaned_data


        