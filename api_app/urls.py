from django.urls import path

from .views import StudentViews, deleteStudentViews, getStudentViews, upStudentViews


urlpatterns = [
    path('student/', StudentViews.as_view()),
    path('getstudent/', getStudentViews.as_view()),
    path('getstudent/<int:id>', getStudentViews.as_view()),
    path('updatestudent/<int:id>', upStudentViews.as_view()),
    path('deletestudent/<int:id>', deleteStudentViews.as_view()),
    
      
]

