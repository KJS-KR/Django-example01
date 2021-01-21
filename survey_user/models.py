from django.contrib.postgres.fields import ArrayField
from django.db import models


class SurveyModel(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="survey_users"
    )
    survey_01 = models.CharField(max_length=24, default=123, verbose_name="1번 문항")
    survey_02 = models.CharField(max_length=24, default=123, verbose_name="2번 문항")
    survey_03 = models.CharField(max_length=24, default=123, verbose_name="3번 문항")
    survey_04 = models.CharField(max_length=24, default=123, verbose_name="4번 문항")
    survey_05 = models.CharField(max_length=24, default=123, verbose_name="5번 문항")
    survey_06 = models.CharField(max_length=24, default=123, verbose_name="6번 문항")
    survey_07 = models.CharField(max_length=24, default=123, verbose_name="7번 문항")
