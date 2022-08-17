# define all url mappings related to learning_logs app
from django.urls import path
from . import views

# this is the namespace
app_name = 'learning_logs'

urlpatterns = [
    # home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/topic_<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry_<int:topic_id>', views.new_entry, name='new_entry'),
    path('edit_entry_<int:entry_id>/', views.edit_entry, name='edit_entry'),

]
