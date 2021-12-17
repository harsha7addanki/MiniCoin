from django.contrib import admin
from .models import User,Gift

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Gift)

admin.site.site_header = 'Developer Interface'
admin.site.index_title= 'Developer Interface' 