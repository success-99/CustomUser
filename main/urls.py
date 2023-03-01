from django.urls import path
from main.views import VacancyView,VacancyDetail,SearchResultList

app_name = 'main'
urlpatterns = [
    path('', VacancyView.as_view(), name='vacancylist'),
    path('post/<int:pk>/', VacancyDetail.as_view(), name='vacancydetail'),
    path('search_result/', SearchResultList.as_view(), name='search_result'),

]
