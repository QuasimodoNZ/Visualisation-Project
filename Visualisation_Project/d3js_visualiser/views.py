from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
def some_view(request):
   return render_to_response('d3js_visualiser/index.html')
