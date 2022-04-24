from .serializer import UserCreateSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()