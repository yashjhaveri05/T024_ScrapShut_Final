from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.ngo, name='ngo_signup'),
    path('donor_signup/', views.donor_signup, name='donor_signup'),
    path('login/',views.login_view, name='login_view'),
    path('logout/', views.logout, name='logout'),
    path('home/',views.home, name='home'),
    path('create/',views.create,name='create'),
    path('details/<int:pk>',views.requirements_detail,name='requirements_detail'),
    path('ngo_req/',views.ngo_req,name='ngo_req'),
    path('update/<requirement_id>',views.update,name='update'),
    path('delete/<requirement_id>',views.delete,name='delete'),
    path('donate/',views.donate,name='donate'),
    path('donations_made/',views.donations_made,name='donations_made'),
    path('donations_received/', views.donations_received,name='donations_received'),
    path('validate/<int:pk>', views.validate,name='validate'),
    path('gifts/', views.gifts, name='gifts'),
    path('redeem/<int:pk>', views.redeem, name='redeem'),
    path('redeemed_gifts/', views.redeemed_gifts, name='redeemed_gifts'),
]

