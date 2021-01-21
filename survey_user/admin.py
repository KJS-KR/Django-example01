from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.SurveyModel)
class SurveyAdmin(admin.ModelAdmin):

    pass
