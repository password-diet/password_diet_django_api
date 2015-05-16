from models import SitePassword
from rest_framework import serializers


class SitePasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SitePassword
        fields = ('id', 'url', 'password', 'created', 'modified')
