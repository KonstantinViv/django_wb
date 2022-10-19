from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance

# Register your models here.
#admin.site.register(Author)
# Определения к классу администратор
# Зарегистрируйте класс admin с соответствующей моделью

#admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
#admin.site.register(BookInstance)
# Регистрируем классы администратора для книг

# Регистрируем классы администратора для экземпляра книги


# Listing 8.9
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')

#Listing 8.12
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language')
    list_filter = ('genre', 'author')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')

# Listing 8.13
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name',
             ('date_of_birth', 'date_of_death')]