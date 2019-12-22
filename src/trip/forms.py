from django import forms
from .models import  (Comment,
                      Cities_dir,
                      Countries_dir,
                      Profile,
                      User,
                      Trips_daily,)
from phonenumber_field.modelfields import PhoneNumberField
#from .widgets import EventSplitDateTime
from datetime import date, datetime
from .widgets import XDSoftDateTimePickerInput

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
                                                                'rows':5,
                                                        }))
    settle_date = forms.DateTimeField(label = 'Выберете дату',input_formats=['%d/%m/%Y %H:%M'], widget=XDSoftDateTimePickerInput())
    class Meta:
        model = Trips_daily
        exclude = ['owner']

    def clean(slef):
        cleaned_data = super().clean()
        from_city = cleaned_data.get('from_city')
        to_city = cleaned_data.get('to_city')

        if from_city == to_city:
            raise forms.ValidationError('Города не должны совподать')        



#Commet model
class CommentForm(forms.ModelForm):
    comment_text  = forms.CharField(label = 'Отзыв',widget=forms.Textarea(
                                                    attrs={
                                                            'placeholder':'Оставить отзыв',
                                                            'rows':4,
                                                    }))
    class Meta:
        model = Comment
        fields = ('comment_text',)


#Form for datepicker
