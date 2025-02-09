from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import LoginForm, RegisterForm


class LoginView(LoginRequiredMixin, View):
    def get(self, request):
        form = LoginForm()
        context = {
            "form": form
        }
        return render(request, "users/login.html", context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        data = {
            "username": username,
            "password": password
        }
        login_form = AuthenticationForm(data=data)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("landing")
        else:
            context = {
                "form": login_form,
            }
            return render(request, "users/login.html", context)


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect("landing")


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, "users/register.html", context)

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "password": password
        }
        create_form = RegisterForm(data=data)
        if create_form.is_valid():
            create_form.save()
            return redirect("login")
        else:
            context = {
                "form": create_form
            }
            return render(request, "users/register.html", context)


class DetailView(View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, "users/users_detail.html", context={"user": user})


class SettingsView(View):
    def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, 'users/settings.html', context={"user": user})

    def post(self, request, id):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        password = request.POST["password"]
        user = User.objects.get(id=id)
        user.first_name = first_name
        user.last_name_name = last_name
        user.set_password(password)
        user.save()
        return HttpResponse("<h1>Successful</h1>")


# class DeleteView(View):
#     def get(self, request, id):
#         user = User.objects.get(id=id)
#         user.delete()
#         return redirect("users/register.html")
