from django.conf.urls import url
from . import views





urlpatterns =[

  url(r'^api/notes',views.ListNote.as_view()),
  url(r'^api/note/(?P<pk>\d+)/edit/',views.UpdateNote.as_view()),
  url(r'^api/note/(?P<pk>\d+)/delete/',views.DeleteNote.as_view()),
  url(r'api/create',views.CreateNote.as_view())
  

]
