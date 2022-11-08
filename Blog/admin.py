from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(myuser)
admin.site.register(BlogAuthor)
admin.site.register(Categories)
# admin.site.register(BlogComments)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post, PostAdmin)
