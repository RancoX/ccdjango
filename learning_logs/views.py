from django.shortcuts import render
from .models import Topic, Entry

# Create your views here.


def index(request):
    # this receives request from url and then process the data for template of home page
    return render(request=request, template_name='learning_logs/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request=request, template_name='learning_logs/topics.html', context=context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
