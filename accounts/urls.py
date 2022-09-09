from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [

    path('',views.home,name = 'home'),
    path('user/',views.userPage,name='user_page'),

    path('products/',views.products,name = 'products'),
    path('customer/<str:pk>/',views.customer,name = 'customer'),

    path('create_order/',views.createOrder,name = 'create_order'),
    path('update_order/<str:pk>',views.updateOrder,name = 'update_order'),
    path('delete_order/<str:pk>',views.deleteOrder,name = 'delete_order'),
    
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

    path('delete_customer/<str:pk>',views.delete_customer,name='delete_customer'),
    path('settings/',views.accountSettings,name='account_settings'),

]


'''
Class based view

1- Submit email form                        //PasswordResetView.as_view()
2- Email sent success message               //PasswordResetDoneView.as_view()
3- Link to password reset form in email     //PasswordResetConfirmView.as_view()
4- Password successfully changed message    //PasswordResetCompleteView.as_view()

'''