from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page

from portfolio.models import PortfolioPage


class HomePage(Page):
    pass
    
    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        projects = PortfolioPage.objects.live().order_by('priority')
        
        context['projects'] = projects
        
        return context
