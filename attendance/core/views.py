from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Staff, Attendance
from .serializers import CustomUserSerializer, StaffSerializer, AttendanceSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser


class CustomUserCreate(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        custom_user = CustomUser.objects.get(pk=pk)
        serializer = CustomUserSerializer(custom_user)
        return Response(serializer.data)

    def put(self, request, pk):
        custom_user = CustomUser.objects.get(pk=pk)
        serializer = CustomUserSerializer(custom_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        custom_user = CustomUser.objects.get(pk=pk)
        custom_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StaffList(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffDetail(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        staff = Staff.objects.get(pk=pk)
        serializer = StaffSerializer(staff)
        return Response(serializer.data)

    def put(self, request, pk):
        staff = Staff.objects.get(pk=pk)
        serializer = StaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        staff = Staff.objects.get(pk=pk)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AttendanceList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        attendance = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttendanceDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        attendance = Attendance.objects.get(pk=pk)
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)

    def delete(self, request, pk):
        attendance = Attendance.objects.get(pk=pk)
        attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MarkAttendance(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


