from django.contrib import admin
from .models import TablesFire, FirePosition, Shells, Powders  # Імпорт моделі TablesFire
from .forms import TablesFireAdminForm, FirePositionAdminForm

class TablesFireAdmin(admin.ModelAdmin):
    
    #form = TablesFireAdminForm  # Підключаємо кастомну форму
    list_display = ('shell', 'arc_shell', 'powder', 'additional_powder', 'min_distance', 'max_distance')
    search_fields = ('shell', 'powder', 'additional_powder')  # Додано для пошуку за полями
    list_filter = ('shell',)  # Додаємо фільтр по полю `shell`
    #list_display_links = ('shell',)
# Реєструємо модель TablesFire з кастомним класом TablesFireAdmin

class FirePositionAdminForm(admin.ModelAdmin):
    
    #form = TablesFireAdminForm  # Підключаємо кастомну форму
    list_display = ('name', 'division', 'battery', 'status')
    search_fields = ('name', 'division', 'battery', 'status') # Додано для пошуку за полями
    list_filter = ('division', 'battery')  # Додаємо фільтр по полю `shell`
    #list_display_links = ('shell',)

admin.site.register(TablesFire, TablesFireAdmin)
admin.site.register(FirePosition, FirePositionAdminForm)
admin.site.register(Shells)
admin.site.register(Powders)
