import requests as req
from django.conf import settings
from typing import List
import os


def status_checker() -> List:
	available_hosts = settings.AVAILABLE_HOSTS
	results = []
	status_checker_host = os.getenv('STATUS_SERVER_URL')

	for host in available_hosts:
		resp = req.get(status_checker_host + '/api/status/', params={'server_url': host})
		result = resp.json()
		print(host, result, 'status checker')

		results.append([host, result['active_requests']])

	return results
