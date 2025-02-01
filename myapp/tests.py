import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
def test_faq_translation():
    client = APIClient()

    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.",
    )

    # Test default language (English)
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200
    assert "What is Django?" in response.data[0]['translated_question']

    response = client.get(reverse('faq-list') + "?lang=hi")
    assert response.status_code == 200
    assert "Django क्या है?" in response.data[0]['translated_question']
