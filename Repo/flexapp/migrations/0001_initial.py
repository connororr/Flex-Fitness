# Generated by Django 2.2.6 on 2019-10-31 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('isModifiable', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(max_length=50, null=True)),
                ('birthday', models.DateField(null=True)),
                ('height', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('bench', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('squat', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('deadlift', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('flexScore', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flexapp.Exercise')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LogEntries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('reps', models.PositiveSmallIntegerField(null=True)),
                ('userExercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flexapp.UserExercise')),
            ],
        ),
    ]
