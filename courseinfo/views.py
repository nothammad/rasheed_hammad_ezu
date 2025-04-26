from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from courseinfo.forms import InstructorForm, SectionForm, CourseForm, StudentForm, SemesterForm, RegistrationForm
from courseinfo.models import (
    Instructor,
    Section,
    Course,
    Semester,
    Student,
    Registration,
)
from courseinfo.utils import ObjectCreateMixin, PageLinksMixin


# Create your views here.


class InstructorList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin,ListView):
    paginate_by = 25
    model = Instructor
    permission_required = 'courseinfo.view_instructor'


class InstructorDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Instructor
    permission_required = 'courseinfo.view_instructor'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        instructor = self.get_object()
        section_list = instructor.sections.all()
        context['section_list'] = section_list
        return context

class InstructorCreate(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    form_class = InstructorForm
    model = Instructor
    permission_required = 'courseinfo.add_instructor'

class InstructorUpdate(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    form_class = InstructorForm
    model = Instructor
    permission_required = 'courseinfo.change_instructor'
    template_name = 'courseinfo/instructor_form_update.html'

class InstructorDelete(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = Instructor
    permission_required = 'courseinfo.delete_instructor'
    success_url = reverse_lazy('courseinfo_instructor_list_urlpattern')

class SectionList(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    model = Section
    permission_required = 'courseinfo.view_section'

class SectionDetail(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    model = Section
    permission_required = 'courseinfo.view_section'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        section = self.get_object()
        semester = section.semester
        course = section.course
        instructor = section.instructor
        registration_list = section.registrations.all()
        context['semester'] = semester
        context['course'] = course
        context['instructor'] = instructor
        context['registration_list'] = registration_list
        return context

class SectionCreate(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    form_class = SectionForm
    model = Section
    permission_required = 'courseinfo.add_section'

class SectionUpdate(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    form_class = SectionForm
    model = Section
    permission_required = 'courseinfo.change_section'
    template_name = 'courseinfo/section_form_update.html'

class SectionDelete(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = Section
    permission_required = 'courseinfo.delete_section'
    success_url = reverse_lazy('courseinfo_section_list_urlpattern')

class CourseList(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    model = Course
    permission_required = 'courseinfo.view_course'

class CourseDetail(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    model = Course
    permission_required = 'courseinfo.view_course'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        course = self.get_object()
        course_list = course.sections.all()
        context['course_list'] = course_list
        return context

class CourseCreate(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    form_class = CourseForm
    model = Course
    permission_required = 'courseinfo.add_course'

class CourseUpdate(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    form_class = CourseForm
    model = Course
    permission_required = 'courseinfo.change_course'
    template_name = 'courseinfo/course_form_update.html'

class CourseDelete(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = Course
    permission_required = 'courseinfo.delete_course'
    success_url = reverse_lazy('courseinfo_course_list_urlpattern')

class SemesterList(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    model = Semester
    permission_required = 'courseinfo.view_semester'

class SemesterDetail(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    model = Semester
    permission_required = 'courseinfo.view_semester'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        semester = self.get_object()
        section_list = semester.sections.all()
        context['section_list'] = section_list
        return context

class SemesterCreate(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    form_class = SemesterForm
    model = Semester
    permission_required = 'courseinfo.add_semester'

class SemesterUpdate(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    form_class = SemesterForm
    model = Semester
    permission_required = 'courseinfo.change_semester'
    template_name = 'courseinfo/semester_form_update.html'

class SemesterDelete(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = Semester
    permission_required = 'courseinfo.delete_semester'
    success_url = reverse_lazy('courseinfo_semester_list_urlpattern')
class StudentList(LoginRequiredMixin, PermissionRequiredMixin,PageLinksMixin,ListView):
    paginate_by = 25
    model = Student
    permission_required = 'courseinfo.view_student'


class StudentDetail(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    model = Student
    permission_required = 'courseinfo.view_student'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        student = self.get_object()
        registration_list = student.registrations.all()
        context['registration_list'] = registration_list
        return context

class StudentCreate(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    form_class = StudentForm
    model = Student
    permission_required = 'courseinfo.add_student'

class StudentUpdate(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    form_class = StudentForm
    model = Student
    permission_required = 'courseinfo.change_student'
    template_name = 'courseinfo/student_form_update.html'

class StudentDelete(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = Student
    permission_required = 'courseinfo.delete_student'
    success_url = reverse_lazy('courseinfo_student_list_urlpattern')

class RegistrationList(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    model = Registration
    permission_required = 'courseinfo.view_registration'

class RegistrationDetail(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    model = Registration
    permission_required = 'courseinfo.view_registration'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        registration = self.get_object()
        section = registration.section
        student = registration.student
        context['section'] = section
        context['student'] = student
        return context

class RegistrationCreate(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    form_class = RegistrationForm
    model = Registration
    permission_required = 'courseinfo.add_registration'

class RegistrationUpdate(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    form_class = RegistrationForm
    model = Registration
    permission_required = 'courseinfo.change_registration'
    template_name = 'courseinfo/registration_form_update.html'

class RegistrationDelete(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model = Registration
    permission_required = 'courseinfo.delete_registration'
    success_url = reverse_lazy('courseinfo_registration_list_urlpattern')