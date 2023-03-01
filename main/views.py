from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Vacancy
from django.db.models import Q

# Create your views here.

class VacancyView(ListView):
    model = Vacancy
    template_name = "vacancy/vacancylist.html"


class VacancyDetail(DetailView):
    model = Vacancy
    template_name = "vacancy/vacancydetail.html"
    context_object_name = "vac"


class SearchResultList(ListView):
    model = Vacancy
    template_name = 'vacancy/search_result.html'
    context_object_name = 'barcha_yangiliklar'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Vacancy.objects.filter(
            Q(country__icontains=query) | Q(university__icontains=query)
        )