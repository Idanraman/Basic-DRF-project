# Generated by Django 3.0.4 on 2020-03-27 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200327_1916'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='animalbreed',
            name='eating_type_valid',
        ),
        migrations.AddConstraint(
            model_name='animalbreed',
            constraint=models.CheckConstraint(check=models.Q(eating_type__in=['All', 'Plants', 'Meat']), name='eating_type_valid'),
        ),
    ]
