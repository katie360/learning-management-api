from django.db import models
from teacher.models import Teacher
from manager.models import Manager
from account.models import Account
from ckeditor_uploader.fields import RichTextUploadingField


DAYS = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)

RESOURCE_TYPES = (
    ('Learning Skills', 'Learning Skills'),
    ('Learning Plan Boosts', 'Learning Plan Boosts'),
    ('Recommendable TextBooks', 'Recommendable TextBooks'),
)

TERM = (
    ('Term 1', 'Term 1'),
    ('Term 2', 'Term 2'),
    ('Term 3', 'Term 3'),
)

TERM_EXAM = (
    ('Mid Term', 'Mid Term'),
    ('End Term', 'End Term'),
    ('Holiday', 'Holiday'),
)
   
class Curriculum(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField(max_length=500)
   status = models.BooleanField(default=True)
   
   def __str__(self):
      return self.name
   

class Class(models.Model):
   name = models.CharField(max_length=100)
   curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
   code = models.CharField(max_length=10, unique=True)
   plural = 'Classes'

   def __str__(self):
      return self.name
   
class Subject(models.Model):
   name = models.CharField(max_length=100)
   subject_class = models.ForeignKey(Class,on_delete=models.CASCADE)
   code = models.CharField(max_length=10,unique=True)
   
   def __str__(self):
      return self.name
   
   
class Resource(models.Model):
   name = models.CharField(max_length=100)
   date_created = models.DateTimeField(auto_now_add=True)
   date_edited = models.DateTimeField(auto_now=True)
   subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject')
   teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
   status = models.BooleanField(default=True)

   def __str__(self):
      return self.name

   @property
   def get_subject(self):
      return self.subject.name


class ResourceChapter(models.Model):
   resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
   chapter = models.CharField(max_length=100)
   content = RichTextUploadingField()
   date_created = models.DateTimeField(auto_now_add=True)
   date_edited = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.chapter

   @property
   def get_resource(self):
      return self.resource.name


class ResourcePlanBoost(models.Model):
   name = models.CharField(max_length=100)
   file = models.FileField(upload_to='resources/')
   date_created = models.DateTimeField(auto_now_add=True)
   date_edited = models.DateTimeField(auto_now=True)
   subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
   teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
   status = models.BooleanField(default=True)
   term = models.CharField(max_length=200, choices=TERM)
   term_exam = models.CharField(max_length=200, choices=TERM_EXAM)

   def __str__(self):
      return self.name


class ResourceTextbook(models.Model):
   name = models.CharField(max_length=100)
   file = models.FileField(upload_to='resources/', blank=True, null=True)
   link = models.URLField(blank=True, null=True)
   date_created = models.DateTimeField(auto_now_add=True)
   date_edited = models.DateTimeField(auto_now=True)
   subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
   teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
   status = models.BooleanField(default=True)
   free = models.BooleanField(default=True)

   def __str__(self):
      return self.name

   @property
   def get_subject(self):
      return self.subject.name
   
class TimeTable(models.Model):
   subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
   teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
   day = models.CharField(max_length=10,choices=DAYS)
   start_time = models.TimeField()
   end_time = models.TimeField()
   link = models.CharField(max_length=100, blank=True, null=True)   
   
   def __str__(self):
      return self.subject.name


class Assignment(models.Model):
   subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
   name = models.CharField(max_length=100)
   instructions = models.TextField(max_length=500)
   file = models.FileField(upload_to='assignments/', blank=True, null=True)
   total_score = models.IntegerField(default=30)
   date_created = models.DateTimeField(auto_now_add=True)
   date_due = models.DateTimeField()
   returned = models.BooleanField(default=False)
   status = models.BooleanField(default=True)
   teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
   
   def __str__(self):
      return self.name
      
   
class TestAndQuiz(models.Model):
   subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
   name = models.CharField(max_length=100)
   instructions = models.TextField(max_length=500)
   total_score = models.IntegerField(default=30)
   date_created = models.DateTimeField(auto_now_add=True)
   date_due = models.DateTimeField()
   returned = models.BooleanField(default=False)
   status = models.BooleanField(default=True)
   teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)                                                  
   
   def __str__(self):
      return self.name
   
