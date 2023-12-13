from django.shortcuts import render
from django.contrib.auth import get_user, authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Drawing
from .forms import RegistrationForm


class RegistrationView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('index')
    template_name = 'registration/registration.html'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)


def index(request):
    drawings = Drawing.objects.order_by('-published')
    user = get_user(request)
    return render(request, 'online_store/index.html', {'drawings': drawings, 'user': user})
