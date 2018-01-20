from django.conf.urls import url
from . import views





urlpatterns =[

  url(r'^labels',views.ListLabel.as_view()),
  url(r'^label/(?P<label>)/edit/',views.UpdateLabel.as_view()),
  url(r'^label/(?P<pk>\d+)/delete/',views.DeleteLabel.as_view()),
  url(r'^label/create',views.CreateLabel.as_view()),
  

]
