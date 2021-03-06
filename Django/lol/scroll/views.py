from django.shortcuts import render
from django.http import JsonResponse

from time import sleep

# Create your views here.
def index(request):
    return render(request, 'scroll/index.html')

def posts(request):
    start = int(request.GET.get('start') or 0)
    end = int(request.GET.get('end') or (start + 9))
    data = []
    for i in range(start, end+1):
        data.append(f'Post# {i}')
    return JsonResponse(data, safe=False)