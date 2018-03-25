from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, DetailView
from django.views.generic.base import View

from .forms import AddKrukForm
from .models import Kruk


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class MainView(View):
    def get(self, request):
        kruki = Kruk.objects.all()
        ctx = {
            'kruki': kruki
        }
        return render(request,template_name='kruk/main.html', context=ctx)


class MainInaczej(ListView):
    """Widok listy z użyciem ListView"""
    model = Kruk
    ordering = ['-creation_date']
    paginate_by = 15
    context_object_name = 'lista_krukow'

class KrukView(DetailView):
    """Widok szczegółowy tweeta"""
    model = Kruk


class AddKrukView(LoginRequiredMixin, FormView):
    form_class = AddKrukForm
    template_name = "kruk/add_kruk.html"
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        content = form.cleaned_data['content']
        Kruk.objects.create(
            content=content,
            krukacz=self.request.user
        )
        return super(AddKrukView, self).form_valid(form)

