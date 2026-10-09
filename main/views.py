from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactMessageForm
from .models import Education, Experience, Project, Service, Skill


def home(request):
    projects = Project.objects.filter(is_published=True).order_by("-featured", "-created_at")
    skills = Skill.objects.order_by("category", "name")
    experiences = Experience.objects.order_by("-start_date", "-end_date")
    educations = Education.objects.order_by("-start_date", "-end_date")
    services = Service.objects.order_by("title")

    form = ContactMessageForm()

    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            recipient_email = getattr(settings, "EMAIL_TO", "tuyizereolivier650@gmail.com")
            from_email = getattr(settings, "DEFAULT_FROM_EMAIL", recipient_email)
            email_body = (
                f"Name: {contact_message.name}\n"
                f"Email: {contact_message.email}\n"
                f"Subject: {contact_message.subject}\n\n"
                f"Message:\n{contact_message.message}"
            )

            email = EmailMessage(
                subject=f"Portfolio Contact: {contact_message.subject}",
                body=email_body,
                from_email=from_email,
                to=[recipient_email],
            )
            email.send(fail_silently=True)

            messages.success(request, "Your message was sent successfully. I will get back to you soon.")
            return redirect(f"{reverse('home')}#contact")
        messages.error(request, "Please correct the highlighted errors and try again.")

    context = {
        "projects": projects,
        "skills": skills,
        "experiences": experiences,
        "educations": educations,
        "services": services,
        "contact_form": form,
    }
    return render(request, "main/index.html", context)
