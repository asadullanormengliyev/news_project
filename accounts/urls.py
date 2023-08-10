from django.urls import path
from .views import dashboard_view  # user_login (Bu login qismini qo'lda yozgan edik)
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView # Djangoning tayyor login viewsi

urlpatterns=[
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/',PasswordChangeDoneView.as_view(), name='password_choneg_done'),
    path('profile', dashboard_view, name='user_profile')
]
