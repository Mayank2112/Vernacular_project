from rest_framework.views import APIView
from .apifunc import validate_finite_values_entity, validate_numeric_entity
from rest_framework.response import Response
import json

class Api(APIView):
    def post(self, request):
        result = validate_finite_values_entity(request.data['values'], request.data['supported_values'], request.data['invalid_trigger'], request.data['key'], request.data['support_multiple'], request.data['pick_first'])
        return Response(json.dumps(result))
class Api1(APIView):
    def post(self, request):
        result = validate_numeric_entity(request.data['values'], request.data['invalid_trigger'], request.data['pick_first'])
        return Response(json.dumps(result))
