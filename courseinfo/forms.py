from django import forms
from courseinfo.models import Instructor, Section, Course, Semester, Student, Registration

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'


    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()

        return result

# Section

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

    def clean_section_name(self):
        return self.cleaned_data['section_name'].strip()

# Course
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


    def clean_course_number(self):
        return self.cleaned_data['course_number'].strip()

    def clean_course_name(self):
        return self.cleaned_data['course_name'].strip()

# Semester
class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'

    def clean_semester_id(self):
        return self.cleaned_data['semester_id'].strip()


# Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_disambiguator(self):
        if len(self.cleaned_data['disambiguator']) == 0:
            result = self.cleaned_data['disambiguator']
        else:
            result = self.cleaned_data['disambiguator'].strip()

        return result

# Registration
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'


    def clean_registration_id(self):
        return self.cleaned_data['registration_id'].strip()
