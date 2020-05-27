from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, response
from challenge_app.api.serializers import ChallengeOwnerSerializer,ChallengeSerializer,TestCaseSerializer
from challenge_app.forms import ChallengeForm,TestCaseForm
from challenge_app.models import Challenge,ChallengeOwner,TestCase
import json
from auth_app.models import User
# from django.contrib.auth.models import User
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
        # check for permission
        if User.objects.all().get(id=request.user.id).is_teacher :
            serializer = ChallengeSerializer()
            return Response({'serializer': serializer})
        
        else:
            return JsonResponse({'message': 'This is Forbidden'}, status=403)

    def post(self, request):
        # check for permission
        if User.objects.all().get(id=request.user.id).is_teacher is False :
            return JsonResponse({'message': 'This is Forbidden'}, status=403)
        
        data=request.data
        # making dictionary mutable to do some changes
        data._mutable = True
        # pop csrfmiddlewaretoken because serializer only need required data to store
        data.pop('csrfmiddlewaretoken')
        # create a serializer and check if it is valid or not
        # if serializer is valid then save it
        # also have to add related details in ChallengeOwner model
        # so now made another serializer for ChallengeOwner and then did same process to save it
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


    # This mathod is for listing all Challenges own by user
    # make a list of challenge object own by logged in user
    # then make serializer for lists of objects
    def list(self, request):
        challenge_owner = ChallengeOwner.objects.all()
        queryset =[]
        for owner in challenge_owner:
            queryset.append(owner.challenge_id)
        serializer = ChallengeSerializer(queryset, many=True)
        return Response({'serializer':serializer.data})
        


class ChallengeEdit(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'challenge_app/edit-challenge.html'
    
    # geting Challenge object which user want to change
    # made a serializer for Challenge object and send it to page
    def get(self,request, challenge_id):
        # check for permission
        if User.objects.all().get(id=request.user.id).is_teacher is False :
            return JsonResponse({'message': 'This is Forbidden'}, status=403)
        # check if it is owner's chellenge or not
        # if it is then it wil process further
        # else, it will give Request Forbidden Error
        if ChallengeOwner.objects().all().get(challenge_id=challenge_id).owner is not request.user:
            return JsonResponse({'message': 'This is Forbidden'}, status=403)
        
        obj=Challenge.objects.all().get(challenge_id=challenge_id)
        serializer=ChallengeSerializer(obj)
        return Response({'serializer':serializer})

    # updating a Challenge object
    def post(self,request, challenge_id):
        # check for permission
        if User.objects.all().get(id=request.user.id).is_teacher is False :
            return JsonResponse({'message': 'This is Forbidden'}, status=403)

        data=request.data
        data._mutable = True
        data.pop('csrfmiddlewaretoken')
        obj=Challenge.objects.all().get(challenge_id=challenge_id)
        obj = ChallengeSerializer().update(obj,validated_data=data)
        serializer=ChallengeSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

