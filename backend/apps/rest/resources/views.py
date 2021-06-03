import logstash
from rest_framework import views
from rest_framework.response import Response

import logging

logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.TCPLogstashHandler("localhost", 5000, version=1))

class RestAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        logger.error("saaa")
        return Response('get method')

    def post(self, request, *args, **kwargs):
        return Response('post method')

    def put(self, request, *args, **kwargs):
        return Response('put method')

    def delete(self, request, *args, **kwargs):
        return Response('delete method')
