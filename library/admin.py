from django.contrib import admin
from .models import Book, Author, BookInstance, Genre

#######################

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ('author', 'genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        ('information', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
# admin.site.register(Genre)
