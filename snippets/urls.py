from django.urls import path
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

snippet_list = views.SnippetViewSet.as_view({'get': 'list', 'post': 'create'})
snippet_detail = views.SnippetViewSet.as_view({
    'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'
})
snippet_highlight = views.SnippetViewSet.as_view({'get': 'highlight'},
                                                 renderer_classes=[renderers.StaticHTMLRenderer])
user_list = views.UserViewSet.as_view({'get': 'list'})
user_detail = views.UserViewSet.as_view({'get': 'retrieve'})

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])
