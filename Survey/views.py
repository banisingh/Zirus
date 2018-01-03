from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Survey.models import Survey
from Survey.serializers import SurveySerializer

# Create your views here.


def survey(request):
    return render(request, 'survey.html')

@api_view(['POST'])
def survey_results(request):
    serializer = SurveySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
