
from django.http import HttpResponse
from .models import Ticket
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
import logging,logging.handlers
from .serializers import TicketSerializer,UserSerializer,GroupSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.models import User, Group




# def index(request):
#     print " Hello I am to watch"
#     latest_question_list = ExampleModel.objects.all()
#     context = {'latest_question_list':latest_question_list}
#     return render(request, 'index.html',context)


# def post_collections(request):
#     if request.method == 'GET':
#         print "##################get request raised from browser"
#         posts = ExampleModel.objects.all()
#         print "What is the call here ",posts
#         serializer = PostSerializer(posts, many=True)
#         print "Serializer Method calling",serializer
#         print Response(serializer.data)
#         return HttpResponse(str(list(ExampleModel.objects.all())))
#     else:
#         print "Unknown reuqtest################"
#         return Response("hello")


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def all_tickets_collection(request):
    print "This called to access the data , watch out for strange data!!!!!!!!!!"
    if request.method == 'GET':
        print "This called to access the data , watch out for strange data!!!!!!!!!!"
        tickets = Ticket.objects.all()
        print tickets
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        ticket = Ticket()
        serializer = TicketSerializer(data=request.data)
        print "System Returned the proper values for analysis : ",serializer
        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data['status']:
                ticket.status = serializer.validated_data['status']
            if serializer.validated_data['priority']:
                ticket.priority = serializer.validated_data['priority']
            ticket.subject = serializer.validated_data['subject']
            ticket.content = serializer.validated_data['content']

            ticket.save()
            return Response(
                {'status': 'Ticket created.'},
                status=status.HTTP_201_CREATED
            )


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
