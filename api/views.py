from models import SitePassword
from rest_framework import viewsets
from rest_framework.response import Response
from serializers import SitePasswordSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SitePassword to be viewed or edited.
    """
    queryset = SitePassword.objects.all()
    serializer_class = SitePasswordSerializer

    def list(self, request):
        queryset = SitePassword.objects.filter(user=request.user)
        serializer = SitePasswordSerializer(queryset, many=True)
        return Response(serializer.data)
