from django.shortcuts import render

# Create your views here.
def test(request):
    context = {}
    return render(request, "index.html", context)