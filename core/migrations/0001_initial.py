# Generated by Django 2.2.4 on 2019-11-21 10:44

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_do_pacote', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('version', models.IntegerField()),
                ('authors', models.CharField(max_length=50)),
                ('owners', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=50)),
                ('project_URL', models.CharField(max_length=50)),
                ('icon_URL', models.URLField()),
                ('description', models.TextField()),
                ('require_license_acceptance', models.BooleanField()),
                ('dependencia', models.CharField(max_length=50)),
                ('installer_type', models.CharField(max_length=3)),
                ('unattended_arguments', models.CharField(max_length=50)),
                ('URL', models.CharField(max_length=50)),
                ('URL_64', models.CharField(max_length=50)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
