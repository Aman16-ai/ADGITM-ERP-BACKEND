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
from rest_framework.decorators import action

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

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if('status' in request.data):
            issue_status = request.data['status']
            print(f"user {request.user.role}")
            print(f"instance {instance.status} update status {issue_status}")
            if (issue_status == 'Verified' and request.user.role != 'MM' and instance.status == 'Completed') or (issue_status == 'Unverified' and request.user.role != 'MM' and instance.status == 'Verified'):
                #Here we can update the status to verified
                if(issue_status == 'Unverified'):
                    request.data['status'] = 'Completed'
                serializer = self.get_serializer(instance,data=request.data,partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer=serializer)
                return Response(serializer.data)
            elif issue_status in ['Verified','Unverified'] and request.user.role == 'MM':
                return Response({'Message':"You don't have permission to verify the issue"},status=status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)
            elif issue_status == 'Verified' and instance.status in ['Completed','Pending','Rejected','Progress']:
                return Response({'Message':'Only completed issues can verified'},status=status.HTTP_403_FORBIDDEN)
            elif issue_status == 'Unverified' and instance.status in ['Completed','Pending','Rejected','Progress']:
                return Response({'Message':'Only verified issues can unverified'},status=status.HTTP_403_FORBIDDEN)
            


        return super().partial_update(request, *args, **kwargs)
    
    def get_queryset(self):
        if('start_date' in self.request.GET and 'end_date' in self.request.GET):
            start_date = self.request.GET['start_date']
            end_date = self.request.GET['end_date']
            print(f'start date : {start_date} end_dat : {end_date}')
            if start_date and end_date:
                start_date = parse_date(start_date)
                end_date = parse_date(end_date)
                data = MaintenanceIssue.objects.filter(Q(created_at__gte=start_date) & Q(created_at__lte=end_date))
                print(data)
                return data
        print(self.request.GET)
        return super().get_queryset()
    def get_serializer_class(self):
        if self.action == 'list':
            return self.serializers['list']
        return self.serializers['create']
    def finalize_response(self, request, response, *args, **kwargs):
        final_response = Response({"status":response.status_code,"Response":response.data},status=response.status_code)
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
    