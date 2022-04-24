from django.forms import ValidationError
from rest_framework.serializers import ModelSerializer,CharField
from django.contrib.auth import get_user_model


User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    password2 = CharField()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
        ]
        extra_kwargs = { 'password': {'write_only': True},
        'password2': {'write_only': True},
        }

    def validate(self, data):
        pass2 = data.get("password2")
        password = data.get("password")
        print(type(password),type(pass2))

        if password != pass2:
            return ValidationError("Passwords must match.")
        return data


    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        print(username,password)

        try:
            user_obj = User(
                username=username,
                email= email
            )
            user_obj.set_password(password)
            user_obj.save()
        except ValidationError as e:
            print(e)
            
        return validated_data