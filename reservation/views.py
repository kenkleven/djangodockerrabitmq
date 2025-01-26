from rest_framework import viewsets
from rest_framework.response import Response
from .producer import send_message
from .consumer import main
import sys



class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        message = ' '.join(sys.argv[1:]) or "Hello World!"
        send_message(message)
        return Response()

    def liste(self, request):
        main()
        return Response()  