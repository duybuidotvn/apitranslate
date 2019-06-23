from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    # path('detail', views.detail, name='detail'),
    # path('<int:request_id>/detail', views.detail, name='detail'),
    # path('<int:request_id>/step1', views.step1, name='step1'),
    # path('<int:request_id>/step2', views.step2, name='step2'),
    # path('<int:request_id>/step3', views.step3, name='step3'),
    # path('index.html', views.index, name='index.html'),
    # path('phuong', views.phuong, name='phuong'),
    # path('hien', views.hien, name='hien'),
    # path('hack', views.hack, name='hack'),
    # path('<int:request_id>/',views.detail, name='detail'),
    # path('<int:request_id>/result',views.result, name='result'), 
    # path('<int:request_id>/vote/<int:request_id1>',views.vote, name='vote'),
    # path('<int:pk>/detail',views.testGenericView.as_view(), name='detail'),
]