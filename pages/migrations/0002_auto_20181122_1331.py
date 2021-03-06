# Generated by Django 2.1.3 on 2018-11-22 04:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='course_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.CourseName'),
        ),
        migrations.AddField(
            model_name='review',
            name='professor_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Professor'),
        ),
    ]
