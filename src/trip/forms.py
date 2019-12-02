from django import forms
from .models import Trips_daily, Cities_dir

class Trips_dailyForm(forms.ModelForm):
    from_city    = forms.Select()
    description  = forms.CharField(label = 'Описание',widget=forms.Textarea(
                                                        attrs={
                                                                'placeholder':'Опишите детали поездки',
                                                                'col':35,
                                                        }))
    settle_date  = forms.DateTimeField(label = 'Дата поездки', input_formats=['%d.%m.%Y'], widget=forms.DateTimeInput(
                                                        attrs={
                                                                'placeholder':'19.01.2020',
                                                        }))
    class Meta:
        model = Trips_daily
        fields = ('from_country',
                  'from_city',
                  'to_country',
                  'to_city',
                  'description',
                  'price',
                  'settle_date'                  
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['from_city'].queryset = Cities_dir.objects.none()
        self.fields['to_city'].queryset = Cities_dir.objects.none()

        if 'from_country' and 'to_country' in self.data:
            try:
                from_country_id, to_country_id = int(self.data.get('from_country')), int(self.data.get('to_country'))
                self.fields['from_city'].queryset = Cities_dir.objects.filter(country_id=from_country_id).order_by('city_name')
                self.fields['to_city'].queryset   = Cities_dir.objects.filter(country_id=to_country_id).order_by('city_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
#        elif self.instance.pk:
#            self.fields['from_city'].queryset = self.instance.from_country.from_city_set.order_by('name')
#            self.fields['to_city'].queryset = self.instance.to_country.to_city_set.order_by('name')
 
#Forma Validation in django
    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise forms.ValidationError("Неверная цена")
        return price