from django import forms
from .models import Trips_daily, Cities_dir

class Trips_dailyForm(forms.ModelForm):
    class Meta:
        model = Trips_daily
        fields = ('country', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = Cities_dir.objects.none()
 #       self.fields['to_city'].queryset = Cities_dir.objects.none()