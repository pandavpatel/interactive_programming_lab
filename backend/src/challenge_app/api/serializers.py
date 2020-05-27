from rest_framework import serializers
from ..models import Challenge,ChallengeOwner,TestCase


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'

    def create(self, validated_data):
        return Challenge.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance



class ChallengeOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeOwner
        fields = '__all__'


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = '__all__'
    def create(self, validated_data):
        return TestCase.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.input = validated_data.get('input', instance.input)
        instance.output = validated_data.get('output', instance.output)
        instance.marks = validated_data.get('marks', instance.marks)
        instance.is_hidden = validated_data.get('is_hidden', instance.is_hidden)
        instance.exexution_time_limit = validated_data.get('exexution_time_limit', instance.exexution_time_limit)
        instance.save()
        return instance