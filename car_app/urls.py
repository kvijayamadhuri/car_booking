from django.urls import path
from .views import CarCreateView,CarListView,CarUpdateView,delete_user,details_user

urlpatterns=[
    path('create-user/',CarCreateView.as_view()),
    path('list-user/', CarListView.as_view()),
    path('update-user/<int:id>/',CarUpdateView.as_view()),
    path('delete-user/<int:id>/',delete_user),
    path('details-user/<int:id>/',details_user)
]