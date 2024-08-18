from django.contrib import admin
from django.urls import path, include
from films import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.film_list, name='home'),  # Перенаправление главной страницы на список фильмов
    path('films/', include('films.urls')),
]
