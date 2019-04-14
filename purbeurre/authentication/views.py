from django.views.generic import TemplateView, FormView
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import RegisterForm

# Create your views here.


class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'authentication/account.html'

    def get(self, request, *args, **kwargs):
        fullname = " ".join([request.user.first_name, request.user.last_name])
        context = {'fullname': fullname}
        return render(request, self.template_name, context)


class RegisterView(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('authentication:account')
    template_name = 'authentication/register.html'

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=raw_password)
        if user:
            login(self.request, user)
        return super().form_valid(form)


@login_required
def LogoutView(request):
    logout(request)
    return redirect('products:index')