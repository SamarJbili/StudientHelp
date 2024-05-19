from django.urls import path
from . import views
from .views import EvenementCulturelUpdateView, EvenementScientifiqueUpdateView, TransportUpdateView,LogementUpdateView, TransportDeleteView,eventCultDeleteView,eventScDeleteView,StageDeleteView,MesPostView,eventCultView,eventScView,logementDeleteView,StageCreateView, LogementCreateView, EvenementScientifiqueCreateView,EvenementCulturelCreateView,TransportCreateView,LogementListView,StageListView,TransportListView,CommentCreateView,LikeView,PostDetailView,acceuilView


urlpatterns = [
    # URLs for posts
    path('', acceuilView.as_view(), name='acceuil'),
    path('inscription/',views.inscription, name = 'inscription'), 
    path('change-password/',views.change_password, name='change_password'),
    

    path('create-stage/', StageCreateView.as_view(), name='create-stage'),
    path('create-logement/', LogementCreateView.as_view(), name='create-logement'),
    path('create-evenementCulturel/', EvenementCulturelCreateView.as_view(), name='create-evenementCult'),
    path('create-evenementSc/', EvenementScientifiqueCreateView.as_view(), name='create-evenementSc'),
    path('create-transport/', TransportCreateView.as_view(), name='create-transport'),


    path('logement/', LogementListView.as_view(), name='logement-list'),
    path('eventCult/', eventCultView.as_view(), name='eventCult-list'),
    path('eventSc/', eventScView.as_view(), name='eventSc-list'),

    path('stage/', StageListView.as_view(), name='stage-list'),
    path('transport/', TransportListView.as_view(), name='transport-list'),


    path('inscription/',views.register, name = 'register'), 
    path('change-password/',views.change_password, name='change_password'),

    path('search/',views.search, name='search'),

    path('mespost/', MesPostView.as_view(), name='mespost-view'),

    path('inputform/',views.inputform, name='inputform'),

    path('<int:pk>/deletelog/', logementDeleteView.as_view(), name='logement_delete'),
    path('<int:pk>/deletetransport/', TransportDeleteView.as_view(), name='transport-delete'),
    path('<int:pk>/deleteeventsc/', eventScDeleteView.as_view(), name='eventSc-delete'),
    path('<int:pk>/deleteeventcult/', eventCultDeleteView.as_view(), name='eventCult-delete'),
    path('<int:pk>/deletestage/',StageDeleteView.as_view(), name='stage-delete'),

    path('<int:pk>/updatelogement/', LogementUpdateView.as_view(), name='logement-update'),
    path('<int:pk>/updatetransport/', TransportUpdateView.as_view(), name='transport-update'),
    path('<int:pk>/updateeventsc/', EvenementScientifiqueUpdateView.as_view(), name='eventSc-update'),
    path('<int:pk>/updateeventcult/', EvenementCulturelUpdateView.as_view(), name='eventCult-update'),
    path('<int:pk>/updateStage/', LogementUpdateView.as_view(), name='Stage-update'),



    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='add-comment'),
    path('post/<int:post_id>/like/', LikeView.as_view(), name='like-post')


]
