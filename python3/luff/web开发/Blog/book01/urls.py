from django.urls import path, re_path

from book01 import views


urlpatterns = [
    re_path(r'^add_book/', views.add_book, name='add_book'),
    re_path(r'^add_author/', views.add_author, name='add_author'),
    re_path(r'^add_publish/', views.add_publish, name='add_publish'),
    re_path(r'^add_book/', views.add_book, name='add_book'),
    re_path(r'^book_info/', views.book_info, name='book_info'),
    re_path(r'^delete/(?P<book_id>\d+)/$', views.delete_book, name='delete_book'),
    re_path(r'^edit/(?P<book_id>\d+)/$', views.edit_book, name='edit_book'),
    re_path(r'^file_upload/', views.file_upload, name='file_upload'),
    re_path(r'^page_demo/', views.page_demo, name='page_demo'),
    re_path(r'^reg/', views.reg, name='reg'),
    re_path(r'^session_login', views.session_login, name='session_login'),
    re_path(r'^session_index', views.session_index, name='session_index'),
    re_path(r'^test/', views.session_test, name='session_test'),
    re_path(r'^del/', views.session_del, name='session_del'),
    re_path(r'auth_login', views.auth_login, name='auth_login'),
    re_path(r'auth_index/', views.auth_index, name='auth_index'),
    re_path(r'auth_logout/', views.auth_logout, name='auth_logout'),
    re_path(r'reg/', views.reg, name='reg'),
]
