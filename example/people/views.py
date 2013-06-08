from django.views.generic import DetailView, ListView

from . import models


class PeopleListView(ListView):
    model = models.Person


class PersonView(DetailView):
    model = models.Person
