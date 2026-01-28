from rest_framework import serializers
from .models import CareerApplication,ContactMessage,MOU,GalleryImage,Project,CommunityItem
import re


class CareerApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerApplication
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"

class MOUSerializer(serializers.ModelSerializer):
    class Meta:
        model = MOU
        fields = "__all__"

class GalleryImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = GalleryImage
        fields = ['id', 'title', 'category', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url
    

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class CommunityItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityItem
        fields = "__all__"


from .models import CpuInquiry

class CpuInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = CpuInquiry
        fields = '__all__'


       
    def validate_phone(self, value):
        if not re.fullmatch(r'\d{10}', value):
            raise serializers.ValidationError(
                "Phone number must be exactly 10 digits."
            )
        return value

 
    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")

        # strict email regex (production safe)
        email_regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        if not re.fullmatch(email_regex, value):
            raise serializers.ValidationError(
                "Enter a valid email address."
            )

        return value