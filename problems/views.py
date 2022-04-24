from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Problems
from .serializer import ProblemsSerializer


from .models import Problems
# Create your views here.
@api_view(['GET'])
def problems_set(request):
    probs=Problems.objects.all()
    serializer = ProblemsSerializer(probs,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_problem(request):
    # probs=Problems.objects.all()
    serializer = ProblemsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)