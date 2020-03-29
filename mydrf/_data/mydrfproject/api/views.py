from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpRequest
from django.http import HttpResponse, JsonResponse
from django_filters import rest_framework as drf_filters #DjangoFilterBackend

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import *
from api.models import *

class BreedPermissions(permissions.BasePermission):

	@staticmethod
	def get_role(request : HttpRequest) -> str:
		if request.user.is_staff and request.user.is_superuser:
			return('admin')
		elif request.user.is_authenticated:
			return('user')
		elif 0: #Complete "Owner" representation
			return('owner')
		return(None)

	@staticmethod
	def basic_permissions(user: str,view : ModelViewSet) -> bool:

		permissions_dict = {
			'list':['admin'],
			'create':['user'],
			'retrieve':['admin','user',None],
			'less':['admin','user',None],
			'update':['user'],
			'partial_update':['user'],
			'destroy':['admin'],
		}
		if view.action in permissions_dict:
			if user in permissions_dict[view.action]:
				return True
		return False

	@staticmethod
	def permissions_exceptions(user: str,view : ModelViewSet) -> bool:
		is_allowed = True
		return is_allowed

	def has_permission(self,request : HttpRequest ,view : ModelViewSet) ->bool:
		user = self.get_role(request)
		is_allowed = self.basic_permissions(user,view) and \
			self.permissions_exceptions(user,view)
		#return True
		return is_allowed


class DefaultPagination(PageNumberPagination):
	page_size = 40
	page_size_query_param = 'page_size'
	max_page_size = 40


class BreedFilter(drf_filters.FilterSet):
    min_id = drf_filters.NumberFilter(field_name="id", lookup_expr='gte')
    max_id = drf_filters.NumberFilter(field_name="id", lookup_expr='lte')

    class Meta:
        model = AnimalBreed
        fields = ['name', 'id', 'eating_type']


class BreedViewSet(viewsets.ModelViewSet):
	permission_classes = [BreedPermissions]

	#Filtering
	filter_backends = [drf_filters.DjangoFilterBackend,filters.OrderingFilter]
	filterset_class = BreedFilter

	#Ordering
	ordering_fields = ['name', 'eating_type']
	ordering = ['id']

	queryset = AnimalBreed.objects.all()

	serializer_class = BreedSerializer
	pagination_class = DefaultPagination

	@action(detail=True, methods=['get'])
	def less(self, request : HttpRequest, pk : int) -> Response:
		"""GET LESS DATA REGARDING THE INSTANCE"""
		breed = self.get_object()
		serializer = BreedLessSerializer(self.queryset.get(pk=pk))
		return Response(serializer.data)
