from django.contrib import admin
from .models import Paste

@admin.register(Paste)
class PasteAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'content', 'file', 'created_at', 'expiration_time', 'is_active')
    search_fields = ('title', 'code')
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)

    def is_expired(self, obj):
        return obj.is_expired()
    is_expired.boolean = True
    is_expired.short_description = 'Expired'

# Alternatively, you can use admin.site.register(Paste, PasteAdmin)
