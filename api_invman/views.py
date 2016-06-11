from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import api
from .forms import apiForm


class apiListView(ListView):
    model = api


class apiCreateView(CreateView):
    model = api
    form_class = apiForm


class apiDetailView(DetailView):
    model = api


class apiUpdateView(UpdateView):
    model = api
    form_class = apiForm

