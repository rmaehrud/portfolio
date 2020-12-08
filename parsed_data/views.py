from django.shortcuts import render, redirect
from .models import BlogData


def data(request):
        blogdata=BlogData.objects.all()

        context= {
                'blogdata':blogdata,
        }
        return render(request, 'work_1.html',context)