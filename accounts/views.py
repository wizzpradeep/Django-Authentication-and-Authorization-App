# views.py
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .utils import send_verification_email
import uuid
from .models import EmailVerification
from django.contrib import messages
from .decorators import login_required, user_is_authenticated

@user_is_authenticated
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            token = uuid.uuid4()
            EmailVerificationObject = EmailVerification(user=user, token=token, is_verified=False)
            EmailVerificationObject.save()
            send_verification_email(request, user.email, token)
            messages.success(request, "Your account has been created successfully, please check your email to verify your account.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def email_verify(request, token):
    EmailVerificationObject = EmailVerification.objects.filter(token=token).first()
    if EmailVerificationObject:
        EmailVerificationObject.is_verified = True
        EmailVerificationObject.user.is_active = True
        EmailVerificationObject.user.save()
        EmailVerificationObject.save()
        messages.success(request, "Email verified successfully. You can now log in.")
    else:
        messages.error(request, "Invalid verification token.")
    return render(request, 'registration/email_verify.html')

@user_is_authenticated
def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                EmailVerificationObject = EmailVerification.objects.filter(user=user).first()
                if EmailVerificationObject and EmailVerificationObject.is_verified:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, "User is not verified")
            else:
                messages.error(request, "Invalid email or password")
        else:
            messages.error(request, "Invalid email or password")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
