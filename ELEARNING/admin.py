from django.contrib import admin
from .models import Intake
from .models import Upload

# Register your models here.
admin.site.register(Intake)
admin.site.register(Upload)