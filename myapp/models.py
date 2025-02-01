from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    
    # Translations
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def get_translated_question(self, lang='en'):
        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn,
        }
        if lang != 'en' and translations.get(lang):
            return translations[lang]
        return self.question

    def get_translated_answer(self, lang='en'):
        if lang != 'en' and hasattr(self, f"answer_{lang}"):
            return getattr(self, f"answer_{lang}")
        return self.answer

    def save(self, *args, **kwargs):
        translator = Translator()
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, src='en', dest='bn').text
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
