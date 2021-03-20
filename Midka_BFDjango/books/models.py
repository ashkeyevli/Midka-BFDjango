from django.db import models
from utils.constants import JOURNAL_TYPES, JOURNAL_TYPE_BULLET

# Create your models here.

class BookJournalBase(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True , verbose_name="Book name")
    price = models.FloatField(null=True, blank=True , verbose_name="Price")
    description =  models.TextField(max_length=300, blank=True)
    created_at = models.DateField(verbose_name='Дата создания')

    class Meta:
        # verbose_name = 'Book'
        # verbose_name_plural = 'Books'
        abstract = True

class Book(BookJournalBase):
    num_pages = models.IntegerField(verbose_name="Pages")
    genre = models.CharField(max_length=30, null=True, blank=True , verbose_name="Genre")

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
class Journal(BookJournalBase):
    type = models.SmallIntegerField(choices=JOURNAL_TYPES, default=JOURNAL_TYPE_BULLET)
    publisher = models.CharField(max_length=30, null=True, blank=True , verbose_name="publisher")
    class Meta:
        verbose_name = 'Jounral'
        verbose_name_plural = 'Journals'
