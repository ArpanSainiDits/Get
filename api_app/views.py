from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student
from django.shortcuts import get_object_or_404
from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class StudentViews(APIView):
        def post(self, request):
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status" : "success", "data" : serializer.data}, status = status.HTTP_200_OK)
            else :
                return Response({"status" : "error", "data" : serializer.error}, status = status.HTTP_400_BAD_REQUEST)
            
class getStudentViews(APIView):
    def get(self, request, id= None):
                if id :
                    item = Student.objects.get(id=id)
                    serializer = StudentSerializer(item)
                    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
                items = Student.objects.all()
                serializer = StudentSerializer(items, many=True)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK) 
            

class upStudentViews(APIView):
    def patch(self, request, id=None):
        item = Student.objects.get(id=id)
        serializer = StudentSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})            
        
        
class deleteStudentViews(APIView):   
    def delete(self, request, id=None):
        item = get_object_or_404(Student, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})     
    
    