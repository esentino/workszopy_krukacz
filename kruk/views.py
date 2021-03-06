from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse, resolve
from django.views.generic import CreateView, FormView, ListView, DetailView
from django.views.generic.base import View

from .forms import AddKrukForm, AddKrukCommentForm
from .models import Kruk, KrukComment, Observer


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

class AddKrukCommentView(LoginRequiredMixin, FormView):
    form_class = AddKrukCommentForm
    template_name = "kruk/add_kruk.html"
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        content = form.cleaned_data['content']
        kruk_pk = self.kwargs.get('pk', None)
        if kruk_pk is not None:
            kruk = get_object_or_404(Kruk, pk=kruk_pk)
            KrukComment.objects.create(
                content=content,
                krukacz=self.request.user,
                kruk=kruk
            )
            self.success_url = reverse('detail', args=[kruk_pk])
            return super(AddKrukCommentView, self).form_valid(form)
        return super(AddKrukCommentView, self).form_invalid(form)

class KrukaczView(LoginRequiredMixin, DetailView):
    model=User
    context_object_name = 'user_object'

class AddObserveView(LoginRequiredMixin, View):
    def get(self, request, pk):
        if request.user.pk != pk:
            user_to_observe = get_object_or_404(User, pk=pk)
            observer, created = Observer.objects.get_or_create(krukacz=request.user)
            observer.observed_krukacz.add(user_to_observe)
            observer.save()
            return redirect(reverse('krukacz', args=[pk]))
        else:
            messages.error(request, 'Nie możesz obserwować samego siebie')
            return redirect(reverse('krukacz', args=[pk]))
