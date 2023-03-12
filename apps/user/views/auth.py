from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.views import TokenViewBase

from utilities.mixins import ResponseViewMixin


class CustomTokenViewBase(TokenViewBase, ResponseViewMixin):
    """
    Class to override TokenViewBase
    """

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return self.success_response(data=serializer.validated_data, code=status.HTTP_200_OK)


class CustomTokenObtainPairView(CustomTokenViewBase):
    _serializer_class = api_settings.TOKEN_OBTAIN_SERIALIZER


class CustomTokenRefreshView(CustomTokenViewBase):
    _serializer_class = api_settings.TOKEN_REFRESH_SERIALIZER
