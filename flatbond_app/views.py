from django.shortcuts import render

# Create your views here.
def flatbond_detail(client_id):
    return 0
def index(request):
    #if request.method == 'POST':
    return render(request, 'index.html')
