from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .form import UserCreationForm,UserChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id','name')
    list_filter = ('is_active','is_staff')
    fieldsets = (
        (None,{'fields':('id','name','password')}),
        ("Permissions",{'fields':('is_active','is_staff')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id','name', 'password_first', 'password_second'),
        }),
    )
    search_fields = ('id',)
    ordering = ('id',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
