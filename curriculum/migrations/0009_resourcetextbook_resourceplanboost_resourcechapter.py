# Generated by Django 4.1.1 on 2022-09-23 18:38

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('curriculum', '0008_alter_resource_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceTextbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='resources/')),
                ('link', models.URLField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_edited', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('free', models.BooleanField(default=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='ResourcePlanBoost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='resources/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_edited', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('term', models.CharField(choices=[('Term 1', 'Term 1'), ('Term 2', 'Term 2'), ('Term 3', 'Term 3')], max_length=200)),
                ('term_exam', models.CharField(choices=[('Mid Term', 'Mid Term'), ('End Term', 'End Term'), ('Holiday', 'Holiday')], max_length=200)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceChapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=100)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_edited', models.DateTimeField(auto_now=True)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.resource')),
            ],
        ),
    ]
