from django.urls import path
from pvr import views

app_name = 'pvr'
urlpatterns = [
                # path("",views.home,name="home"),
                path('',views.movieListview.as_view(),name="home"),
                # path("addmovie/",views.addmovie,name='addmovie'),
                path('addmovie/',views.createview.as_view(),name='addmovie'),
                # path('viewmovie/<int:p>', views.viewmovie, name='viewmovie'),
                path('movie/<int:pk>',views.detailview.as_view(),name="viewmovie"),
                # path('deletemovie/<int:p>', views.deletemovie, name='deletemovie'),
                # path('editmovie/<int:p>', views.editmovie, name='editmovie'),
                path('updatemovie/<int:pk>',views.updatemovie.as_view(),name='editmovie'),
                path('deletemovie/<int:pk>',views.deleteview.as_view(),name='deletemovie'),

            ]