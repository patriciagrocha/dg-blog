from django.shortcuts import render
from django.http import HttpResponse

def post_list(req):
    return render(req, 'blog/post_list.html', {})