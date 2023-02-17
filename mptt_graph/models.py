from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import TreeForeignKey, MPTTModel


class GraphModel(models.Model):
    title = models.CharField(max_length=200, verbose_name=_(u"Title"))
    model_path = models.CharField(max_length=200, verbose_name=_(u"Model path"),
                                  help_text=_(u"Path to the model"))
    model_pk = models.PositiveSmallIntegerField(
        verbose_name=_(u"Root node primary key"))
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class TreeNode(MPTTModel):
    type_choices = [
        ('Topic', 'Topic'),
        ('Example', 'Example'),
        ('Attribute', 'Attribute'),
        ('Reason', 'Reason'),
        ('Theory', 'Theory'),
    ]
    title = models.CharField(max_length=200, verbose_name=_(u"Title"))
    parent = TreeForeignKey('self', null=True, blank=True, related_name=u'children',
                            verbose_name=_(u'Parent node'), on_delete=models.CASCADE)
    node_id = models.IntegerField(null=True, blank=True)
    vote = models.IntegerField(default=0)
    type = models.CharField(max_length=20,choices=type_choices,default='Topic')
    # comment = models.TextField(max_length=500)

    def __str__(self):
        return self.title
