from django.db import models
from django.utils.translation import ugettext as _
from markdown import markdown


class Category(models.Model):
    """
    Category models
    """
    title = models.CharField(verbose_name=_(u'Title'),
                             help_text=_(u' '),
                             max_length=255
                             )
    slug = models.SlugField(verbose_name=_(u'Slug'),
                            help_text=_(u'Uri identifier'),
                            max_length=255,
                            unique=True
                            )

    class Meta:
        app_label = _(u'blog')
        verbose_name = _(u'Category')
        verbose_name_plural = _(u'Categories')
        ordering = ['title']

    def __unicode__(self):
        return '{}'.format(self.title)


class Article(models.Model):
    """
    Article model
    """
    title = models.CharField(verbose_name=_(u'Title'),
                             help_text=_(u' '),
                             max_length=255
                             )

    slug = models.SlugField(verbose_name=_(u'Slug'),
                            help_text=_('Uri identifier'),
                            max_length=255,
                            unique=True
                            )

    content_markdown = models.TextField(verbose_name=_(u'Content (Markdown)'),
                                        help_text=_(' ')
                                        )

    content_markdup = models.TextField(verbose_name=_(u'Content (Markup)'),
                                       help_text=_(' ')
                                       )

    categories = models.ManyToManyField(Category,
                                        verbose_name=_(u'Categories'),
                                        help_text=_(u' '),
                                        null=True,
                                        blank=True
                                        )
    date_publish = models.DateTimeField(verbose_name=_(u'Publish Data'),
                                        help_text=_(u' ')
                                        )

    class Meta:
        app_label = _(u'blog')
        verbose_name = _(u'Article')
        verbose_name_plural = _(u'Articles')
        ordering = ['-date_publish']

    def save(self):
        self.content_markdown = markdown(self.content_markdown, ['codehilite'])
        super(Article, self).save()

    def __unicode__(self):
        return "{}".format(self.title,)













































