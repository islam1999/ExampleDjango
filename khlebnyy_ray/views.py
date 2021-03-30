from django.shortcuts import render
from collections import Counter
def home(request):
    return render(request, 'home.html')

def reverse (request):
    text = request.GET['name']
    reversed_text =  len(text.split())
    return render(request, 'reverse.html', {'name':text, 'r':reversed_text})
