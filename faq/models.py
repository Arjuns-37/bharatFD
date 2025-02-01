from venv import logger
from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache
translator = Translator()
class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)
    def get_translated_question(self, lang='en'):
        cached_question = cache.get(f"faq_{self.id}_question_{lang}")
        if cached_question:
            return cached_question
        if lang == 'hi' and self.question_hi:
            cache.set(f"faq_{self.id}_question_{lang}", self.question_hi)
            return self.question_hi
        elif lang == 'bn' and self.question_bn:
            cache.set(f"faq_{self.id}_question_{lang}", self.question_bn)
            return self.question_bn
        translated = self.translate_text(self.question, lang)
        cache.set(f"faq_{self.id}_question_{lang}", translated)
        return translated

    def get_translated_answer(self, lang='en'):
        cached_answer = cache.get(f"faq_{self.id}_answer_{lang}")
        if cached_answer:
            return cached_answer
        if lang == 'hi' and self.answer_hi:
            cache.set(f"faq_{self.id}_answer_{lang}", self.answer_hi)
            return self.answer_hi
        elif lang == 'bn' and self.answer_bn:
            cache.set(f"faq_{self.id}_answer_{lang}", self.answer_bn)
            return self.answer_bn
        translated = self.translate_text(self.answer, lang)
        cache.set(f"faq_{self.id}_answer_{lang}", translated)
        return translated

    def translate_text(self, text, lang):
        try:
            translation = translator.translate(text, src='en', dest=lang)
            return translation.text
        except Exception as e:
            logger.error(f"Translation failed: {e}")
            return text

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, 'bn')
        if not self.answer_hi:
            self.answer_hi = self.translate_text(self.answer, 'hi')
        if not self.answer_bn:
            self.answer_bn = self.translate_text(self.answer, 'bn')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
