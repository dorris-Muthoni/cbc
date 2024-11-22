from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def charts_apexcharts(request):
    return render(request, 'charts-apexcharts.html')

def co_club(request):
    return render(request, 'co-club.html')

def co_events(request):
    return render(request, 'co-events.html')

def pages_blank(request):
    return render(request, 'pages-blank.html')

def pages_contact(request):
    return render(request, 'pages-contact.html')

def pages_error_404(request):
    return render(request, 'pages-error-404.html')

def pages_faq(request):
    return render(request, 'pages-faq.html')

def pages_login(request):
    return render(request, 'pages-login.html')

def pages_register(request):
    return render(request, 'pages-register.html')

def students_assignments(request):
    return render(request, 'students-assignments.html')

def students_assignment_editors(request):
    return render(request, 'students-assignment-editors.html')

def students_badges(request):
    return render(request, 'students-badges.html')

def students_class_posts(request):
    return render(request, 'students-class-posts.html')

def students_exams(request):
    return render(request, 'students-exams.html')

def students_group_projects(request):
    return render(request, 'students-group-projects.html')

def students_live_classes(request):
    return render(request, 'students-live-classes.html')

def students_profiles(request):
    return render(request, 'students-profiles.html')

def students_subjects(request):
    return render(request, 'students-subjects.html')

def users_profile(request):
    return render(request, 'users-profile.html')
