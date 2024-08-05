from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=60, null=False)
    country = models.CharField(max_length=45, null=False)
    
    def __str__(self) -> str:
        return self.name

class Discos(models.Model):
    name = models.CharField(max_length=45, null=False)
    DISCOS_GENRE = {
        ('Alterantivo', 'Alternativo'),
        ('Blues', 'Blues'),
        ('Grunge', 'Grunge'),
        ('Heavy Metal', 'Heavy Metal'),
        ('Indie', 'Indie'),
        ('Metal', 'Metal'),
        ('Rock', 'Rock'),
        ('Reggaeton', 'Reggaeton'),
        ('Reagge', 'Reagge'),
        ('Pop', 'Pop')
    }
    genre = models.CharField(max_length=45, choices=DISCOS_GENRE, null=False)
    year = models.IntegerField(null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='discos_images')
    
    def __str__(self) -> str:
        return self.name