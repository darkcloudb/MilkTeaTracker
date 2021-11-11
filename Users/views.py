from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from Users.forms import SignUpForm, LoginForm
from Users.models import MyUser
from django.contrib import messages
from django.views.generic import View

# The SignUp and Login Views


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('password1') == data.get('password2'):
                try:
                    check = MyUser.objects.get(username=data.get('username'))
                    context = {'form': form}
                    messages.error(request, 'Username is already taken. Please try another.')
                    return render(request, 'username_taken.html', {'form': form})
                except MyUser.DoesNotExist:
                    user = MyUser.objects.create_user(
                        username=data.get('username'),
                        password=data.get('password')
                    )
                    login(request, user)
                    return redirect(reverse('homepage'))
            else:
                context = {'form': form}
                messages.error(request, 'Passwords do not match. Please try again.')
                return render(request, 'password_match.html', {'form': form})
        else:
            form = SignUpForm()
            return render(request, 'signup.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data.get('username'),
                password=data.get('password')
            )
            if user:
                login(request, user)
                return redirect(request.GET.get('next', 'homepage'))
            else:
                return render(request, 'incorrect.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('homepage'))
