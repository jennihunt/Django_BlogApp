from django.contrib import admin
from .models import Post,Category,Comment

# Register your models here.
@admin.register(Post,Category,Comment)
class PermissionAdmin(admin.ModelAdmin):
    pass

