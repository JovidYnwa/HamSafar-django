from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse


class Profile(models.Model):
    user       = models.OneToOneField(User, on_delete = models.CASCADE)
    user_phone = PhoneNumberField()
    user_img   = models.ImageField(upload_to=None, blank=True, null=True)

class Countries_dir(models.Model):
    country_name = models.CharField(max_length = 50)
    country_code = models.CharField(max_length = 50)

    def __str__(self):
        return '{}'.format(self.country_name)

class Cities_dir(models.Model):
    country   = models.ForeignKey(Countries_dir, on_delete=models.CASCADE)
    city_name = models.CharField(max_length = 50)
    city_code = models.CharField(max_length = 50)

    def __str__(self):
        return '{}'.format(self.city_name)


#User = settings.AUTH_USER_MODEL

class Trips_daily(models.Model):
    owner        = models.ForeignKey(User, on_delete=models.CASCADE)
    from_country = models.ForeignKey(Countries_dir, verbose_name="Страна выезда", related_name='from_country', on_delete=models.CASCADE)
    from_city    = models.ForeignKey(Cities_dir, verbose_name="Город выезда", related_name='from_city', on_delete=models.CASCADE)
    to_country   = models.ForeignKey(Countries_dir, verbose_name="Страна назначения", related_name='to_country', on_delete=models.CASCADE)
    to_city      = models.ForeignKey(Cities_dir, verbose_name="Город назначения", related_name='to_city', on_delete=models.CASCADE)
    description  = models.CharField(max_length = 250, verbose_name="Опсание")
    date_posted  = models.DateTimeField(auto_now=True, auto_now_add=False)
    price        = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена", blank =True)
    settle_date  = models.DateTimeField(auto_now=False, verbose_name="Дата поездки")

    def __srt__(self):
        return '{} - {}'.format(self.from_city, self.to_city)

    def get_absolute_url(self):
        return reverse('detail_of_trip', kwargs= {'id': self.id})

    def get_update_url(self):
        return reverse('edit_of_trip', kwargs= {'id':self.id})







   





