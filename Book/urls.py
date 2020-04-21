from django.urls import path
from Book import views
from Library.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', views.homePage, name='homePage'),
    path('upload_book/', views.UploadBook, name='upload_book'),
    path('edit_book/<str:pk>/', views.EditBook, name='edit_book'),
    path('delete_book/<str:pk>/', views.DeleteBook, name='delete_book'),

    path('login/', views.LoginPage, name='login'),
    path('register/', views.RegisterPage, name='register'),
    path('logout/', views.LogOut, name='logout'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="Book/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="Book/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="Book/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="Book/password_reset_done.html"),
         name="password_reset_complete"),


]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
