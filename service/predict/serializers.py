from rest_framework import serializers
# from .models import ExampleModel
from .objects import  TicketObject
from .models import Ticket

from django.contrib.auth.models import User,Group



# class PostSerializer(serializers.ModelSerializer):
#     queryset=ExampleModel.objects.all()
#
#     class Meta:
#         model = ExampleModel
#         fields = ('sample_id', 'created_at', 'description', 'sample_type')


class TicketSerializer(serializers.Serializer):
    print "##########################Ticket serializer##############"
    ticket_id = serializers.CharField(required=False, read_only=True)
    status = serializers.IntegerField(required=False)
    priority = serializers.IntegerField(required=False)
    subject = serializers.CharField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField(required=False, read_only=True)

    # def restore_object(self, attrs, instance=None):
    #     print "##########Looking into the restore objects"
    #     if instance is not None:
    #         instance.status = attrs.get('status', instance.status)
    #         instance.priority = attrs.get('priority', instance.priority)
    #         instance.subject = attrs.get('subject', instance.subject)
    #         instance.content = attrs.get('content', instance.content)
    #         return instance
    #     return TicketObject(**attrs)

    def create(self, validated_data):
        print " Trigger to create the instance of the object"
        return Ticket.objects.create(**validated_data)

    def update(self, instance, validated_data):
            instance.status = validated_data.get('status', instance.status)
            instance.priority = validated_data.get('priority', instance.priority)
            instance.subject = validated_data.get('subject', instance.subject)
            instance.content = validated_data.get('content', instance.content)
            instance.save()
            return instance

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')