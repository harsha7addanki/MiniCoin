from django.contrib import admin
from .models import User,Gift

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)

class GiftAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gift, GiftAdmin)
admin.site.site_header = 'Developer Interface'