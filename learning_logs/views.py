from django.shortcuts import render

# Create your views here.
def index(request):
    # this receives request from url and then process the data for template of home page
    return render(request=request,template_name='learning_logs/index.html')