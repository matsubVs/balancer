from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ServerStatus


class StatusResponseView(APIView):

    def get(self, request):
        server_url = request.GET.get('server_url')
        if not server_url:
            return Response({'error': 'invalid get data'})

        server_row = ServerStatus.objects.filter(server_name=server_url).first()
        if server_row:
            return Response({'active_requests': server_row.active_requests, "server_url": server_url})
        else:
            server_row = ServerStatus.objects.create(server_name=server_url, active_requests=0)
            server_row.save()

            return Response({'active_requests': server_row.active_requests})


    def post(self, request):
        data = request.data

        try:
            server_url = data['server_url']
            operation = data['operation']
        except Exception as e:
            return Response({'error': 'invalid post data'})

        server_row = ServerStatus.objects.filter(server_name=server_url).first()
        if server_row and operation == 'ADD':
            server_row.active_requests += 1
            server_row.save()

            return Response({'active_requests': server_row.active_requests})

        elif server_row and operation == 'REMOVE':
            server_row.active_requests -= 1
            server_row.save()

            return Response({'active_requests': server_row.active_requests})

        else:
            server_row = ServerStatus.objects.create(server_name=server_url, active_requests=1)
            server_row.save()

            return Response({'active_requests': server_row.active_requests})
