from django.urls import path
from . import views

urlpatterns = [
    path('', views.contest_view, name='contest_page'),
    path('kazanan-sec/', views.pick_winner_view, name='pick_winner'),
]

## İStek karşılar '' isteği contest_urls e gönderir.
### Boş adresi gördüğü için contest_view e yönlendirir.