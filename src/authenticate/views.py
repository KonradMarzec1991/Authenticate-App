from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, PasswordChangeform
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(View):
    template_name = 'authenticate/home.html'

    def get(self, request):
        return render(request, self.template_name, {})


class LoginUser(View):
    template_name = 'authenticate/login.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Error in logging in - Please try again!')
            return redirect('login')


class LogoutUser(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('home')


class RegisterUser(View):
    template_name = 'authenticate/register.html'

    def get(self, request):

        form = SignUpForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been registered')
            return redirect('home')
        else:
            form = SignUpForm()
            messages.success(request, 'Input data is wrong - please verify your account again!')

            context = {
                'form': form
            }
            return render(request, self.template_name, context)


class EditProfile(LoginRequiredMixin, View):
    template_name = 'authenticate/edit_profile.html'

    def get(self, request):
        form = EditProfileForm(instance=request.user)

        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have edited your profile')
            return redirect('home')
        else:
            form = EditProfileForm(instance=request.user)
            messages.error(request, 'There is something wrong - please edit again!')

            context = {
                'form': form
            }
            return render(request, self.template_name, context)


class ChangePassword(LoginRequiredMixin, View):
    template_name = 'authenticate/change_password.html'

    def get(self, request):
        form = PasswordChangeform(user=request.user)

        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = PasswordChangeform(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'You have changed your password')
            return redirect('home')
        else:
            form = PasswordChangeform(user=request.user)
            messages.error(request, 'There is something wrong - please edit again!')

            context = {
                'form': form
            }
            return render(request, self.template_name, context)


class DeleteAccount(LoginRequiredMixin, View):
    template_name = 'authenticate/delete_account.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, 'You have been deleted your account')
        return redirect('home')
