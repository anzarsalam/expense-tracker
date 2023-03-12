from rest_framework import serializers

from apps.user.models import AppUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('username', 'first_name', 'last_name', 'password', 'email')

    def save(self, **kwargs):
        password = self.validated_data.pop('password')
        user = super(RegisterSerializer, self).save(**kwargs)
        user.set_password(password)
        user.save()
        return user
