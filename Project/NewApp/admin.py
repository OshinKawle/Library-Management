from django.contrib import admin
from .models import Library


class LibraryAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','branch','roll_no','email','book_name']


admin.site.register(Library,LibraryAdmin)
