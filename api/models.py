from django.db import models


class Highscore(models.Model):
    score = models.IntegerField(null=False)
    name = models.CharField(max_length=200, null=False)
    posted = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-score',)