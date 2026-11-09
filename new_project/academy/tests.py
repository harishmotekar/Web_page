from django.test import TestCase
from django.urls import reverse

from .models import Inquiry


class AcademyPageTests(TestCase):
    def test_homepage_shows_course_content(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Learn the skills")

    def test_course_catalog_and_detail(self):
        response = self.client.get(reverse("courses"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Data Science Foundations")

        detail = self.client.get(
            reverse("course_detail", kwargs={"slug": "generative-ai-llms"})
        )
        self.assertEqual(detail.status_code, 200)
        self.assertContains(detail, "Prompt design")

    def test_invalid_course_returns_404(self):
        response = self.client.get(
            reverse("course_detail", kwargs={"slug": "not-a-course"})
        )
        self.assertEqual(response.status_code, 404)

    def test_contact_form_saves_inquiry(self):
        response = self.client.post(
            reverse("contact"),
            {
                "name": "Alex Learner",
                "email": "alex@example.com",
                "course": "Generative AI & LLMs",
                "message": "I would like to learn more.",
            },
        )
        self.assertRedirects(response, reverse("contact"))
        self.assertEqual(Inquiry.objects.count(), 1)
        self.assertEqual(Inquiry.objects.get().email, "alex@example.com")

    def test_contact_form_rejects_invalid_email(self):
        response = self.client.post(
            reverse("contact"),
            {"name": "Alex", "email": "not-an-email", "course": "", "message": ""},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Inquiry.objects.count(), 0)
        self.assertContains(response, "Enter a valid email address")
