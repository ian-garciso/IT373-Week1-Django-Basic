from django.shortcuts import render

# Create your views here.
def home(request):
    ctx = {
        'course':'IT373 - Web System and Technologies 2',
        'week1': 1,
    }
    return render(request, 'pages/home.html', ctx)

def about(request):
    return render(request, 'pages/about.html')


def hello(request):
    return render(request, 'pages/hello.html')