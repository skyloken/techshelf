from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from . import api
from .forms import LoginForm

urlpatterns = [

    path('', views.index, name='index'),
    path('reviews/<int:review_id>/', views.review_detail, name='review_detail'),

    path('books/', views.books, name='books'),
    path('books/<int:book_id>', views.book_detail, name='book_detail'),

    path('api/reviews/<int:review_id>/like/', api.LikeReview.as_view(), name='like_review_api'),
    path('api/books/<int:book_id>/mark/', api.MarkBook.as_view(), name='mark_book_api'),

    path('login/', auth_views.LoginView.as_view(template_name='app/login.html', form_class=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
