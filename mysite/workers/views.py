from django.shortcuts import render
from workers.models import Employee, JobPosition
from workers.serializers import EmployeeSerializer, JobPositionSerializer
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status


class EmployeeList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class EmployeeList(mixins.ListModelMixin,
#                    mixins.CreateModelMixin):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         def create(self, validated_data):
#             return Employee.objects.create(**validated_data)
#
#         return self.create(request, *args, **kwargs)
#

class JobPositionList(generics.ListCreateAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer


class EmployeeDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

        # def get_object(self, pk):
        #     try:
        #         return Employee.objects.get(id=pk)
        #     except Employee.DoesNotExcist:
        #         raise Http404
        #
        # def get(self, request, pk, format=None):
        #     emp = self.get_object(pk)
        #     serializer = EmployeeSerializer(emp)
        #     return Response(serializer.data)
        #
        # def put(self, request, pk, format=None):
        #     emp = self.get_object(pk)
        #     serializer = EmployeeSerializer(emp, data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data)
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #
        # def delete(self, request, pk, format=None):
        #     emp = self.get_object(pk)
        #     emp.delete()
        #     return Response(status=status.HTTP_204_NO_CONTENT)
