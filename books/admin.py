from django.contrib import admin
from .models import Book, Review


# @admin.register(Review)
class ReviewInline(admin.TabularInline):
    model = Review

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [ReviewInline,]
    list_display = ['title', 'author', 'price']
    
