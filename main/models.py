from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    technologies = models.TextField(help_text="List technologies separated by commas.")
    image = models.URLField(blank=True, default="")
    github_url = models.URLField(blank=True, default="")
    live_url = models.URLField(blank=True, default="")
    featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        return [item.strip() for item in self.technologies.split(",") if item.strip()]


class Skill(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["category", "name"]

    def __str__(self):
        return f"{self.name} ({self.category})"


class Experience(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True, default="")
    description = models.TextField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)

    class Meta:
        ordering = ["-start_date", "-end_date"]

    def __str__(self):
        return self.position


class Education(models.Model):
    institution = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ["-start_date", "-end_date"]

    def __str__(self):
        return f"{self.qualification} - {self.institution}"


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}: {self.subject}"
