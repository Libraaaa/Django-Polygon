# Generated by Django 5.0.3 on 2024-03-31 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_markdowncontent_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('mime_type', models.CharField(max_length=100)),
                ('md5_hash', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
