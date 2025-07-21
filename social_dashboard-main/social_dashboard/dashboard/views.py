from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Post, Comment, Profile, SocialAccount
from .serializers import PostSerializer, CommentSerializer
from .forms import CustomUserCreationForm, ProfileForm

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        post.likes += 1
        post.save()
        return Response({'likes': post.likes}, status=status.HTTP_200_OK)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@login_required
def dashboard_page(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    return render(request, 'dashboard.html', {'profile': profile})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def update_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard-page')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form': form})

@login_required
def update_social_accounts(request):
    social, _ = SocialAccount.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        social.twitter_handle = request.POST.get('twitter_handle', '')
        social.facebook_handle = request.POST.get('facebook_handle', '')
        social.save()
        return redirect('dashboard-page')
    return render(request, 'update_social.html', {'social': social})
