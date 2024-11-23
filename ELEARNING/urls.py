from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('', views.home,name='my_index'),
    path('enrollment_documents/', views.enrollment_documents,name='my_enrollment_documents'),
    path('enrollment_form/', views.enrollment_form,name='my_enrollment_form'),
    path('co-club/', views.co_club,name='my_co_club'),
    path('co-events/', views.co_events,name='my_co_events'),
    path('pages-blank/', views.pages_blank,name='my_pages_blank'),
    path('pages-contact/', views.pages_contact,name='my_pages_contact'),
    path('pages-error-404/', views.pages_error_404,name='my_pages_error_404'),
    path('pages-faq/', views.pages_faq,name='my_pages_faq'),
    path('pages-login/', views.pages_login,name='my_pages_login'),
    path('pages-register/', views.pages_register,name='my_pages_register'),
    path('students-assignment-editors/', views.students_assignment_editors,name='my_students_assignment_editors'),
    path('students-assingments/', views.students_assignments,name='my_students_assignments'),
    path('students-badges/', views.students_badges,name='my_students_badges'),
    path('students-class-posts/', views.students_class_posts,name='my_students_class_posts'),
    path('students-exams/', views.students_exams,name='my_students_exams'),
    path('students-group-projects/', views.students_group_projects,name='my_students_group_projects'),
    path('students-live-classes/', views.students_live_classes,name='my_students_live_classes'),
    path('students-profiles/', views.students_profiles,name='my_students_profiles'),
    path('students-subjects/', views.students_subjects,name='my_students_subjects'),
    path('users-profile/', views.users_profile,name='my_users_profile'),
]

# Add static files urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root  = settings.MEDIA_ROOT)