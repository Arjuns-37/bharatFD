from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer, FAQDetailSerializer
from rest_framework.response import Response
from django.shortcuts import render

class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQDetailSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        lang = self.request.query_params.get('lang', 'en')
        context['lang'] = lang
        return context
    
def home(request):
    return render(request, 'home.html')
