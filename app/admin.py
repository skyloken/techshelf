from django.contrib import admin
from .models import *

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Mark)
