from django import forms

from wagtail.wagtailcore.blocks import (TextBlock, StructBlock, StreamBlock,
                                        FieldBlock, CharBlock, RichTextBlock, 
                                        RawHTMLBlock, ListBlock)
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock


class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', 'Wrap left'), ('right', 'Wrap right'), ('mid', 'Mid width'), ('full', 'Full width'),
    ))
    
class ImageSeriesFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('square_md', 'Square Medium Res - 400 x 400'), ('rect_lg', 'Rectangle Medium Res - 600x400'),
    ))                                       
                                                                               
class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock()
    alt = CharBlock()
    alignment = ImageFormatChoiceBlock()
    
class PullQuoteBlock(StructBlock):
    quote = TextBlock("quote title")
    attribution = CharBlock()

    class Meta:
        icon = "openquote"

        
class HTMLAlignmentChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('normal', 'Normal'), ('full', 'Full width'),
    ))        
        
 
class AlignedHTMLBlock(StructBlock):
    html = RawHTMLBlock()
    alignment = HTMLAlignmentChoiceBlock()

    class Meta:
        icon = "code"   


class BlogStreamBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    paragraph = RichTextBlock(icon="pilcrow")
    aligned_image = ImageBlock(label="Aligned image", icon="image")
    pullquote = PullQuoteBlock()
    aligned_html = AlignedHTMLBlock(icon="code", label='Raw HTML')
    document = DocumentChooserBlock(icon="doc-full-inverse")
