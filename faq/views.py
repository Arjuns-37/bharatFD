from django.shortcuts import render
from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer
def home(request):
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()
    for faq in faqs:
        faq.question_translated = getattr(faq, f'question_{lang}', faq.question)  
        faq.answer_translated = getattr(faq, f'answer_{lang}', faq.answer)  
    return render(request, 'faq/home.html', {'faqs': faqs, 'lang': lang})
class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        lang = self.request.query_params.get('lang', 'en')  # Default to 'en'
        context['lang'] = lang
        return context
