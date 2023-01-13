from django.contrib import admin

# Register your models here.

# changes made on 8-01-23 making model instead of database
from .models import userData

admin.site.register(userData)
