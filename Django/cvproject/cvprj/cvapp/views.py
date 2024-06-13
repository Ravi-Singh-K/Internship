from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "User has successfully registered.")
            return redirect("log-in")
        else:
            username = request.POST['username']
            new_username = CustomUser.objects.filter(username = username)
            password1 = request.POST['password']
            password2 = request.POST['password2']
            form_email = request.POST['email']
            new_email = CustomUser.objects.filter(email = form_email)
            if password1 and password2 and password1 != password2:
                messages.error(request, "Passwords do not match with each other.")
            if new_email.count():
                messages.error(request, "Email exists already")
            if new_username.count():
                messages.error(request, "Username exists already")
            return redirect("home")
            
    else:
        form = UserRegistrationForm()
    context = {
        'form':form,
    }
    return render(request, 'home/home.html', context)


# Using LoginForm from forms.py
def do_login(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")
            
            else:
                messages.error(request, "Username and Password is incorrect. Login Failed")
                return redirect("log-in")
    form = LoginForm()
    
    context = {
        'form':form,
    }
    return render(request, 'log-in/login.html', context)


@login_required(login_url="log-in")
def dashboard(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {
        'user':user,
    }
    
    return render(request, 'home/dashboard.html', context)

def do_logout(request):
    logout(request)
    return redirect("log-in")


@login_required(login_url="log-in")
def do_update(request):
    return render(request, 'edit/update.html')


@login_required(login_url="log-in")
def personalinfo(request):
    user = get_object_or_404(CustomUser, id = request.user.id)
    if request.method == 'POST':
        form = UserInformationForm(request.POST, request.FILES, instance=user)
        if form.is_valid:
            form.save()
            messages.success(request, "Record Updated Successfully")
            return redirect("personalinfo")
        else:
            messages.error(request, "Record Failed To Update")
    form = UserInformationForm(instance=user)
    context = {
        'form':form,
    }
    return render(request, 'edit/personal-info.html', context)


# Update Education of CustomUser
@login_required(login_url="log-in")
def update_education(request):
    
    user = get_object_or_404(CustomUser, id=request.user.id)
    if request.method == 'POST':
        formset = EducationFormSet(request.POST, instance=user)
        if formset.is_valid():
            formset.save()
            messages.success(request, "Record Updated Successfully")
            return redirect("update_education")
        else:
            messages.error(request, "Record Failed To Update")
    else:
        formset = EducationFormSet(instance=user)

    context = {
        'formset': formset,
    }
    return render(request, 'edit/education.html', context)


# Update Work Experience of CustomUser - Company Model
@login_required(login_url="log-in")
def update_work_experience(request):
    user = get_object_or_404(CustomUser, id=request.user.id)

    if request.method == 'POST':
        formset = WorkFormSet(request.POST, instance=user)
        
        if formset.is_valid():
            formset.save()
            messages.success(request, "Record Updated Successfully")
            return redirect("update_experience")
        else:
            messages.error(request, "Record Failed To Update")
            return redirect("update_experience")
    else:
        formset = WorkFormSet(instance=user)
    
    context = {
        'formset' : formset,
    }
    return render(request, 'edit/company.html', context)


@login_required(login_url="log-in")
def update_link(request):
    user = get_object_or_404(CustomUser, id=request.user.id)

    if request.method == 'POST':
        formset = LinkFormSet(request.POST, instance=user)
        
        if formset.is_valid():
            formset.save()
            messages.success(request, "Record Updated Successfully")
            return redirect("update_link")
        else:
            messages.error(request, "Record Failed To Update")
            return redirect("update_link")
    else:
        formset = LinkFormSet(instance=user)
    
    context = {
        'formset' : formset,
    }
    return render(request, 'edit/social-media.html', context)



@login_required(login_url="log-in")
def update_achievement(request):
    user = get_object_or_404(CustomUser, id=request.user.id)

    if request.method == 'POST':
        formset = AchievementFormset(request.POST, instance=user)
        
        if formset.is_valid():
            formset.save()
            messages.success(request, "Record Updated Successfully")
            return redirect("update_achievement")
        else:
            messages.error(request, "Record Failed To Update")
            return redirect("update_achievement")
    else:
        formset = AchievementFormset(instance=user)
    
    context = {
        'formset' : formset,
    }
    return render(request, 'edit/achievement.html', context)


@login_required(login_url="log-in")
def update_reference(request):
    user = get_object_or_404(CustomUser, id = request.user.id)

    if request.method == 'POST':
        formset = ReferenceFormSet(request.POST, instance=user)

        if formset.is_valid():
            formset.save()
            messages.success(request, "Record Updated Successfully")
            return redirect("update_reference")
        else:
            messages.error(request, "Record Failed To Update")
            return redirect("update_reference")
    else:
        formset = ReferenceFormSet(instance=user)
    context = {
        'formset':formset,
    }
    return render(request, 'edit/reference.html', context)


@login_required(login_url="log-in")
def update_skill(request):

    if request.method == 'POST':
        form = UserSkillForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully")
            return redirect("update_skill")
        else:
            messages.error(request, "Record Failed To Update")
            return redirect("update_skill")
    else:
        form = UserSkillForm()
    context = {
        'form' : form,
    }
    return render(request, 'edit/skill.html', context)


@login_required(login_url="log-in")
def update_language(request):

    if request.method == 'POST':
        form = UserLanguageForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully")
            return redirect("update_language")
        else:
            messages.error(request, "Record Failed To Update")
            return redirect("update_language")
    else:
        form = UserLanguageForm()
    context = {
        'form' : form,
    }
    return render(request, 'edit/language.html', context)


def sample1(request):
    return render(request, 'cvsamples/sample1.html')
def sample2(request):
    return render(request, 'cvsamples/sample2.html')
def sample3(request):
    return render(request, 'cvsamples/sample3.html')


from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
import os

@login_required(login_url="log-in")
def download(request):
    user = CustomUser.objects.get(id = request.user.id)

    template_name = request.GET.get('template')
    if not template_name:
        return HttpResponse('Template parameter is required', status=400)

    templates = {
        'sample1': 'cvsamples/sample1.html',
        'sample2': 'cvsamples/sample2.html',
        'sample3': 'cvsamples/sample3.html'
    }

    template_path = templates.get(template_name)
    if not template_path:
        return HttpResponse('Invalid template name', status=400)
    
    profile_pic_path = os.path.join(settings.MEDIA_ROOT, user.profile_pic.name)
    context = {
        'user' : user,
        'profile_pic_url' : profile_pic_path,
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="sample.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors')
    return response

