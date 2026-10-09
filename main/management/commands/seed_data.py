from django.core.management.base import BaseCommand

from main.models import Education, Experience, Project, Service, Skill


class Command(BaseCommand):
    help = "Seed the portfolio with sample content for local development."

    def handle(self, *args, **options):
        if Project.objects.count() == 0:
            Project.objects.create(
                title="Electronic Shop / Olivier Store",
                slug="electronic-shop-olivier-store",
                description="An e-commerce platform for selling electronics and accessories with product management, cart, checkout flow, and customer-focused search experience.",
                technologies="Python, Django, HTML, CSS, JavaScript, SQLite",
                image="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=900&q=80",
                github_url="https://github.com/",
                live_url="https://example.com/",
                featured=True,
                is_published=True,
            )
            Project.objects.create(
                title="Student Management System",
                slug="student-management-system",
                description="A system for managing student records, academic information, and administrative operations in a structured and organized workflow.",
                technologies="Python, Django, SQLite, HTML, CSS",
                image="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=900&q=80",
                github_url="https://github.com/",
                live_url="",
                featured=False,
                is_published=True,
            )
            Project.objects.create(
                title="Flutter / Firebase Student CRUD Application",
                slug="flutter-firebase-student-crud-application",
                description="A mobile application for performing student create, read, update, and delete operations with Firebase-backed data handling.",
                technologies="Flutter, Dart, Firebase, Mobile UI",
                image="https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&w=900&q=80",
                github_url="https://github.com/",
                live_url="",
                featured=True,
                is_published=True,
            )
            Project.objects.create(
                title="Django E-Commerce System",
                slug="django-e-commerce-system",
                description="A web-based commerce application built in Django focused on product catalog management and business-ready online selling flows.",
                technologies="Python, Django, HTML, CSS, JavaScript, SQLite",
                image="https://images.unsplash.com/photo-1556740749-887f6717d7e4?auto=format&fit=crop&w=900&q=80",
                github_url="https://github.com/",
                live_url="https://example.com/",
                featured=False,
                is_published=True,
            )

        if Skill.objects.count() == 0:
            skill_groups = [
                ("Programming", [
                    ("Python", "Advanced"),
                    ("JavaScript", "Intermediate"),
                    ("HTML", "Advanced"),
                    ("CSS", "Advanced"),
                    ("Dart", "Beginner"),
                ]),
                ("Frameworks and Technologies", [
                    ("Django", "Advanced"),
                    ("Flutter", "Intermediate"),
                ]),
                ("Databases", [
                    ("SQLite", "Advanced"),
                    ("MySQL", "Intermediate"),
                    ("Firebase", "Intermediate"),
                ]),
                ("Development Tools", [
                    ("Git", "Advanced"),
                    ("GitHub", "Advanced"),
                    ("Visual Studio Code", "Advanced"),
                    ("Android Studio", "Intermediate"),
                ]),
                ("Software Development", [
                    ("Object-Oriented Programming", "Advanced"),
                    ("CRUD applications", "Advanced"),
                    ("REST APIs", "Intermediate"),
                    ("Database design", "Advanced"),
                    ("Authentication", "Intermediate"),
                    ("E-commerce systems", "Advanced"),
                    ("Software requirements analysis", "Intermediate"),
                ]),
            ]
            for category, items in skill_groups:
                for name, proficiency in items:
                    Skill.objects.create(name=name, category=category, proficiency=proficiency)

        if Experience.objects.count() == 0:
            Experience.objects.create(
                position="TVET Trainer / Software Development",
                company="Independent / Training Practice",
                description="Teaching software development concepts, preparing programming lessons, and guiding learners through practical projects using Python and related technologies.",
                start_date=None,
                end_date=None,
                current=True,
            )

        if Education.objects.count() == 0:
            Education.objects.create(
                institution="University of Rwanda Polytechnic – Musanze College",
                qualification="Advanced Diploma in E-Commerce",
                description="Focused on e-commerce systems, digital business, and technology-enabled business solutions.",
                start_date=None,
                end_date=None,
            )
            Education.objects.create(
                institution="Catholic University of Rwanda",
                qualification="Bachelor's Degree in Computer Science",
                description="Currently studying computer science with interest in software engineering, system design, and practical application development.",
                start_date=None,
                end_date=None,
            )
            Education.objects.create(
                institution="RP Musanze College",
                qualification="A1 ICT / E-Commerce",
                description="Earlier education in ICT and e-commerce fundamentals.",
                start_date=None,
                end_date=None,
            )

        if Service.objects.count() == 0:
            services = [
                ("Web Application Development", "Building modern and functional web applications using Django and other practical web technologies."),
                ("Django Development", "Creating secure and maintainable Django-based web applications with clean backend logic."),
                ("Database Development", "Designing and managing database systems for reliable data handling and application performance."),
                ("E-Commerce Development", "Developing online business solutions for product management, sales, and digital commerce workflows."),
                ("Business Management Systems", "Creating software solutions to improve operations, workflows, and business process management."),
                ("Software Requirements Analysis", "Translating business needs into clear requirements and practical software features."),
                ("Website Development", "Building responsive and professional websites that communicate a clear digital presence."),
                ("Technical Training", "Supporting learners and teams through software development lessons and practical technical coaching."),
            ]
            for title, description in services:
                Service.objects.create(title=title, description=description)

        self.stdout.write(self.style.SUCCESS("Portfolio sample data seeded successfully."))
