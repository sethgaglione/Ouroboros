import datetime

from django import test
from django.template.loader import render_to_string
from django.utils import html, timezone

from hacker import models as hacker_models


class SharedTestCase(test.TestCase):
    def setUp(self):
        self.email = "dummy@email.com"
        self.password = "dummypwd"
        self.first_name = "Kennedy"
        self.last_name = "Doe"

        self.hacker = hacker_models.Hacker(
            email=self.email,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name,
            is_active=True,
        )
        self.hacker.save()

        self.email2 = "dummy2@email.com"
        self.password2 = "bigdummypwd"
        self.first_name2 = "John"
        self.last_name2 = "Doe"

        self.hacker2 = hacker_models.Hacker(
            email=self.email2,
            password=self.password2,
            first_name=self.first_name2,
            last_name=self.last_name2,
            is_active=True,
        )
        self.hacker2.save()

    def create_active_wave(self):
        start = timezone.now() - datetime.timedelta(days=1)
        end = start + datetime.timedelta(days=30)

        self.wave1 = hacker_models.Wave(start=start, end=end)
        self.wave1.save()

    def assertEmailBodiesEqual(self, template_name, context, email):
        html_output = render_to_string(template_name, context)
        stripped = html.strip_tags(html_output)
        self.assertEqual(email.body, stripped)