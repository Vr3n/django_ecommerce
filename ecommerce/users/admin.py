from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)

    group.short_description = 'Groups'


    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', )
    list_filter = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', )

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'password', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2','is_staff', 'is_active')
        }),
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name', )


admin.site.register(CustomUser, CustomUserAdmin)