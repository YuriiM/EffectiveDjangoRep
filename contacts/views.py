from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .models import Contact
from .forms import ContactForm, ContactAddressFormSet


class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class ListContactView(ListView):
    model = Contact

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)


class CreateContactView(CreateView):
    model = Contact
    form_class = ContactForm

    def get_success_url(self):
        return reverse('contacts:contacts-list')

    def get_context_data(self, **kwargs):
        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts:contacts-new')
        return context


class UpdateContactView(UpdateView):
    model = Contact
    form_class = ContactForm

    def get_success_url(self):
        return reverse('contacts:contacts-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts:contacts-edit',
                                    kwargs={'pk': self.get_object().id})
        return context


class DeleteContactView(DeleteView):
    model = Contact

    def get_success_url(self):
        return reverse('contacts:contacts-list')


class ContactView(DetailView):
    model = Contact

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(
            pk=pk,
            owner=self.request.user,
        )
        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise Http404((u"No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj


class EditContactAddressView(UpdateView):
    model = Contact
    template_name = 'contacts/edit_addresses.html'
    form_class = ContactAddressFormSet

    def get_success_url(self):
        # redirect to the Contact view.
        return self.get_object().get_absolute_url()
