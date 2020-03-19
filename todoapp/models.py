from django.db import models


class TodoList(models.Model):
    task = models.CharField(max_length = 250)
    

    def __str__(self):
        return self.task
    
