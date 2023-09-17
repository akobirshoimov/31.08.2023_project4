from django.shortcuts import render,get_object_or_404
from .models import Books,Article
from django.http import JsonResponse
from rest

# Create your views here.
def detail(request,detail_id):
    each = Books.objects.get(id=detail_id)
    each = get_object_or_404(Books,id=detail_id)
    info = f'book name:{Books.name}, page : {Books.page}'
    return JsonResponse(info)

def all(request):
    all = Article.objects.all()
    result = [] 
    for i in all:
        result.append({
            'name':i.name,
            'page':i.page,
            'publish_date': i.pub_date
        })
    return JsonResponse(result,safe = False)


