from django.db import models

# Create your models here.

answer_choices = (("Sí asistiré", "Sí asistiré"), ("No asistiré", "No asistiré"))

class Guests(models.Model):
    '''
    
    '''
    identifier = models.CharField(max_length = 100, blank = False, null = False)
    code = models.CharField(max_length = 6, blank = True, null = True, unique = True)
    num_guests_assigned = models.IntegerField(max_length = 10)
    num_guests_selected = models.IntegerField(max_length = 10, null = True, blank = True)
    num_guests_selected_char = models.CharField(max_length = 50, blank = True, null = True)
    answer = models.CharField(max_length = 100, blank = True, null = True, choices = answer_choices, default = "Pendiente") 
    guests_names = models.CharField(max_length = 800, blank = True, null = True)
    wish_text = models.TextField(blank = True, null = True)
    
    def __str__(self):
        return str(self.id)
    