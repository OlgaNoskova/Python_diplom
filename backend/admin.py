from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'id', 'first_name', 'last_name', 'is_staff', 'is_superuser')  # Поля отображения в админке
    list_filter = ('is_staff', 'is_superuser')                # Поля фильтрации в админке
    search_fields = ('email', 'last_name', 'phone', 'city')   # Поля поиска в админке в верхней части панели
    list_editable = ('is_staff', 'is_superuser')              # Поля редактирования в админке
