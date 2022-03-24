
from django import forms
from django.forms import widgets
from django.forms.fields import CharField
from .models import Food
'''
class FoodForm(forms.Form):
    food_Id = forms.CharField(label='Food Id',label_suffix=" :- ",
        widget=forms.NumberInput(attrs={'placeholder':'Enter Food Id',
                                        }))
    food_Name = forms.CharField(label='Food Name',label_suffix=" :- ",
        widget=forms.TextInput(attrs={'placeholder':'Enter Food Name',
                                        }))
    food_Price = forms.CharField(label='Food Price',label_suffix=" :- ",
        widget=forms.NumberInput(attrs={'placeholder':'Enter Food Price',
                                        })
'''
class FoodForm(forms.ModelForm):
    food_Name=CharField(min_length=3,error_messages={
        'required':'Please Enter Food Name',
        'min_length':'Length of Food must greater 3'
    }) 
    food_Price=CharField(error_messages={
        'required':'Please Enter Food Price'
    }) 
    choices = (
            ('V','Veg'),
            ('NV','Non-Veg'),
        )
    food_Type=CharField(widget=forms.RadioSelect(choices=choices, attrs={'class': ''}),
    error_messages={
        'required':'Please Enter Food Type'
    })
    food_Description=CharField(required=False,
            widget=forms.Textarea(attrs={'rows':3}))


    class Meta:
        model=Food
        #fields=('food_Id','food_Name','food_Type')
        fields='__all__'
      