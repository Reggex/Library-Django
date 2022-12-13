from django.contrib import admin
from .models import Book, Author, Reader, Issuance

admin.site.register(Book)
admin.site.register(Author)
# admin.site.register(Bibliography)
admin.site.register(Reader)
admin.site.register(Issuance)
