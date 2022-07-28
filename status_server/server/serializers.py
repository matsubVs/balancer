from rest_framework import serializers
from models import *

class ServerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerStatus
        fields = ['server_name', 'active_requests']