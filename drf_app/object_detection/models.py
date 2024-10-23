from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)  # Название предмета
    description = models.TextField()  # Описание предмета

    def __str__(self):
        return self.name
