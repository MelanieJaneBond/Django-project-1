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
    path('book/form', book_form, name='book_form'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('librarians', librarian_list, name='librarians'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarian'),
    path('libraries', library_list, name="libraries"),
    path('library/form', library_form, name="library_form")
]