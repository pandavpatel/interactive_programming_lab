from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, response
from challenge_app.api.serializers import ChallengeOwnerSerializer,ChallengeSerializer,TestCaseSerializer
from challenge_app.forms import ChallengeForm,TestCaseForm
from challenge_app.models import Challenge,ChallengeOwner,TestCase
import json
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.urls import reverse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView 
from rest_framework import status,generics,mixins

# Create your views here.

class ChallengeDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'challenge_app/add-challenge.html'

    def get(self, request):
        serializer = ChallengeSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        data=request.data
        data._mutable = True
        data.pop('csrfmiddlewaretoken')
        serializer = ChallengeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            id=serializer.data['challenge_id']
            owner_data={'challenge_id':id, 'owner':request.user.id}
            owner_serializer = ChallengeOwnerSerializer(data=owner_data)
            if owner_serializer.is_valid():
                owner_serializer.save()
            else :
                return JsonResponse(owner_serializer._errors)
            return JsonResponse(owner_serializer.data)
        else:
            return JsonResponse(serializer._errors)



class ChallengeList(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'challenge_app/list-challenge.html'

    def list(self, request):
        challenge_owner = ChallengeOwner.objects.all().filter(owner=request.user.id)
        queryset =[]
        for owner in challenge_owner:
            queryset.append(owner.challenge_id)
        serializer = ChallengeSerializer(queryset, many=True)
        return Response({'serializer':serializer.data})
        


class ChallengeEdit(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'challenge_app/edit-challenge.html'
    
    def get(self,request, challenge_id):
        obj=Challenge.objects.all().get(challenge_id=challenge_id)
        serializer=ChallengeSerializer(obj)
        return Response({'serializer':serializer})

    def post(self,request, challenge_id):
        data=request.data
        data._mutable = True
        data.pop('csrfmiddlewaretoken')
        obj=Challenge.objects.all().get(challenge_id=challenge_id)
        obj = ChallengeSerializer().update(obj,validated_data=data)
        serializer=ChallengeSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

