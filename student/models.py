from distutils.command.upload import upload
from re import S
from django.db import models
from account.models import Account
from curriculum.models import Class, Subject, Assignment, TestAndQuiz, Exam


class Student(models.Model):
   username = models.CharField(max_length=50, unique=True)
   contact_no = models.CharField(max_length=20, default='2547xxxxxxx')
   parent_name = models.CharField(max_length=100)
   parent_phone_no = models.CharField(max_length=20, default='2547xxxxxxx')
   city = models.CharField(max_length=100, default='Nairobi')
   country = models.CharField(max_length=100, default='Kenya')
   profile = models.ImageField(blank=True, null=True, upload_to='profile/', default='profile/default.png')
   user = models.OneToOneField(Account, on_delete=models.CASCADE)
   about = models.TextField(max_length=500, blank=True, null=True)
   subject = models.ManyToManyField(Subject, blank=True, null=True)
   gender = models.CharField(max_length=10)
   dob = models.DateField()

   def __str__(self):
      return self.username


class Result(models.Model):
   student = models.ForeignKey(Student, on_delete=models.CASCADE)
   subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
   score = models.IntegerField()
   total = models.IntegerField(blank=True, null=True)
   grade = models.CharField(max_length=10, blank=True, null=True)
   comments = models.TextField(max_length=500, blank=True, null=True)

   def __str__(self):
      template = '{0.student.user.first_name} {0.student.user.last_name}'
      return template.format(self)


class RegistrationDeadline(models.Model):
   class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
   deadline = models.DateField()
   status = models.BooleanField(default=True)

   def __str__(self):
      return self.class_name.name


class StudentAssignment(models.Model):
   assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
   student = models.ForeignKey(Student, on_delete=models.CASCADE)
   score = models.IntegerField(blank=True, null=True)
   detail = models.TextField(max_length=5000, blank=True, null=True)
   upload = models.FileField(blank=True, null=True, upload_to='assignment/')
   comment = models.TextField(max_length=500, blank=True, null=True)
   date_submitted = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.student.username + ' ' + self.assignment.name


class StudentTest(models.Model):
   test = models.ForeignKey(TestAndQuiz, on_delete=models.CASCADE)
   student = models.ForeignKey(Student, on_delete=models.CASCADE)
   score = models.IntegerField(blank=True, null=True)
   pass_mark = models.IntegerField(blank=True, null=True)
   done = models.BooleanField(default=False)
   comment = models.TextField(max_length=500, blank=True, null=True)
   date_submitted = models.DateTimeField(auto_now_add=True)
   question_1 = models.CharField(max_length=50, blank=True, null=True)
   question_1_answer = models.TextField(max_length=500, blank=True, null=True)
   question_2 = models.CharField(max_length=50, blank=True, null=True)
   question_2_answer = models.TextField(max_length=500, blank=True, null=True)
   question_3 = models.CharField(max_length=50, blank=True, null=True)
   question_3_answer = models.TextField(max_length=500, blank=True, null=True)
   question_4 = models.CharField(max_length=50, blank=True, null=True)
   question_4_answer = models.TextField(max_length=500, blank=True, null=True)
   question_5 = models.CharField(max_length=50, blank=True, null=True)
   question_5_answer = models.TextField(max_length=500, blank=True, null=True)
   question_6 = models.CharField(max_length=50, blank=True, null=True)
   question_6_answer = models.TextField(max_length=500, blank=True, null=True)
   question_7 = models.CharField(max_length=50, blank=True, null=True)
   question_7_answer = models.TextField(max_length=500, blank=True, null=True)
   question_8 = models.CharField(max_length=50, blank=True, null=True)
   question_8_answer = models.TextField(max_length=500, blank=True, null=True)
   question_9 = models.CharField(max_length=50, blank=True, null=True)
   question_9_answer = models.TextField(max_length=500, blank=True, null=True)
   question_10 = models.CharField(max_length=50, blank=True, null=True)
   question_10_answer = models.TextField(max_length=500, blank=True, null=True)

   def __str__(self):
      return self.student.username + ' ' + self.test.name


class StudentExam(models.Model):
   exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
   student = models.ForeignKey(Student, on_delete=models.CASCADE)
   score = models.IntegerField(blank=True, null=True)
   comment = models.TextField(max_length=500, blank=True, null=True)
   date_submitted = models.DateTimeField(auto_now_add=True)
   question_1 = models.CharField(max_length=50, blank=True, null=True)
   question_1_answer = models.TextField(max_length=500, blank=True, null=True)
   question_2 = models.CharField(max_length=50, blank=True, null=True)
   question_2_answer = models.TextField(max_length=500, blank=True, null=True)
   question_3 = models.CharField(max_length=50, blank=True, null=True)
   question_3_answer = models.TextField(max_length=500, blank=True, null=True)
   question_4 = models.CharField(max_length=50, blank=True, null=True)
   question_4_answer = models.TextField(max_length=500, blank=True, null=True)
   question_5 = models.CharField(max_length=50, blank=True, null=True)
   question_5_answer = models.TextField(max_length=500, blank=True, null=True)
   question_6 = models.CharField(max_length=50, blank=True, null=True)
   question_6_answer = models.TextField(max_length=500, blank=True, null=True)
   question_7 = models.CharField(max_length=50, blank=True, null=True)
   question_7_answer = models.TextField(max_length=500, blank=True, null=True)
   question_8 = models.CharField(max_length=50, blank=True, null=True)
   question_8_answer = models.TextField(max_length=500, blank=True, null=True)
   question_9 = models.CharField(max_length=50, blank=True, null=True)
   question_9_answer = models.TextField(max_length=500, blank=True, null=True)
   question_10 = models.CharField(max_length=50, blank=True, null=True)
   question_10_answer = models.TextField(max_length=500, blank=True, null=True)
   question_11 = models.CharField(max_length=50, blank=True, null=True)
   question_11_answer = models.TextField(max_length=500, blank=True, null=True)
   question_12 = models.CharField(max_length=50, blank=True, null=True)
   question_12_answer = models.TextField(max_length=500, blank=True, null=True)
   question_13 = models.CharField(max_length=50, blank=True, null=True)
   question_13_answer = models.TextField(max_length=500, blank=True, null=True)
   question_14 = models.CharField(max_length=50, blank=True, null=True)
   question_14_answer = models.TextField(max_length=500, blank=True, null=True)
   question_15 = models.CharField(max_length=50, blank=True, null=True)
   question_15_answer = models.TextField(max_length=500, blank=True, null=True)
   question_16 = models.CharField(max_length=50, blank=True, null=True)
   question_16_answer = models.TextField(max_length=500, blank=True, null=True)
   question_17 = models.CharField(max_length=50, blank=True, null=True)
   question_17_answer = models.TextField(max_length=500, blank=True, null=True)
   question_18 = models.CharField(max_length=50, blank=True, null=True)
   question_18_answer = models.TextField(max_length=500, blank=True, null=True)
   question_19 = models.CharField(max_length=50, blank=True, null=True)
   question_19_answer = models.TextField(max_length=500, blank=True, null=True)
   question_20 = models.CharField(max_length=50, blank=True, null=True)
   question_20_answer = models.TextField(max_length=500, blank=True, null=True)

   def __str__(self):
      template = '{0.student.user.first_name} {0.student.user.last_name} {0.exam.subject.name}'
      return template.format(self)
