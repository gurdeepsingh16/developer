
from django.urls import path
from student_app import views

urlpatterns = [
    path('student_register', views.student_register, name='student_register'),
    path('login', views.student_login, name="login"),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('stuadd', views.stuadd, name='stuadd'),
    path('stushow', views.stushow, name='stushow'),
    path('comment', views.comment_func, name='comment'),
    path('comment_show<int:id>', views.show_comment, name='comment_show'),
    path('delete<int:id>', views.delete, name='delete'),
    path('delete_comment<int:id>', views.delete_comment, name='delete_comment'),
    path('update<int:id>', views.update, name='update'),
    path('update<int:id>', views.update, name='update'),
]
