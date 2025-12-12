from django.views import generic
from .models import Student, Course, Enrollment
from .forms import StudentForm, EnrollmentForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


# Student list with simple search
class StudentListView(LoginRequiredMixin, generic.ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(
                Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(roll_number__icontains=q) | Q(email__icontains=q)
            )
        return qs

class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'

class StudentCreateView(generic.CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'

class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'

class StudentDeleteView(generic.DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('students:student-list')

# Optional: Enrollment CRUD
class EnrollmentCreateView(generic.CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'students/enrollment_form.html'
    success_url = reverse_lazy('students:student-list')
