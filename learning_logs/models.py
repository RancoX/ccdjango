from tabnanny import verbose
from django.db import models

# Create your models here.
class Topic(models.Model):
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return string representation of the model
        return self.text

class Entry(models.Model):
    # something specific learned about a Topic above
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    text=models.TextField()
    data_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        # this class redefines the meta data of this model class
        # verbose_name_plural tells Django the plural of Entry is Entries rather than Entrys
        verbose_name_plural='entries'
    
    def __str__(self):
        return f"{self.text[:50]}..."