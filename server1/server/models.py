from django.db import models


class ServerStatus(models.Model):
	id = models.AutoField(primary_key=True)
	server_name = models.CharField(max_length=20)
	active_requests = models.IntegerField()

	def __str__(self):
		return self.server_name