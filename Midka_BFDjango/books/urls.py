from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from books.views import BooksViewSet, JournalViewSet
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register('books', BooksViewSet, basename='books')
router.register('journal', JournalViewSet, basename='books')
urlpatterns = [
]
urlpatterns += router.urls