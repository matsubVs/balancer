import requests as req
from .status_checker import status_checker

from rest_framework.response import Response
from rest_framework.decorators import api_view


def get_available_host() -> str:
	pool = status_checker()
	sorted_pool = sorted(pool, key=lambda x: x[1])
	print(sorted_pool)

	return sorted_pool[0][0]


@api_view(['POST',])
def long_request(request):
	print("POST")
	host = get_available_host()

	hostname = 'http://' + host + '/api/long/'
	print('selected hostname', hostname, 'long')

	request_ = req.post(hostname)
	response = request_.json()

	return Response(response)


@api_view(['POST',])
def short_request(request):
	print("GET")

	host = get_available_host()
	hostname = 'http://' + host + '/api/short/'
	print('selected hostname', hostname, 'short')

	request_ = req.post(hostname)
	response = request_.json()
	print(response)

	return Response(response)
