from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.conf import settings

from .serializers import (
    CareerApplicationSerializer,
    ContactMessageSerializer,
    MOUSerializer,
    GalleryImageSerializer,
    ProjectSerializer,
    CommunityItemSerializer,
    CpuInquirySerializer,
)

from .models import (
    CareerApplication,
    ContactMessage,
    MOU,
    GalleryImage,
    Project,
    CommunityItem,
)

import traceback


# ---------------- CAREER APPLICATION ----------------
class CareerApplicationCreate(APIView):
    def post(self, request):
        serializer = CareerApplicationSerializer(data=request.data)

        if serializer.is_valid():
            application = serializer.save()

            subject = "New Career Application Received"
            body = f"""
New Career Application Submitted

Full Name: {application.full_name}
Email: {application.email}
Phone: {application.phone}

College: {application.college}
CGPA: {application.cgpa}
Year of Passing: {application.year_of_passing}
Experience: {application.experience}

Skills:
{application.skills}
"""

            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.EMAIL_HOST_USER],
            )

            if application.resume:
                email.attach_file(application.resume.path)

            try:
                email.send()
                email_status = "Email sent successfully"
            except Exception as e:
                print("Career email error:", e)
                email_status = f"Email failed: {e}"

            return Response(
                {
                    "message": "Application submitted successfully",
                    "email_status": email_status,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------------- CONTACT MESSAGE ----------------
class ContactMessageCreate(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)

        if serializer.is_valid():
            contact = serializer.save()

            try:
                send_mail(
                    subject=f"New Contact: {contact.subject}",
                    message=f"""
Name: {contact.name}
Email: {contact.email}
Phone: {contact.phone}

Message:
{contact.message}
""",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                email_status = "Email sent successfully"
            except Exception as e:
                print("Contact email error:", e)
                email_status = f"Email failed: {e}"

            return Response(
                {
                    "message": "Message received successfully",
                    "email_status": email_status,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------------- MOU ----------------
class MOUListAPIView(ListAPIView):
    serializer_class = MOUSerializer

    def get_queryset(self):
        return MOU.objects.filter(is_active=True)


# ---------------- GALLERY ----------------
class GalleryImageListAPIView(ListAPIView):
    serializer_class = GalleryImageSerializer

    def get_queryset(self):
        return GalleryImage.objects.all().order_by("-created_at")


# ---------------- PROJECTS ----------------
class ProjectListAPIView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


# ---------------- COMMUNITY ----------------
class CommunityItemListAPIView(ListAPIView):
    serializer_class = CommunityItemSerializer

    def get_queryset(self):
        return CommunityItem.objects.filter(section="giveback").order_by("-created_at")


# ---------------- CPU INQUIRY ----------------
@api_view(["POST"])
def create_inquiry(request):
    serializer = CpuInquirySerializer(data=request.data)

    if serializer.is_valid():
        inquiry = serializer.save()

        subject = "New CPU Inquiry Received"
        message = f"""
Name: {inquiry.full_name}
Email: {inquiry.email}
Phone: {inquiry.phone}

CPU Model: {inquiry.cpu_model}
Quantity: {inquiry.quantity}
RAM: {inquiry.ram}
Storage: {inquiry.storage}

Message:
{inquiry.message}
"""

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            email_status = "Email sent successfully"
        except Exception as e:
            print("Inquiry email error:", e)
            traceback.print_exc()
            email_status = f"Email failed: {e}"

        return Response(
            {
                "message": "Inquiry submitted successfully",
                "email_status": email_status,
            },
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
