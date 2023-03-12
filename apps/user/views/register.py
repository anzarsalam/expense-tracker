from apps.user.messages import register as messages
from apps.user.serializers.register import RegisterSerializer
from rest_framework.views import APIView

from utilities.mixins import ResponseViewMixin


class RegisterView(APIView, ResponseViewMixin):
    permission_classes = []

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.success_response(message=messages.REGISTRATION_SUCCESSFUL)
        return self.error_response(message=messages.REGISTRATION_FAILED, data=serializer.errors)
