from django.contrib import admin

from .models import ContactMessage, Education, Experience, Project, Service, Skill


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "is_published", "created_at")
    list_filter = ("featured", "is_published")
    search_fields = ("title", "description", "technologies")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency")
    list_filter = ("category",)
    search_fields = ("name", "category")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("position", "company", "current", "start_date", "end_date")
    list_filter = ("current",)
    search_fields = ("position", "company", "description")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("qualification", "institution", "start_date", "end_date")
    search_fields = ("qualification", "institution", "description")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "description")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created_at",)

    actions = ["mark_as_read"]

    @admin.action(description="Mark selected messages as read")
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
