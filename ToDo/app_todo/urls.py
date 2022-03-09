from django.urls import path
from .views import list_todo_view, create_todo_view, todo_view, todo_change_view, todo_complete_view, todo_delete_view
from .views import list_todo_complete_view, todo_complete_info_view

urlpatterns = [
    path('', list_todo_view, name='list_todo'),
    path('complete/', list_todo_complete_view, name='list_todo_complete'),
    path('create/', create_todo_view, name='create_todo'),
    path('todo/<int:todo_pk>/', todo_view, name='todo'),
    path('complete/<int:todo_pk>/', todo_complete_info_view, name='todo_complete_info'),
    path('todo/<int:todo_pk>/change/', todo_change_view, name='change_todo'),
    path('todo/<int:todo_pk>/complete/', todo_complete_view, name='complete_todo'),
    path('todo/<int:todo_pk>/delete/', todo_delete_view, name='delete_todo'),
]
