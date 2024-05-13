# Generated by Django 5.0.4 on 2024-05-13 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated time')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.basemodel')),
                ('name', models.CharField(max_length=50, verbose_name='Country name')),
                ('code', models.CharField(max_length=10, verbose_name='Country code')),
            ],
            bases=('common.basemodel',),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.basemodel')),
                ('file', models.FileField(upload_to='files/', verbose_name='File')),
                ('type', models.CharField(choices=[('image', 'Image'), ('file', 'File'), ('music', 'Music'), ('video', 'Video')], max_length=10, verbose_name='File type')),
            ],
            bases=('common.basemodel',),
        ),
        migrations.CreateModel(
            name='CustomerFeedback',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.basemodel')),
                ('description', models.TextField(verbose_name='Description')),
                ('rank', models.IntegerField(verbose_name='Rank')),
                ('customer_name', models.CharField(max_length=60, verbose_name='Customer name')),
                ('customer_position', models.CharField(max_length=60, verbose_name='Customer position')),
                ('customer_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_images', to='common.media')),
            ],
            bases=('common.basemodel',),
        ),
        migrations.CreateModel(
            name='OurInstagramStory',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.basemodel')),
                ('story_link', models.URLField(verbose_name='Story link')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instagram_stories', to='common.media')),
            ],
            bases=('common.basemodel',),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.basemodel')),
                ('name', models.CharField(max_length=50, verbose_name='Region name')),
                ('zip_code', models.CharField(max_length=20, verbose_name='Zip code')),
                ('country_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='common.country')),
            ],
            bases=('common.basemodel',),
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.basemodel')),
                ('home_title', models.CharField(max_length=120, verbose_name='Title')),
                ('home_subtitle', models.CharField(max_length=120, verbose_name='Subtitle')),
                ('home_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media')),
            ],
            bases=('common.basemodel',),
        ),
    ]
