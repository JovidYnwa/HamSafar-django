from django import forms
from .models import Trips_daily, Cities_dir

class Trips_dailyForm(forms.ModelForm):
    class Meta:
        model = Trips_daily
        fields = ('from_country', 'from_city', 'to_country', 'to_city')

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
        elif self.instance.pk:
            self.fields['from_city'].queryset = self.instance.from_country.fromcity_set.order_by('name')
            self.fields['to_city'].queryset = self.instance.to_country.fromcity_set.order_by('name')