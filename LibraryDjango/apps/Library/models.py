from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from phonenumber_field.modelfields import PhoneNumberField


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f"{self.name} {self.surname}"


class Book(models.Model):
    author = models.ManyToManyField(Author, blank=True, verbose_name="Автор")
    name = models.CharField(max_length=255, verbose_name="Название")
    publication_year = models.PositiveSmallIntegerField(verbose_name='Год публикации', validators=[
        MaxValueValidator(datetime.datetime.now().year), MinValueValidator(1)
    ])
    page_number = models.PositiveSmallIntegerField(verbose_name='Количество страниц', validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f"{self.name} {self.publication_year} {self.page_number}"


class Reader(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    phone_number = PhoneNumberField(verbose_name="Номер телефона")

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number}"


class Issuance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name="Читатель")
    date_issue = models.DateField(verbose_name="Дата выдачи")
    date_expiration = models.DateField(verbose_name="Дата возврата", null=True)

    class Meta:
        verbose_name = 'Выданная книга'
        verbose_name_plural = 'Выданные книги'

    def __str__(self):
        return f"{self.book} {self.reader} {self.date_issue} {self.date_expiration}"
