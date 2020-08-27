from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User



from django.contrib import admin
from django.contrib.auth import admin as auth_admin
# Agrego en admin a el Modelo Usuario

# admin.site.register(User,UserAdmin)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    fieldsets = (("User", {"fields": ("rut","telefono","fecha_nacimiento","N_tarjeta","imagen",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", 
                    "is_superuser"]
