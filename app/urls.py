from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user),
    path("home", views.index, name='home'),
    path('signup/', views.registration),
    path("pylessons", views.pylessons, name='pylessons'),
    path("quiz", views.pyquiz, name='quiz'),
    path("about", views.about, name='about'),
    path("contact", views.home, name='contact'),
    #Beginner's path
    path("varandtc",views.varandtc,name='varandtc'),
    path("datatype",views.datatype,name='datatype'),
    path("operation",views.operation,name='operation'),
    path("strings",views.strings,name='strings'),
    path("lists",views.lists,name='lists'),
    path("tuples",views.tuples,name='tuples'),
    path("diction",views.diction,name='diction'),
    path("sets",views.sets,name='sets'),
    path("loops",views.loops,name='loops'),
    #Intermediate's path
    path("clasobj",views.clasobj,name='clasobj'),
    path("filehand",views.filehand,name='filehand'),
    path("gui",views.gui,name='gui'),
    path("inherit",views.inherit,name='inherit'),
    path("modules",views.modules,name='modules'),
    path("polymor",views.polymor,name='polymor'),
    #AfterQuiz Path
    path("full",views.full,name='full'),
    path("eighty",views.eighty,name='eighty'),
    path("sixty",views.sixty,name='sixty'),
    path("forty",views.forty,name='forty'),
    path("twenty",views.twenty,name='twenty'),
    path("zero",views.zero,name='zero')
]