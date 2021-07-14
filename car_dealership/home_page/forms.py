from django import forms
from home_page.models import car

price_ranges = (("0-100,000","0-100,000"),("100,000-500,000","100,000-500,000"),("500,000","1,000,000"))



class carForm(forms.fo):
    price = forms.ChoiceField(choices=price_ranges)
    color = forms.ChoiceField(choices=color_choice)
    class Meta:
        model = car
        fields = '__all__'
