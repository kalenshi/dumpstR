from rest_framework import serializers

from .models import ContactEnroll


class ContactEnrollSerializer(serializers.ModelSerializer):
    """
    Serializer class for the enroll contact model
    """

    class Meta:
        model = ContactEnroll
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone",
            "message",
            "contact_date",
            "company",
        )
        extra_kwargs = {
            "phone": {"required": False},
            "message": {"required": False},
            "contact_date": {"required": False},
            "company": {"required": False},
        }
