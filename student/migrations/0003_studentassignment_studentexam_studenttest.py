# Generated by Django 3.2.13 on 2022-09-04 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0005_exam_question_studentannouncement_teacherannouncement_testquestion_testquizes'),
        ('student', '0002_registrationdeadline_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
                ('pass_mark', models.IntegerField(blank=True, null=True)),
                ('done', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('question_1', models.CharField(blank=True, max_length=50, null=True)),
                ('question_1_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_2', models.CharField(blank=True, max_length=50, null=True)),
                ('question_2_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_3', models.CharField(blank=True, max_length=50, null=True)),
                ('question_3_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_4', models.CharField(blank=True, max_length=50, null=True)),
                ('question_4_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_5', models.CharField(blank=True, max_length=50, null=True)),
                ('question_5_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_6', models.CharField(blank=True, max_length=50, null=True)),
                ('question_6_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_7', models.CharField(blank=True, max_length=50, null=True)),
                ('question_7_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_8', models.CharField(blank=True, max_length=50, null=True)),
                ('question_8_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_9', models.CharField(blank=True, max_length=50, null=True)),
                ('question_9_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_10', models.CharField(blank=True, max_length=50, null=True)),
                ('question_10_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.testandquiz')),
            ],
        ),
        migrations.CreateModel(
            name='StudentExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('question_1', models.CharField(blank=True, max_length=50, null=True)),
                ('question_1_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_2', models.CharField(blank=True, max_length=50, null=True)),
                ('question_2_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_3', models.CharField(blank=True, max_length=50, null=True)),
                ('question_3_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_4', models.CharField(blank=True, max_length=50, null=True)),
                ('question_4_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_5', models.CharField(blank=True, max_length=50, null=True)),
                ('question_5_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_6', models.CharField(blank=True, max_length=50, null=True)),
                ('question_6_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_7', models.CharField(blank=True, max_length=50, null=True)),
                ('question_7_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_8', models.CharField(blank=True, max_length=50, null=True)),
                ('question_8_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_9', models.CharField(blank=True, max_length=50, null=True)),
                ('question_9_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_10', models.CharField(blank=True, max_length=50, null=True)),
                ('question_10_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_11', models.CharField(blank=True, max_length=50, null=True)),
                ('question_11_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_12', models.CharField(blank=True, max_length=50, null=True)),
                ('question_12_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_13', models.CharField(blank=True, max_length=50, null=True)),
                ('question_13_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_14', models.CharField(blank=True, max_length=50, null=True)),
                ('question_14_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_15', models.CharField(blank=True, max_length=50, null=True)),
                ('question_15_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_16', models.CharField(blank=True, max_length=50, null=True)),
                ('question_16_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_17', models.CharField(blank=True, max_length=50, null=True)),
                ('question_17_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_18', models.CharField(blank=True, max_length=50, null=True)),
                ('question_18_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_19', models.CharField(blank=True, max_length=50, null=True)),
                ('question_19_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('question_20', models.CharField(blank=True, max_length=50, null=True)),
                ('question_20_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
                ('detail', models.TextField(blank=True, max_length=5000, null=True)),
                ('upload', models.FileField(blank=True, null=True, upload_to='assignment/')),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
