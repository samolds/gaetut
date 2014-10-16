from django.conf import settings
from django.db import models
#import markdown


class Website(models.Model):
    """Description of the Website model
    """
    choices = (
        ('prsl', 'Personal'),
        ('mntn', 'Maintain'),
        ('dvlp', 'Develop'),
    )

    url = models.CharField(max_length=100, unique=True)
    display = models.CharField(max_length=50)
    note = models.CharField(max_length=50, blank=True, null=True)
    kind = models.CharField(max_length=4, choices=choices)
    private = models.BooleanField()

    def __unicode__(self):
        return "%s" % self.display

    def save(self, *args, **kwargs):
        self.url = self.url.lower()
        super(Website, self).save(*args, **kwargs)

    class Meta:
        verbose_name = (u"Website")
        verbose_name_plural = (u"Websites")

