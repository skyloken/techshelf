from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from .models import Review


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'app/signup.html'


def index(request):
    review_list = Review.objects.order_by('-reviewed_at')
    context = {'review_list': review_list}
    return render(request, 'app/index.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'app/review_detail.html', context)
