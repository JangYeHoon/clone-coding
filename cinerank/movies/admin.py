from django.contrib import admin
from movies.models import *

# Register your models here.
class LikeUserInline(admin.TabularInline):
    model = Movie.like_users.through
    verbose_name = "좋아요 한 User"
    verbose_name_plural = f"{verbose_name} 목록"
    extra = 1

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "cd",
        "name",
    ]
    inlines = [
        LikeUserInline,
    ]