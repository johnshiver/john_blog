from django.db import models
from django.utils.translation import ugettext as _
from markdown import markdown

class Category(model.Model):
	"""
	Category Model
    """
	title = models.CharField(
	                         verbose_name = _(u'Title'),
							 help_text = _(u' '),
							 max_length = 255
							 )
	
	slug = models.SlugField(
	                        verbose_name = _(u'Slug'),
							help_text = _(u'Uri identifier.'),
							max_length = 255,
							unique = True
							)

	class Meta:
		app_label = _(u'blog')
		verbose_name = _(u'Category')
		ordering = ['title',]

	def __unicode__(self):
		return "{}".format(self.title)


class Article(models.Model):
	"""
	Article Model
	"""
	title = models.CharField(
							 verbose_name = _(u'Title'),
							 verbose_text = _(u' '),
							 max_length = 255
							 )

	slug = models.SlugField(
							verboses_name= _(u'Slug'),
							helpt_text = _(u'Uri identifier.'),
							max_length = 255,
							unique = True
							)

	content_markdown = models.TextField(
										verbose_name = _(u'Content (Markdown)'),
										help_text = _(u' '),
										)
	content_markup = models.TextField(
									   










