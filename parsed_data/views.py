from django.shortcuts import render, redirect
from .models import BlogData,BigData
from .serializers import BigDataSerializer
from rest_framework import permissions
from rest_framework import viewsets


def data(request):
        blogdata=BlogData.objects.all()


        context= {
                'blogdata':blogdata,
        }
        return render(request, 'work_1.html',context)

class BigDataView(viewsets.ModelViewSet):
    queryset = BigData.objects.all()
    serializer_class = BigDataSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
