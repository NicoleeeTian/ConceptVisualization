# -*- coding: utf-8 -*-

from django.urls import re_path,path
from . import views
from mptt_graph.views import ModelListGraphsView, ModelGraphView, ModelGraphInlineView


urlpatterns = [
    re_path('^(?P<modpath>[-._\w]+)/(?P<pk>[0-9]+)/$', ModelGraphInlineView.as_view(), name="mpttgraph-inline"),
    re_path('^(?P<modpath>[-._\w]+)/(?P<pk>[0-9]+)/$', ModelGraphView.as_view(), name="mpttgraph-detail"),
    re_path('^', ModelListGraphsView.as_view(), name="mpttgraph-index"),
]
