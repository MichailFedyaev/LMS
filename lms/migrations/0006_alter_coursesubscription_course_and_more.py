# Generated by Django 5.1.4 on 2025-01-31 12:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0005_course_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesubscription',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_subscription', to='lms.course', verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='coursesubscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_course_subscription', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
