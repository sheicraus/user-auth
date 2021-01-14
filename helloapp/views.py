from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .forms import SignUpForm
# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


def SignUpView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {'form': form})
