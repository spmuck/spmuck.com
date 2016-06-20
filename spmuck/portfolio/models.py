from django.db import models
from blog.models import BlogPage
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page


class PortfolioPage(BlogPage):
    project_date = models.DateField("Project Date")
    priority = models.SmallIntegerField("Priority", unique='true')
    
    content_panels = BlogPage.content_panels + [
         FieldPanel('project_date'),
         FieldPanel('priority'),
    ]

class PortfolioIndex(Page):
    pass