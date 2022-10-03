from django.contrib import admin
from .models import Student, Result, RegistrationDeadline, StudentAssignment, StudentTest

admin.site.register(Student)
admin.site.register(Result)
admin.site.register(RegistrationDeadline)
admin.site.register(StudentAssignment)
admin.site.register(StudentTest)

