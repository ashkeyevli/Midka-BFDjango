from rest_framework import serializers
from books.models import BookJournalBase, Journal, Book


class BookJournalBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookJournalBase
        fields = '__all__'


class JounralSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
        fields = '__all__'




class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

