from bookmarks.models import Bookmark
from django.contrib import admin

class BookmarkModelAdmin(admin.ModelAdmin):
	readonly_fields = ['url_title']

	def __init__(self, *args, **kwargs):
		super(BookmarkModelAdminForm, self).__init__(*args, **kwargs)
		if kwargs.get('instance') is not None:
			self.fields['url_title'] = ReadOnlyField()
 
admin.site.register(Bookmark)