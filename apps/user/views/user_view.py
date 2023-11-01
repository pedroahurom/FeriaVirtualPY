from rest_framework.viewsets import ModelViewSet
from apps.user.models.user_model import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.user.serializers.user_serializer import UserSerializer
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'username'
    pagination_class = None
    #filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username', 'email']
    http_method_names = ['get', 'post', 'put', 'patch']

    def get_queryset(self):
        return User.objects.filter(is_active=True).order_by('-date_joined')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
