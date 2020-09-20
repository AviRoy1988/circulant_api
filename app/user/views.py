from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serealizers import UserSerealizer, AuthTokenSerializer

# Create your views here.

class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerealizer


class CreateTokenAPIView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UpdateRetriveUserAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerealizer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated)

    def get_object(self):
        return self.request.user