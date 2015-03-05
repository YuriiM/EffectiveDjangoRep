from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView
from django.views.generic import UpdateView, DeleteView, DetailView
from .models import Contact
from .forms import ContactForm


class ListContactView(ListView):
    model = Contact


class CreateContactView(CreateView):
    model = Contact
    form_class = ContactForm

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):
        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')
        return context


class UpdateContactView(UpdateView):
    model = Contact
    form_class = ContactForm

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit',
                                    kwargs={'pk': self.get_object().id})
        return context


class DeleteContactView(DeleteView):
    model = Contact

    def get_success_url(self):
        return reverse('contacts-list')


class ContactView(DetailView):
    model = Contact
