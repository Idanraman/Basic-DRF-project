# Generated by Django 3.0.4 on 2020-03-27 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalBreed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('voice', models.CharField(max_length=30)),
                ('eating_type', models.CharField(choices=[('ALL', 'All'), ('Plants', 'Plants'), ('Meat', 'Meat')], max_length=30)),
                ('can_it_fly', models.BooleanField(default=False)),
                ('can_it_swim', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=30)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AnimalBreed')),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Animal')),
                ('mother', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_requests_created', to='api.Animal')),
            ],
        ),
    ]
