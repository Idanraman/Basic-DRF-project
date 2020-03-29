import pytest
import unittest
from mixer.backend.django import mixer
from api.models import AnimalBreed, Animal
from django.db.utils import IntegrityError
from django.core.exceptions import *

pytestmark = pytest.mark.django_db


class TestBreed(unittest.TestCase):

	def setUp(self):
		self.model = 'api.AnimalBreed'

	def test_breed_creation(self):
		obj = mixer.blend(self.model)
		assert obj.pk == 1, 'wrong primary key'

	def test_breed_bad_inputs_to_model(self):
		with self.assertRaises(IntegrityError): 
			obj = mixer.blend(self.model,name=None)

	def test_breed_no_voice_error(self):
		with self.assertRaises(IntegrityError): 
			obj = mixer.blend(self.model, voice=None)

	def test_breed_bad_eating_type_error(self):
		with self.assertRaises(IntegrityError): 
			obj = mixer.blend(self.model, eating_type='BlaBla')

	def test_breed_no_swimming_flying_data_error(self):
		with self.assertRaises(ValidationError):
			obj = mixer.blend(self.model, can_it_swim=None)
		#self.assertRaises(IntegrityError, lambda: obj.save())

	#def test_no_voice_error(self):
	#	obj = mixer.blend(self.model)
	#	obj.voice = None
	#	assert IntegrityError

# class TestAnimal(unittest.TestCase):

# 	def setUp(self):
# 		self.model = 'api.Animal'

# 	def test_animal_model(self):
# 		obj = mixer.blend(self.model)
# 		assert obj.pk == 1, 'wrong primary key'

# 	def test_animal_bad_inputs_to_model(self):
# 		with self.assertRaises(IntegrityError): 
# 			obj = mixer.blend(self.model,name=None)

# 	def test_animal_no_voice_error(self):
# 		with self.assertRaises(IntegrityError): 
# 			obj = mixer.blend(self.model, voice=None)

# 	def test_animal_bad_eating_type_error(self):
# 		with self.assertRaises(IntegrityError): 
# 			obj = mixer.blend(self.model, eating_type='BlaBla')

# 	def test_animal_no_swimming_flying_data_error(self):
# 		with self.assertRaises(ValidationError):
# 			obj = mixer.blend(self.model, can_it_swim=None)