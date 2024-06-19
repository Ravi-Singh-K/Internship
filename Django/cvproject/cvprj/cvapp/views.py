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
    user = CustomUser.objects.get(id = request.user.id)

    if request.method == 'GET':
        form = UserInformationForm(instance = user)

    elif request.method in ['POST', 'PUT', 'PATCH']:
        form = UserInformationForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, "Record has been successfully Updated.")
            return redirect("personalinfo")
        
        else:
            messages.error(request, "Records Failed To Update")
            return redirect("personalinfo")
        
    form = UserInformationForm(instance = user)
    context = {
        'form':form,
    }
    return render(request, 'edit/personal-info.html', context)


# Update Education of CustomUser
@login_required(login_url="log-in")
def update_education(request):
    
    user = CustomUser.objects.get(id = request.user.id)
    if request.method == 'GET':
        formset = EducationFormSet(instance=user)

    elif request.method in ['POST', 'PUT', 'PATCH']:
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
    user = CustomUser.objects.get(id = request.user.id)
    if request.method == 'GET':
        formset = WorkFormSet(instance=user)

    elif request.method in ['POST', 'PUT', 'PATCH']:
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
    user = CustomUser.objects.get(id = request.user.id)

    if request.method == 'GET':
        formset = LinkFormSet(instance=user)

    elif request.method in ['POST', 'PUT', 'PATCH']:
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
    user = CustomUser.objects.get(id = request.user.id)

    if request.method == 'GET':
        formset = AchievementFormset(instance=user)

    elif request.method in ['POST', 'PUT', 'PATCH']:
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
    user = CustomUser.objects.get(id = request.user.id)

    if request.method == 'GET':
        formset = ReferenceFormSet(instance=user)

    elif request.method in ['POST', 'PUT', 'PATCH']:
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
    skills = Skill.objects.all()

    if request.method == 'POST':
        form = UserSkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill added successfully")
            return redirect('update_skill')
        else:
            messages.error(request, "Failed to add skill")
    else:
        form = UserSkillForm()

    context = {
        'form': form,
        'skills': skills,
    }
    return render(request, 'edit/skill.html', context)

@login_required(login_url="log-in")
def edit_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)

    if request.method in ['POST', 'PUT', 'PATCH']:
        form = UserSkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill updated successfully")
            return redirect('update_skill')
        else:
            messages.error(request, "Failed to update skill")
    else:
        form = UserSkillForm(instance=skill)

    context = {
        'form': form,
        'skill': skill,
    }
    return render(request, 'edit/edit_skill.html', context)



@login_required(login_url="log-in")
def update_language(request):
    languages = Language.objects.all()

    if request.method == 'POST':
        form = UserLanguageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Language added successfully")
            return redirect('update_language')
        else:
            messages.error(request, "Failed to add language")
    else:
        form = UserLanguageForm()

    context = {
        'form': form,
        'languages': languages,
    }
    return render(request, 'edit/language.html', context)

@login_required(login_url="log-in")
def edit_language(request, language_id):
    language = get_object_or_404(Language, id=language_id)

    if request.method in ['POST', 'PUT', 'PATCH']:
        form = UserLanguageForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            messages.success(request, "Language updated successfully")
            return redirect('update_language')
        else:
            messages.error(request, "Failed to update language")
    else:
        form = UserLanguageForm(instance=language)

    context = {
        'form': form,
        'language': language,
    }
    return render(request, 'edit/edit_language.html', context)



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

