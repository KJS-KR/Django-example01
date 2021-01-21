from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render
from . import forms
from survey_user import models as survey_user_model
import simplejson as json

# Create your views here.
class LoginView(FormView):
    template_name = "home.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("users:survey")

    def form_valid(self, form):
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, user_id=user_id, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def go_home(request):

    return render(request, "home.html")


def go_survey(request):

    if request.method == "POST":
        print(request.POST.getlist("lense[]"))
        print(request.user.id)
        survey = survey_user_model.SurveyModel.objects.create(
            user_id=request.user.id,
            survey_01=request.POST["age"],
            survey_02=request.POST["gender"],
            survey_03=request.POST.getlist("lense[]"),
            survey_04=request.POST.getlist("medicine[]"),
            survey_05=request.POST.getlist("past[]"),
            survey_06=request.POST.getlist("surgical[]"),
            survey_07=request.POST.getlist("family[]"),
        )
        # print(request.user.id)

        get_info = survey_user_model.SurveyModel.objects.all()
        form = {
            "ans_01": survey.survey_01,
            "ans_02": survey.survey_02,
            "ans_03": survey.survey_03,
            "ans_04": survey.survey_04,
            "ans_05": survey.survey_05,
            "ans_06": survey.survey_06,
            "ans_07": survey.survey_07,
        }

        return render(
            request,
            "survey_success.html",
            {
                "form": form,
            },
        )
    return render(request, "survey.html")


def go_success(request):

    return render(request, "survey_success.html")