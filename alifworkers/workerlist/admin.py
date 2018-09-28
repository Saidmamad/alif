from django.contrib import admin
from .views import Workers, Address, Education, Position

# Register your models here.

admin.site.register(Workers)
admin.site.register(Address)
admin.site.register(Education)
admin.site.register(Position)
