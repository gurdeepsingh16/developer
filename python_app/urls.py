
from django.urls import path
from python_app import views

urlpatterns = [

    path('', views.home, name='home'),
    path('show', views.show_practice, name='show'),
    path('practice<int:id>', views.practice_more, name="practice"),
    path('add', views.add_func, name="add"),
    path('add1', views.add_pracctice, name="add1"),

    # search and show
    path('search', views.search, name='search'),
    path('sly', views.search_subtopic, name="sly"),
    path('s<int:id>', views.search_subtopic2, name='search_subtopic'),

    # login and register and logout

    # path('register', views.register, name="register"),
    #     path('login', views.login, name="login"),
    #     path('logout', views.logout, name='logout')
    # ]
]
