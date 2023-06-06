from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance


#Определение к классу администратор
#class AuthorAdmin(admin.ModelAdmin):
#    list_display = ('last_name', 'first_name')
#    fields = ['first_name', 'last name',
#              ('date_of_birth', 'date_of_death')]
#Зарегистрируйте класс admin с соответствующей моделью
#admin.site.register(Author, AuthorAdmin)



class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


#Регистрируем классы администратора для книг
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline]


#Регистрирвуем классы администратора для экземпляра книги

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'inv_nom')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

admin.site.register(Author)
#admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
#admin.site.register(BookInstance)


# Register your models here.
