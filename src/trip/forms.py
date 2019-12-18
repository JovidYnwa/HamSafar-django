from django import forms
from .models import  (Comment,
                      Cities_dir,
                      Profile,
                      User,
                      Trips_daily,)
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date, datetime

class SignupForm(forms.ModelForm):
    user_phone = forms.CharField(label = 'Телефон', widget = forms.TextInput(
                                                    attrs ={
                                                            'placeholder': 'Формат: +992 918181818',
                                                            }))
    class Meta:
        model = Profile
        fields = ('user_phone',)

    def signup(self, request, user):
        user.profile.user_phone = self.cleaned_data['user_phone']
        user.save()


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
    

        #def __init__(self, *args, **kwargs):
            #super().__init__(*args, **kwargs)
            #self.fields['from_city'].queryset = Cities_dir.objects.none()
            #self.fields['to_city'].queryset   = Cities_dir.objects.none()
  
    def clean(self):
        super(Trips_dailyForm, self).clean
        from_city = self.cleaned_data.get("from_city")
        to_city   = self.cleaned_data.get("to_city")
        print(from_city, to_city)
        if from_city == to_city:
            raise forms.ValidationError("Города не должны совподать!")
        return from_city

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)
        