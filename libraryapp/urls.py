from django.conf.urls import url
from django.conf.urls import url, include
from django.urls import path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    url(r'^$', book_list, name='home'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^books$', book_list, name='books'),
    url(r'^librarians$', librarian_list, name='librarians'),
    url(r'^libraries$', library_list, name="libraries"),
    path('^book/form', book_form, name='book_form')
]