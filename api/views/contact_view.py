from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from api.serializers import ContactEnrollSerializer
from api.models import ContactEnroll


class ContactEnrollView(APIView):
    """
    View for interacting with potential students planning on enrolling
    """
    serializer_class = ContactEnrollSerializer

    def get(selfself, request, format=None):
        """
        Returns potential students who's contact_date is less than or equal
        to the current date in the database
        Args:
            request:
            format:
        Returns:
        """
        ...

    def post(self, request, format=None):
        """
        Creates entries in the database and returns a contact id
        with some text
        Args:
            request:
            format:
        Returns:
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
