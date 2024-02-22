from telnetlib import STATUS
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# Create your views here.
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from company.models import Epmloyee ,TeamLeader
from .serilaizares import EmployeeSerilazer

@api_view(['GET', 'POST'])
def MyAPIView(request):
        # data=Epmloyee.objects.all()
        # seralizer=EmployeeSerilazer(data,many=True)
        # return Response(seralizer.data)
        if request.method == 'GET':
              emps =Epmloyee.objects.all()
              seralizer=EmployeeSerilazer(emps,many=True)
              return Response(seralizer.data)
       
        if request.method == 'POST':
            data=request.data
            seralizer=EmployeeSerilazer(data=data)
            if seralizer.is_valid():
                seralizer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
# calsses base view 
# @api_view(["GET", "POST"])
class MyAPIView2(APIView):
    def get(self,request):
        Epmloyees=Epmloyee.objects.all()
        seralizer=EmployeeSerilazer(Epmloyees,many=True)
        return Response(seralizer.data)
    
    def post(self,request):
        data=request.data
        seralizer=EmployeeSerilazer(data=data)
        if seralizer.is_valid():
            seralizer.save()
            Epmloyees=Epmloyee.objects.all()
            all_data=EmployeeSerilazer(seralizer.data)
            return Response({"emplyees":all_data.data},status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
  # view set       
class MyAPIView3(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerilazer
    queryset = Epmloyee.objects.all()