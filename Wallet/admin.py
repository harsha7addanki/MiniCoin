from django.contrib import admin
from .models import User, Gift, Notification


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Gift)
admin.site.register(Notification)

admin.site.site_header = 'Developer Interface'
admin.site.index_title = 'Developer Interface'
