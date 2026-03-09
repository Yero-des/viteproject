from django.db import models
from django.templatetags.static import static

# Create your models here.
class Greeting(models.Model):
    # name = models.CharField(blank=True)
    image = models.ImageField(upload_to='greetings')
    updated_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return static('img/rafa.gif') 