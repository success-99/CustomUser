from django.shortcuts import render, redirect
from .forms import SignupForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('home')


# Create your views here.

class SignupView(View):
    def get(self, request):
        return render(request, 'registration/signup.html', {'form': SignupForm()})

    def post(self, request):
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sizning hisobingiz muvaffaqiyatli yaratildi !')
            return redirect('login')
        return render(request, 'registration/signup.html', {'form': form})
