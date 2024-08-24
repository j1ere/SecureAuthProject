from django.shortcuts import render, redirect, get_object_or_404
from .models import RegistrationDetails, CustomUserModel
from .forms import AdminRegistrationForm, UserAccountCreation
import qrcode
from django.http import HttpResponse
from io import BytesIO
import base64


# Create your views here.
def home(request):
    return render(request, 'admin.html')

def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)

        if form.is_valid():
            registration=form.save()
            #redirect to a success page to show the generated barcode
            return redirect('generate_barcode', registration_id=registration.id)
        
    else:
        form = AdminRegistrationForm()

    return render(request, 'admin_register.html', {'form': form})

def user_register(request, security_code):
    try:
        registration = RegistrationDetails.objects.get(security_code=security_code, is_registered=False)
    except RegistrationDetails.DoesNotExist:
        return redirect('used_url')
    #registration = get_object_or_404(RegistrationDetails, security_code = security_code, is_registered= False)

    if request.method == 'POST':
        form = UserAccountCreation(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.full_names = registration.full_names
            user.hostel_name = registration.hostel_name
            user.phone_number = registration.phone_number

            user.save()

            registration.is_registered = True
            registration.save()

            #invalidate the security code after successful registration

            return redirect('registration_success')
    else:
        form = UserAccountCreation()
    return render(request, 'user_register.html', {'form': form, 'registration': registration})


def generate_barcode(request, registration_id):
    profile = get_object_or_404(RegistrationDetails, id= registration_id)
    url = f'http://192.168.46.115:8000/accounts/secure/{profile.security_code}/'
    qr = qrcode.make(url)
    # response = HttpResponse(content_type='image/png')
    # qr.save(response, 'PNG')
    # return response
    buffered = BytesIO()
    qr.save(buffered, format='PNG')
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return render(request, 'display_barcode.html', {'barcode_image': img_str, 'profile': profile})


def registration_success(request):
    return render(request, 'registration_success.html')

def used_url(request):
    return render(request,'used_url.html')

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

def student_roombooking_page(request):
    return render(request, 'student_roombooking.html')