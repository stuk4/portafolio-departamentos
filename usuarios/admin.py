from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


from django.contrib.auth.admin import UserAdmin 



from django.contrib.auth import admin as auth_admin





@admin.register(User)
class CustomUserAdmin(UserAdmin):
   list_display = ["mostrar_imagen",
                    "username", 
                    "is_superuser"]
   fieldsets = (("User", {"fields": ("telefono","fecha_nacimiento","N_tarjeta","imagen",)}),) + auth_admin.UserAdmin.fieldsets


