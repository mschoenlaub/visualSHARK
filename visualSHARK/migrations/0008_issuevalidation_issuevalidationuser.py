# Generated by Django 2.1.7 on 2019-04-25 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visualSHARK', '0007_auto_20171204_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssueValidation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=255)),
                ('issue_system_id', models.CharField(max_length=255)),
                ('issue_id', models.CharField(max_length=255)),
                ('issue_type', models.TextField()),
                ('issue_type_unified', models.TextField()),
                ('linked', models.BooleanField()),
                ('resolution', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='IssueValidationUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField()),
                ('issue_validation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualSHARK.IssueValidation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
