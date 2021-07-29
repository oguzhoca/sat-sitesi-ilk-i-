from django.shortcuts import render
from django.views.generic import TemplateView
from . forms import ContactForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User


class IndexView(TemplateView):
    template_name = 'index.html'

class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'mesajınızı aldık'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class OdemeView(SuccessMessageMixin, FormView):
    template_name = 'ödeme.html'
    form_class = ContactForm
    success_url = reverse_lazy('ödeme')
    success_message = 'SİPARİŞİNİZİ ALDIK'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AboutView(TemplateView):
    template_name = 'about.html'