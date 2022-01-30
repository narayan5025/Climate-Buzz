from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse

from .models import Segment

# Create your views here.

def index(request):
    segments = Segment.objects
    return render(request, 'segments/index.html',{'segments':segments})

def detail(request,segment_id):
    segment_detail = get_object_or_404(Segment,pk=segment_id)
    return render(request, 'segments/detail.html', {'segment':segment_detail})
