from django.urls import include, path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('librarians/', list_librarians, name='librarians'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('books/form', book_form, name='book_form'),
    path('libraries', list_libraries, name='libraries'),
    path('libraries/form', library_form, name='library_form'),
    path('books/<int:book_id>/', book_details, name='book'),
]