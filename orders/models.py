from django.db import models

# Create your models here.

class Order(models.Model):
    order = models.JSONField() # = What?
    customer = models.JSONField()  # = What?  It's a stringify'd object
    # created_at = models.DateTimeField(auto_now_add=True)
    # is_complete = models.BooleanField()
    
    # class Meta:
    #     ordering = ('-created_at',)
        
    def __str__(self):
        return str(self.created_at) 
