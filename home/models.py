from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from blog.models import BlogPage


class HomePage(Page):
    pass

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(HomePage, self).get_context(request)
        content_pages = self.get_children().live().order_by('-first_published_at')
        context['content_pages'] = content_pages
        return context
