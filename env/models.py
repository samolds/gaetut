from django.conf import settings
from django.db import models
import markdown


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


class Quote(models.Model):
    """Description of the Quote model
    """
    name = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=50)
    quote = models.TextField()
    private = models.BooleanField()

    def __unicode__(self):
        if self.name:
            return "%s" % self.name
        else:
            return "%s" % self.author

    class Meta:
        verbose_name = (u"Quote")
        verbose_name_plural = (u"Quotes")
        ordering = ['-name']


class Post(models.Model):
    """Description of the Post model
    """
    title = models.CharField("title", max_length=100)
    content = models.TextField(blank=True, null=True)
    content_markdown = models.TextField("Content", help_text='<a href="http://daringfireball.net/projects/markdown/syntax">Markdown Help</a>')
    embedded_link = models.CharField(max_length=500, blank=True, null=True)
    private = models.BooleanField()
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField(default=0, blank=True, null=True)

    def __unicode__(self):
        return "%s" % self.title

    def save(self):
        self.content = markdown.markdown(self.content_markdown)
        super(Post, self).save()

    class Meta:
        verbose_name = (u"Post")
        verbose_name_plural = (u"Posts")
