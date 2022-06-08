from django.urls import path
from .views import LibraryDetails,LibraryInfo

urlpatterns=[
    path('details/',LibraryDetails.as_view()),
    path('upd/<int:id>/',LibraryInfo.as_view()),
    path('del/<int:id>/',LibraryInfo.as_view())
]
