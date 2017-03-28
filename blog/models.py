from django.db import models
from wagtail.wagtailcore.blocks import StreamBlock, RichTextBlock, StructBlock, CharBlock, TextBlock

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, StreamFieldPanel)
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='tagged_items')

class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock()
    alt = CharBlock()

class CodeBlock(StructBlock):
    code = TextBlock(icon="pilcrow")
    language = CharBlock()

class BlogStreamBlock(StreamBlock):
    text_content = RichTextBlock(icon="pilcrow")
    image = ImageBlock(label="Image", icon="image")
    code = CodeBlock(label="Code", icon="code")

class BlogPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    date = models.DateField("Post date")
    body = StreamField(BlogStreamBlock())

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('main_image'),
        FieldPanel('tags'),
        StreamFieldPanel('body'),
    ]