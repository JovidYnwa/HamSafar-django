from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    user_phone = PhoneNumberField()
    user_img = models.ImageField(upload_to=None, blank=True, null=True)

class Countries_dir(models.Model):
    country_name = models.CharField(max_length = 50)
    country_code = models.CharField(max_length = 50)

    def __str__(self):
        return '{} {}'.format(self.country_name, self.country_code)

class Cities_dir(models.Model):
    country = models.ForeignKey(Countries_dir, on_delete=models.CASCADE)
    city_name = models.CharField(max_length = 50)
    city_code = models.CharField(max_length = 50)

    def __str__(self):
        return '{} {}'.format(self.country, self.city_name, self.city_code)

class Trips_daily(models.Model):
    from_country = models.ForeignKey(Countries_dir, related_name='from_country', on_delete=models.CASCADE)
    from_city    = models.ForeignKey(Cities_dir, related_name='from_city', on_delete=models.CASCADE)
    to_country   = models.ForeignKey(Countries_dir, related_name='to_country', on_delete=models.CASCADE)
    to_city      = models.ForeignKey(Cities_dir, related_name='to_city', on_delete=models.CASCADE)





   





