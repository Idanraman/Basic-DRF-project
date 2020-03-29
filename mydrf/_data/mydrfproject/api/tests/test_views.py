from django.db.utils import IntegrityError
from django.core.exceptions import *
from django.contrib.auth.models import User

from rest_framework.test import APIRequestFactory, force_authenticate
from mixer.backend.django import mixer
from typing import Dict, Union, List
import pytest
import unittest

from api.views import *

pytestmark = pytest.mark.django_db

UsersDict = Dict[str,Union[None,User]]
TestCases = List[type(Dict[str,Union[None,User,int]])]

def users_factory() -> UsersDict:
	users = {}
	users['none'] = None #Create none user
	users['user'] = mixer.blend('auth.User') #Create regular user
	users['admin'] = mixer.blend('auth.User', \
		is_superuser = True, is_staff = True) #Create admin user
	return users

def permissions_testing_factory(method: str,action: str,test_cases: TestCases) -> None:
	for case in test_cases:
		factory = APIRequestFactory()
		view = BreedViewSet.as_view({method: action})
		request = factory.get('/{self.endpoint}/')
		if not case['user'] == None:
			force_authenticate(request, user=case['user'])
		response = view(request)
		assert response.status_code == case['response_code'] , \
			"%s user should recieve %d" % \
				(str(case['user']),case['response_code'])


class TestBreed(unittest.TestCase):

	def setUp(self) -> None:
		self.breed = mixer.blend("api.AnimalBreed")
		self.endpoint = 'breeds'
		self.users = users_factory()

	def test_breed_list_permissions(self) ->None:
		method = 'get'
		action = 'list'
		test_cases = [
			{'user':self.users['none'],'response_code':403},
			{'user':self.users['user'],'response_code':403},
			{'user':self.users['admin'],'response_code':200}
		]
		permissions_testing_factory(method,action,test_cases)