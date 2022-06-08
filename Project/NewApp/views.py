from django.shortcuts import render
from .models import Library
from .serializers import LibrarySerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class LibraryDetails(APIView):

    def get(self,request):
        #form = Library()
        #return render(request,'addbooks.html',{'form':form})
        lib = Library.objects.all()

        serializer = LibrarySerializer(lib,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer =LibrarySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class LibraryInfo(APIView):
     def get(self,request,id):
         if id:
             try:
                 lib = Library.objects.get(id=id)
             except Library.DoesNotExist:
                 return Response({'msg':'record does not exist'})
             serializer=LibrarySerializer(lib)
             return Response(serializer.data)
         return Response({'msg':'plz provide id'})

     def put(self,request,id):
         if id:
             try:
                 lib=Library.objects.get(id=id)
             except Library.DoesNotExist:
                 return Response({'msg':'record does not exist'})
             serializer =LibrarySerializer(lib,data=request.data,partial=True)
             if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data)
             return Response({'msg':'plz send valid data'})

     def delete(self,request,id):
         if id:
             try:
                 lib=Library.objects.get(id=id)
             except Library.DoesNotExist:
                 return Response({'msg':'record deleted successfully'})
             lib.delete()
             return Response({'msg':'record deleted successfully'})
         return Response({'msg':'please send it '})

