from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Greeting
from django.templatetags.static import static

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'dashboard/index.html'
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        gender = self.request.GET.get('gender')
        greeting = "Bienvenido"
        greetings = Greeting.objects.all().order_by(
            '-updated_at')[:6]
        
        imgs_greeting = [
            g.image.url if g.image else static('img/rafa.gif')
            for g in greetings
        ]

        while len(imgs_greeting) < 6:
            imgs_greeting.append(static('img/rafa.gif'))            
        
        if gender == 'f':
            greeting = "Bienvenida"
            
        context.update({
            'name': name,
            'greeting': greeting,
            'gender': gender,
            'imgs_greeting': imgs_greeting
        })
        return context
    