import pytest
from .models import FAQ

@pytest.mark.django_db
def test_faq_creation():
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a Python web framework.",
        question_hi="Django kya hai?",
        answer_hi="Django ek Python web framework hai."
    )
    assert faq.question == "What is Django?"
    assert faq.get_translated_question('hi') == "Django kya hai?"
    assert faq.get_translated_answer('hi') == "Django ek Python web framework hai."
