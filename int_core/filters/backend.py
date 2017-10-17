from rest_framework.filters import BaseFilterBackend


class IsNotCompleteFilterBackend(BaseFilterBackend):
    """
    Filter that only allows users to see only complete objects.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(complete=False)


class IsOwnerFilterBackend(BaseFilterBackend):
    """
    Filter that only allows users to see only own objects.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user=request.user)
