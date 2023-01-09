from django.contrib import admin
from .models import Student, Result, RegistrationDeadline, StudentAssignment, StudentExam, StudentTest

admin.site.register(Student)
admin.site.register(Result)
admin.site.register(RegistrationDeadline)
admin.site.register(StudentAssignment)
admin.site.register(StudentTest)
admin.site.register(StudentExam)

