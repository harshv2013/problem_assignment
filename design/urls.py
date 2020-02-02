from django.urls import path
from . import views

app_name = 'design'

# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]


urlpatterns = [
    # path('person/create/', views.PersonCreate.as_view(), name='person_create'),
    path('emp', views.emp , name='home'),
    # path('show', views.show ),
    path('show', views.PersonListView.as_view(), name='person-list'),
    # path('show', views.PersonDetailView.as_view(), name='person-detail'),
    path('detail/<int:id>', views.person_detail, name='person-detail'),
    path('edit/<int:id>', views.edit),
    # path('update', views.update),
    path('delete/<int:id>', views.destroy),

]