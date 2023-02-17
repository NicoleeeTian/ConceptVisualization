# -*- coding: utf-8 -*-
from django.http.response import Http404
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from mptt_graph.models import GraphModel, TreeNode
from mptt_graph.utils import get_model_from_path
from django.shortcuts import render




class ModelListGraphsView(TemplateView):
    # high level there is a list of graphs 
    template_name = 'mptt_graph/index.html'
    # initialize one global variable primary key as 1
    primary_key = 1
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            raise Http404
        return super(ModelListGraphsView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ModelListGraphsView, self).get_context_data(**kwargs)
        context['graphs'] = GraphModel.objects.all()

        return context
    
    def post(self, request,**kwargs):
        if "new_graph" in request.POST:
            # post method that create new GraphModel object.
            # Whenever we create a new Graph, we should also initialize a TreeNode object as root
            # root has the same title as GraphModel
            title = request.POST.get('title')
            # print(self.primary_key)
            new_graph = GraphModel.objects.create(title=title,model_path="mptt_graph.models.TreeNode",model_pk=self.__class__.primary_key,vote=0)
            new_graph.save()
            t =TreeNode.objects.create(title=title,node_id = self.__class__.primary_key)
            t.save()
            # print(TreeNode.objects.all())
            # update primary key
            self.__class__.primary_key += 1
            
        # elif "vote_up_graph" in request.POST:
        #     num = GraphModel.objects.get(title=request.POST.get('title')).vote
        #     GraphModel.objects.filter(title=request.POST.get('title')).update(vote=num+1)
        # elif "vote_down_graph" in request.POST:
        #     num = GraphModel.objects.get(title=request.POST.get('title')).vote
        #     GraphModel.objects.filter(title=request.POST.get('title')).update(vote=num-1)

        return render(request, self.template_name , {'graphs': GraphModel.objects.all()})


    
    class Meta:
        verbose_name = _(u'Mptt graph')
        verbose_name_plural = _(u'Mptt graphs')
        ordering = ('title',)

    def __str__(self):
        return self.title



class ModelGraphView(TemplateView):
    # low level for each graph
    template_name = 'mptt_graph/tree.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            raise Http404
        return super(ModelGraphView, self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(ModelGraphView, self).get_context_data(**kwargs)
        # print(self.kwargs['modpath']) mptt_graph.models.TreeNode
        model = get_model_from_path(self.kwargs['modpath'])
        root_node_pk = self.kwargs['pk']
        root_node = model.objects.get(node_id=root_node_pk)
        nodes = root_node.get_descendants(include_self=True)
        context['nodes'] = nodes
        print("hhh")
        return context
    
    def post(self, request, **kwargs):
        if 'new_node' in request.POST:
            title = request.POST.get('title')
            parent_title = request.POST.get('parent')
            type = request.POST.get('type')
            print(title)
            parent = TreeNode.objects.get(title=parent_title)
            new_node = TreeNode.objects.create(title=title,parent=parent,type=type)
            new_node.save()
            # update votes in graph
            graph_id = self.kwargs['pk']
            graph_votes = GraphModel.objects.get(model_pk=graph_id).vote
            GraphModel.objects.filter(model_pk=graph_id).update(vote=graph_votes+1)

        elif "delete_node" in request.POST:
            print("why")
            TreeNode.objects.get(title=request.POST.get('title')).delete()

        elif "vote_up_node" in request.POST:
            num = TreeNode.objects.get(title=request.POST.get('title')).vote
            TreeNode.objects.filter(title=request.POST.get('title')).update(vote=num+1)

        elif "vote_down_node" in request.POST:
            num = TreeNode.objects.get(title=request.POST.get('title')).vote
            TreeNode.objects.filter(title=request.POST.get('title')).update(vote=num-1)

        root_node_pk = self.kwargs['pk']
        root_node = TreeNode.objects.get(node_id=root_node_pk)
        nodes = root_node.get_descendants(include_self=True)
        return render(request, self.template_name , {'nodes': nodes})

    def popup(request):
        print('here!')
        return render(request, 'popup.html')


class ModelGraphInlineView(ModelGraphView):
    template_name = 'mptt_graph/tree_inline.html'