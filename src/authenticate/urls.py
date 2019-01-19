from django.urls import path
from .views import (Home,
                    LoginUser,
                    LogoutUser,
                    RegisterUser,
                    EditProfile,
                    ChangePassword,
                    DeleteAccount
                    )

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('edit_profile/', EditProfile.as_view(), name='edit_profile'),
    path('change_password/', ChangePassword.as_view(), name='change_password'),
    path('delete_account/', DeleteAccount.as_view(), name='delete_account'),
]
