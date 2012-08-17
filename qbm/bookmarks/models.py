from django.db import models
import urllib
import BeautifulSoup
from django.forms import ModelForm
from django.db import models

# Create your models here.
class Bookmark(models.Model):
	url_text = models.URLField(max_length=100)
	title_text = models.TextField()
	url_title = models.TextField()
	url_date = models.DateTimeField(auto_now=True)

class BookmarkForm(ModelForm):
	class Meta:
		model = Bookmark
		exclude = ('url_title')   

	def save(self):
		soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(self.url_text))
		self.url_title = soup.title.string
		super(Bookmark, self).save()