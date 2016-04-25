#-*- encoding=utf8 -*-

from django.db import models
from django.core.urlresolvers import reverse
# from django.contrib,sites.models import Site


class Article(models.Model):
	title = models.CharField(max_length=100)   #the title of blog
	category = models.CharField(max_length=50, blank=True)   #blog分类，可为空
	tag = models.ManyToManyField('Tag',blank=True)   #blog标签
	date_time = models.DateTimeField(auto_now_add=True)   #blog时间
	content = models.TextField(blank=True, null=True)   #blog正文

	def get_absolute_url(self):
		path = reverse('detail', kwargs={'id':self.id})
		return "http://127.0.0.1:8000%s" % path

	def __unicode__(self):
		return self.title.encode('utf-8')


	#按时间下降排序
	class Meta:
		ordering = ['-date_time']


class Tag(models.Model):
	tag_name = models.CharField(max_length=60)

	#display the tag_name
	def __unicode__(self):
		return self.tag_name