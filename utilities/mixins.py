from rest_framework import status
from rest_framework.response import Response


class ResponseViewMixin(object):
    @classmethod
    def response(cls, code, message=None, data=None, headers=None):
        if headers is None:
            headers = {}
        headers.update({'status': code})
        return Response(
            headers=headers,
            status=code,
            data={
                'message': message,
                'status': code,
                'data': data,
            },
            content_type='application/json'
        )

    @classmethod
    def success_response(cls, data=None, message=None, code=status.HTTP_200_OK, headers=None):
        return cls.response(code, message, data, headers)

    @classmethod
    def error_response(cls, data=None, message=None, code=status.HTTP_400_BAD_REQUEST, headers=None):
        return cls.response(code, message, data, headers)

    @classmethod
    def unauthorised_response(cls, data=None, message=None, code=status.HTTP_401_UNAUTHORIZED, headers=None):
        return cls.response(code, message, data, headers)
