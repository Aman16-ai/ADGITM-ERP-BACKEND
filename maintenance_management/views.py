from django.shortcuts import render
from rest_framework import viewsets,views
from rest_framework.response import Response
from .models import MaintenanceIssue,MaintenanceType, MaintenanceIssueComment
from .serializer import MaintenanceIssueSerializer, MaintenanceIssueStatusAndCountSerializer,GetMaintenanceIssueSerializer, MaintenanceTypeModelSerializer, MaintenaceIssueCommentSerializer,GetMaintenaceIssueCommentSerializer
from middleware.custom_premission import MaintenanceManagementPermission
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from django.utils.dateparse import parse_date
from rest_framework import status
from django.db.models import Q
from django_filters import rest_framework as filter
# Create your views here.

class MaintenanceIssueViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceIssue.objects.all()
    # serializer_class = MaintenanceIssueSerializer
    permission_classes = [MaintenanceManagementPermission]

    serializers = {
        'list':    GetMaintenanceIssueSerializer,
        'create': MaintenanceIssueSerializer
        # etc.
    }
    def get_serializer_class(self):
        if self.action == 'list':
            return self.serializers['list']
        return self.serializers['create']
    def finalize_response(self, request, response, *args, **kwargs):
        final_response = Response({"status":response.status_code,"Response":response.data})
        final_response.accepted_renderer = request.accepted_renderer
        final_response.accepted_media_type = request.accepted_media_type
        final_response.renderer_context = self.get_renderer_context()
        return final_response
    
    def get_renderer_context(self):
        """
        Returns a dict that is passed through to Renderer.render(),
        as the `renderer_context` keyword argument.
        """
        # Note: Additionally 'response' will also be added to the context,
        #       by the Response object.
        return {
            'view': self,
            'args': getattr(self, 'args', ()),
            'kwargs': getattr(self, 'kwargs', {}),
            'request': getattr(self, 'request', None)
        }

class MaintenanceIssueStatusAndCountView(views.APIView):
    # permission_classes = [IsAuthenticated]

    def get(self,request):
        try:
            start_date = self.request.query_params.get('start_date')
            end_date = self.request.query_params.get('end_date')
            print(f'start date : {start_date} end_dat : {end_date}')
            statusAndCounts = []
            if start_date and end_date:
                start_date = parse_date(start_date)
                end_date = parse_date(end_date)
                statusAndCounts = MaintenanceIssue.objects.filter(Q(created_at__gte=start_date) & Q(created_at__lte=end_date)).values('status').annotate(count=Count('status'))
            else:
                statusAndCounts = MaintenanceIssue.objects.all().values('status').annotate(count=Count('status'))
            data = MaintenanceIssueStatusAndCountSerializer(statusAndCounts,many=True)
            return Response({'status':'success','Response':data.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status':'Failed',
                'Error' : e
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR,)
        
class MaintenanceTypeViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceType.objects.all()
    serializer_class = MaintenanceTypeModelSerializer
    def finalize_response(self, request, response, *args, **kwargs):
        final_response = Response({"status":response.status_code,"Response":response.data})
        final_response.accepted_renderer = request.accepted_renderer
        final_response.accepted_media_type = request.accepted_media_type
        final_response.renderer_context = self.get_renderer_context()
        return final_response
    
    def get_renderer_context(self):
        """
        Returns a dict that is passed through to Renderer.render(),
        as the `renderer_context` keyword argument.
        """
        # Note: Additionally 'response' will also be added to the context,
        #       by the Response object.
        return {
            'view': self,
            'args': getattr(self, 'args', ()),
            'kwargs': getattr(self, 'kwargs', {}),
            'request': getattr(self, 'request', None)
        }
    

class MaintenanceIssueCommentViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceIssueComment.objects.all()
    # serializer_class = MaintenaceIssueCommentSerializer
    permission_classes = [MaintenanceManagementPermission]
    filter_backends = (filter.DjangoFilterBackend,)
    filterset_fields = {
        'maintenanceIssue':['exact'],
    }

    serializers = {
        'list':    GetMaintenaceIssueCommentSerializer,
        'create': MaintenaceIssueCommentSerializer
        # etc.
    }
    def get_serializer_class(self):
        if self.action == 'list':
            return self.serializers['list']
        return self.serializers['create']
    def finalize_response(self, request, response, *args, **kwargs):
        final_response = Response({"status":response.status_code,"Response":response.data})
        final_response.accepted_renderer = request.accepted_renderer
        final_response.accepted_media_type = request.accepted_media_type
        final_response.renderer_context = self.get_renderer_context()
        return final_response
    
    def get_renderer_context(self):
        """
        Returns a dict that is passed through to Renderer.render(),
        as the `renderer_context` keyword argument.
        """
        # Note: Additionally 'response' will also be added to the context,
        #       by the Response object.
        return {
            'view': self,
            'args': getattr(self, 'args', ()),
            'kwargs': getattr(self, 'kwargs', {}),
            'request': getattr(self, 'request', None)
        }
    