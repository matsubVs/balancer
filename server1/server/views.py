from rest_framework.response import Response
from rest_framework.views import APIView
import os
import requests

from time import sleep


class RequestManager:
    @staticmethod
    def add_active_request():
        server_url = os.getenv('SERVER_URL')

        data = {
            'server_url': server_url,
            'operation': 'ADD'
        }

        request = requests.post('http://' + os.getenv('STATUS_SERVER_URL') + '/api/status/', json=data)


    @staticmethod
    def remove_active_request():
        server_url = os.getenv('SERVER_URL')

        data = {
            'server_url': server_url,
            'operation': 'REMOVE'
        }

        request = requests.post('http://' + os.getenv('STATUS_SERVER_URL') + '/api/status/', json=data)


def request_manager(function):
    def wrapper(*args, **kwargs):
        RequestManager.add_active_request()
        result = function(*args, **kwargs)
        RequestManager.remove_active_request()
        return result
    return wrapper


class LongResponseView(APIView):

    @request_manager
    def post(self, request):
        sleep(20)
        return Response({'response': 'long'})

class ShortResponseView(APIView):

    @request_manager
    def post(self, request):
        sleep(5)
        return Response({'response': 'short'})
