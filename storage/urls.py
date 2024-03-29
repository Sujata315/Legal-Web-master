from django.conf.urls import include
from django.urls import path
from .views import CasesListView
from .views import upload_form,detail_of_Cases,query_Cases

urlpatterns = [
    path('', CasesListView.as_view(), name='view_cases'),
    path('cases/<int:pk>', detail_of_Cases, name='detail_cases'),
    path('upload/', upload_form, name='upload_cases'),
    path('search/', query_Cases, name='search_cases'),
]