from django.db import models

EATING_TYPES = [
	('ALL', 'All'),
	('Plants', 'Plants'),
	('Meat', 'Meat'),
]

GENDER_TYPES = [
	('M','Male'),
	('F','Female')
]

class AnimalBreed(models.Model):
	name = models.CharField(max_length=30)
	voice = models.CharField(max_length=30)
	eating_type = models.CharField(max_length=30, 
		choices=EATING_TYPES)
	can_it_fly = models.BooleanField(default=False)
	can_it_swim = models.BooleanField(default=False)

	class Meta:
		constraints = [
			models.CheckConstraint(
				check=models.Q(
					eating_type__in=[EATING_TYPES[i][0] for i in range(len(EATING_TYPES))]),
					name="eating_type_valid",
			)
		]

class Animal(models.Model):
	name = models.CharField(max_length=30)
	gender = models.CharField(max_length=30, choices=GENDER_TYPES)
	breed = models.ForeignKey(
		'AnimalBreed',
		on_delete=models.CASCADE,
	)
	father = models.ForeignKey('self',on_delete=models.CASCADE)
	mother = models.ForeignKey('self',on_delete=models.CASCADE, related_name='%(class)s_requests_created')

