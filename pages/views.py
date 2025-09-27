from django.shortcuts import render

# Home page view
def home(request):
    ctx = {
        'course': 'IT373 - Web System and Technologies 2',
        'week': 1,  # renamed "week1" → "week" for consistency with template
    }
    return render(request, 'pages/home.html', ctx)

# About page view
def about(request):
    return render(request, 'pages/about.html')
