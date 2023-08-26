from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = User.objects.make_random_password(length=10)
    request.user.set_password(new_password)
    send_mail(subject='Вы сменили пароль',
              message=f'Ваш новый пароль - {new_password}',
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[request.user.email])
    request.user.save()
    return redirect(reverse('catalog:home'))


def activate_new_user(request, pk):
    user = get_user_model()
    user_for_activate = user.objects.get(id=pk)
    user_for_activate.is_active = True
    user_for_activate.save()
    return render(request, 'users/activate_user.html')