class TestQuestion(models.Model):
   choices_type = (
      ('text', 'Text'),
      ('image', 'Image'),
   )
   test = models.ForeignKey(TestAndQuiz,on_delete=models.CASCADE)
   question = models.TextField(max_length=500)
   marks = models.IntegerField(default=0)
   option1 = models.CharField(max_length=100, blank=True, null=True)
   option2 = models.CharField(max_length=100, blank=True, null=True)
   option3 = models.CharField(max_length=100, blank=True, null=True)
   option4 = models.CharField(max_length=100, blank=True, null=True)
   imageOption1 = models.ImageField(upload_to='test_images/', blank=True, null=True)
   imageOption2 = models.ImageField(upload_to='test_images/', blank=True, null=True)
   imageOption3 = models.ImageField(upload_to='test_images/', blank=True, null=True)
   imageOption4 = models.ImageField(upload_to='test_images/', blank=True, null=True)
   textChoose = (('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4'))
   imageChoose = (('A', 'imageOption1'), ('B', 'imageOption2'), ('C', 'imageOption3'), ('D', 'imageOption4'))
   textAnswer = models.CharField(max_length=1, choices=textChoose, blank=True, null=True)
   imageAnswer = models.CharField(max_length=1, choices=imageChoose, blank=True, null=True)
   answer_type = models.CharField(max_length=10, choices=choices_type)
   
   def __str__(self):
      return self.question

class StudentAnnouncement(models.Model):
   title = models.CharField(max_length=100)
   target = models.CharField(max_length=100)
   detail = models.TextField(max_length=500)
   date_created = models.DateTimeField(auto_now_add=True)
   status = models.BooleanField(default=True)
   created_by = models.ForeignKey(Account,on_delete=models.CASCADE)
   
   
   def __str__(self):
      return self.title

class TestQuizes(models.Model):
   subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
   name = models.CharField(max_length=100)
   instructions = models.TextField(max_length=500)
   file = models.FileField(upload_to='assignments/', blank=True, null=True)
   date_created = models.DateTimeField(auto_now_add=True)
   date_due = models.DateTimeField()
   returned = models.BooleanField(default=False)
   status = models.BooleanField(default=True)
   
   
   def __str__(self):
      return self.name  

class TeacherAnnouncement(models.Model):
   title = models.CharField(max_length=100)
   detail = models.TextField(max_length=500)
   date_created = models.DateTimeField(auto_now_add=True)
   status = models.BooleanField(default=True)
   created_by = models.ForeignKey(Manager,on_delete=models.CASCADE)
   
   
   def __str__(self):
      return self.title
   
class Exam(models.Model):
   subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
   exam_date = models.DateTimeField()
   duration = models.IntegerField(default=0)
   date_created = models.DateTimeField(auto_now_add=True)
   teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
   no_of_questions = models.IntegerField(default=0)
   total_marks = models.IntegerField(default=0)
   status = models.BooleanField(default=True)
   teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
   
   def __str__(self):
      return self.subject.name
   
class Question(models.Model):
   choices_type = (
      ('text', 'Text'),
      ('image', 'Image'),
      ('type', 'Typed Answer'),
   )
   exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
   question = models.TextField(max_length=500)
   marks = models.IntegerField(default=0)
   option1 = models.CharField(max_length=100, blank=True, null=True)
   option2 = models.CharField(max_length=100, blank=True, null=True)
   option3 = models.CharField(max_length=100, blank=True, null=True)
   option4 = models.CharField(max_length=100, blank=True, null=True)
   imageOption1 = models.ImageField(upload_to='test_images/', blank=True, null=True)
   imageOption2 = models.ImageField(upload_to='test_images/', blank=True, null=True)
   imageOption3 = models.ImageField(upload_to='test_images/', blank=True, null=True)
   imageOption4 = models.ImageField(upload_to='test_images/', blank=True, null=True)
   typedAnswer = models.TextField(max_length=500, blank=True, null=True)
   textChoose = (('A', 'option1'), ('B', 'option2'), ('C', 'option3'), ('D', 'option4'))
   imageChoose = (('A', 'imageOption1'), ('B', 'imageOption2'), ('C', 'imageOption3'), ('D', 'imageOption4'))
   textAnswer = models.CharField(max_length=1, choices=textChoose, blank=True, null=True)
   imageAnswer = models.CharField(max_length=1, choices=imageChoose, blank=True, null=True)
   answer_type = models.CharField(max_length=10, choices=choices_type)
   
   def __str__(self):
      return self.question


class AskQuestion(models.Model):
   question = models.TextField()
   date_created = models.DateTimeField(auto_now_add=True)
   status = models.BooleanField(default=True)
   created_by = models.ForeignKey('student.Student', on_delete=models.CASCADE)
   paid = models.BooleanField(default=False)

   def __str__(self):
      return self.question

   def get_total_answers(self):
      return self.askquestionanswer_set.count()


class AskQuestionAnswer(models.Model):
   question = models.ForeignKey(AskQuestion, on_delete=models.CASCADE)
   answer = models.TextField()
   date_created = models.DateTimeField(auto_now_add=True)
   status = models.BooleanField(default=True)
   created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)

   def __str__(self):
      return self.answer
