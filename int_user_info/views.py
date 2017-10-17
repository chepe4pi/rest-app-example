from rest_framework.viewsets import ReadOnlyModelViewSet
from int_user_info.serializers.user_info import UserInfoSerializer
from rest_framework.permissions import IsAuthenticated
from int_core.filters.backend import IsOwnerFilterBackend
from int_user_info.models import UserInfo


class ScoresViewSet(ReadOnlyModelViewSet):

    filter_backends = (IsOwnerFilterBackend,)
    permission_classes = [IsAuthenticated]
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()

    def list(self, request, *args, **kwargs):
        UserInfo.objects.get_or_create(user=request.user)
        return super(ScoresViewSet, self).list(self, request, *args, **kwargs)

    class Meta:
        model = UserInfo
