from django.urls import path, re_path, register_converter
from blogs import views

from blogs.converter import MonthConver

register_converter(MonthConver, "mc")
urlpatterns = [
    path("login/", views.login, name="login"),
    re_path(r"article/(?P<year>[0-9]{4})/", views.get_year, name="get_year"),
    path("article/month/<mc:month>/", views.get_month, name="get_month"),
    path('person/', views.get_name_age, name='get_name_age'),
    path('detail/', views.show_detail, name='show_detail'),
    path('add_book_info', views.add_book_info, name='add_book_info'),
    path('get_books_info', views.search_book, name='search_book'),
    path('delete_book', views.delete_book_info, name='delete_book_info'),
    # path("article/month/<slug:month>/", views.get_month, name="get_month"),
]
