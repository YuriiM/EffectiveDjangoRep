from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView
from contacts.models import Contact


class ListContactView(ListView):
    model = Contact


class CreateContactView(CreateView):
    model = Contact

    def get_success_url(self):
        return reverse('contacts-list')
