from django.contrib import admin
from .models import Code, Entrant

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    def get_entrant_email(self, obj):
        return obj.entrant.email if obj.entrant else "Kullanılmadı"
    get_entrant_email.short_description = 'Kullanan Kişi (E-posta)'
    list_display = ('code_value', 'get_entrant_email')
    search_fields = ('code_value', 'entrant__email')

@admin.register(Entrant)
class EntrantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')