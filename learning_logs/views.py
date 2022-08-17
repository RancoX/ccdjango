from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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


def new_topic(request):
    '''
    The new_topic() view handles two scenarios:

    scenario 1: first time in new_topic
        display an empty TopicForm

    scenario 2: user filled out empty forms and submited it: request.method == 'POST' is the distinguisher
    '''
    if request.method != 'POST':
        # No data submitted, so first time on this page, show blank forms
        form = TopicForm()
    else:
        # POST method was detected
        form = TopicForm(data=request.POST)
        # data validation
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # display an empty form or invalid form if form.is_valid() evaluated to False
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    topic=Topic.objects.get(id=topic_id)

    # if GET method, generate empty form then pass it to template
    if request.method == 'GET':
        form = EntryForm()
    # if POST method, save the form and redirects to topic_<topic_id>
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            reverse_urlpattern = reverse('learning_logs:topic', kwargs={'topic_id': topic_id})
            print(reverse_urlpattern)
            # alternatively return redirect('learning_logs:topic', topic_id=topic_id)
            return redirect(reverse_urlpattern)
    context = {'form': form, 'topic':topic}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    # edit an existing entry
    entry=Entry.objects.get(pk=entry_id)
    topic=entry.topic

    if request.method=='GET':
        # this is the request for prefilled table for editing
        form=EntryForm(instance=entry)
    
    elif request.method=='POST':
        form=EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context={'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html',context=context)
