from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Tasks
from .serializer import TasksSerializer
from django.utils import timezone
from datetime import date,timedelta
from django.db.models import Q

class TasksDetails(APIView):
    def get(self,request):
        obj = Tasks.objects.all()
        print(obj)
        serializer = TasksSerializer(obj, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        print("********************************")
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class TasksInfo(APIView):
    def get(self,request,value):
        if(value=="this week"):
            today =timezone.now().date()
            print(today) 
            print(today.weekday()) 
            
            print(timedelta(days=today.weekday()))
            week_start = today - timedelta(days = today.weekday())
            print(timedelta(days=7),"******************")
            week_end = week_start + timedelta(days = 7)
            print(week_start,week_end)
            obj = Tasks.objects.filter(Q(assigned_date__range = [week_start, week_end]) or Q(due_date__range = [week_start, week_end])) 
            serializer = TasksSerializer(obj,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif(value=="last week"):
            today = timezone.now().date()
            last_week_start = today - timedelta(days=today.weekday()) - timedelta(days=7)
            last_week_end = last_week_start + timedelta(days=6)
            obj = Tasks.objects.filter(assigned_date__range =[last_week_start,last_week_end]) or Tasks.objects.filter(due_date__range =[last_week_start,last_week_end])
            serializer = TasksSerializer(obj,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            try:
             obj = Tasks.objects.filter(Q(task_name__icontains=value) | Q(priority_level__icontains=value))
            except Tasks.DoesNotExist:
                msg = {"msg":"not found"}
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)
            serializer = TasksSerializer(obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class TasksFetch(APIView):
    def get(self,request,id):
        obj = Tasks.objects.get(id=id)
        serializer = TasksSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self,request,id):
        try:
            obj = Tasks.objects.get(id=id)
            obj.delete()
            return Response({"msg:deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Tasks.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,id):
        try:
            obj = Tasks.objects.get(id=id)
        except Tasks.DoesNotExist:
            msg = {"msg":"not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = TasksSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TasksFilter(APIView):
    def get(self,request,parameter,value):
        if parameter == "":
            try:
                obj = Tasks.objects.filter(Q(task_name__icontains=value) | Q(priority_level__icontains=value))
                serializer = TasksSerializer(obj, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Tasks.DoesNotExist:
                return Response({"msg":"not found"}, status=status.HTTP_204_NO_CONTENT)
        else:
            today = date.today()
            if parameter == "this week":
                start_date = today - timedelta(days=today.weekday())
                end_date = start_date + timedelta(days=6)
            elif parameter == "last week":
                firstweek_date = today - timedelta(days=today.weekday())
                end_date = firstweek_date - timedelta(days=1)
                start_date = end_date - timedelta(days=6)
            else:
                return Response({"msg":"invalid parameter "}, status=status.HTTP_400_BAD_REQUEST)
            week_based_objs = Tasks.objects.filter(
                Q(due_date__range =(start_date,end_date)) |
                Q(assigned_date__lte=end_date, due_date__gte=end_date))
        try:
            obj = week_based_objs.filter(Q(task_name__icontains=value) | Q(priority_level__icontains=value))
            serializer = TasksSerializer(obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Tasks.DoesNotExist:
            return Response({"msg":"not found"}, status=status.HTTP_204_NO_CONTENT)
