from django.urls import path
from student_app import views
from quiz_app import views
urlpatterns = [

    path("p", views.check_answer, name="paper"),
    

]
