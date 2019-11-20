from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import (Profile,
                     Countries_dir,
                      Cities_dir,
                      Trips_daily)



# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'user_addtional_info'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Countries_dir)
class Locations_dicAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'country_code')

@admin.register(Cities_dir)
class Locations_dicAdmin(admin.ModelAdmin):
    list_display = ('country', 'city_name', 'city_code')


admin.site.register(Trips_daily)
