from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^startpage/', views.start_page, name='start_page'),
    # url(r'^ownerlogin/', views.OwnerLogin, name='owner_new'),
    # url(r'^login/', views.login_view, name='login'),
    # url(r'^register/', views.register_view, name='register'),
    # url(r'^ownerreg/', views.OwnerRegister, name='owner_reg'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^adminloginpage/$', views.adminloginform, name='adminloginpage'),
    url(r'^ownerloginpage/$', views.ownerloginform, name='ownerloginpage'),
    url(r'^customerloginpage/$', views.customerloginform, name='customerloginpage'),
    url(r'^accounts/profile/$', views.owner_profile, name='owner_page'),
    url(r'^ownersignup/$', views.ownersignup, name='ownersignup'),
    url(r'^customersignup/$', views.customersignup, name='customersignup'),
    url(r'^yourcars/$', views.your_cars, name='your_cars'),
    url(r'^addcar/$', views.add_car, name='add_car'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^delete_answer/(?P<object_id>.*)', views.objectDelete, name='delete_object'),
    url(r'^modify/(?P<object_id>.*)', views.modifyCar, name='modify_car'),
    url(r'^allcars/$', views.allCars, name='allcars'),
    url(r'^reserve/(?P<object_id>.*)', views.make_reservation, name='reserve'),
    url(r'^myreservations/$', views.my_reservations, name='myreservations'),
    #   url(r'^save-session-data/$', views.save_session_data, name='save_session_data'),
    #   url(r'^access-session-data/$', views.access_session_data, name='access_session_data'),
    #   url(r'^delete-session-data/$', views.delete_session_data, name='delete_session_data'),
    url(r'^test-session/$', views.test_session, name='test_session'),
    url(r'^test-delete/$', views.test_delete, name='test_delete'),
    url(r'^filtercars/$', views.filteredcars, name='filteredcars'),
    url(r'^modifyreservation/(?P<object_id>.*)', views.modify_reservation, name='modify_reservation'),

    url(r'^deletereservation/(?P<object_id>.*)', views.delete_reservation, name='delete_reservation'),
    url(r'^allowners/$', views.allOwners, name='allowners'),
    url(r'^approvedowners/(?P<object_id>.*)', views.approvedOwners, name='approvedowners'),
    url(r'^rejectowners/(?P<object_id>.*)', views.rejectOwners, name='rejectowners'),
    url(r'^notifications/$', views.notifications, name='notification'),
    url(r'^mytrips/$', views.mytrips, name='mytrips'),
    url(r'^addfeedback/(?P<object_id>.*)', views.adduserfeedback, name='addfeedback'),
    url(r'^myfeedbacks/$', views.displayfeedbacks, name='myfeedbacks'),
    url(r'^errorpage/$', views.errorpage, name='errorpage'),
    url(r'^showmap/(?P<object_id>.*)', views.showmap, name='showmap'),
    url(r'^ownerdocuments/(?P<object_id>.*)', views.OwnerDocs, name='opendocs'),
    
]