from django.db import models
from blog.models import BlogPage
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page


class PortfolioPage(BlogPage):
    project_date = models.DateField("Project Date")
    
    content_panels = BlogPage.content_panels + [
         FieldPanel('project_date'),
    ]

class PortfolioIndex(Page):
    pass