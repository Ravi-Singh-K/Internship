from django.forms import Media
from django.shortcuts import render, redirect, get_object_or_404
from django.http import request
from django.urls import reverse
from portapp.models import CustomUser, Education, Experience, Skill
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login,  logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def home_view(request):
    if request.method == 'POST':
        print("---------------------------------------------------------")
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        print("Hello Part 1 success")
        if not fullname or not username or not email or not phone or not password or not repassword:
            print("Part 2.1")
            messages.error(request, "All the fields are required.") 
        elif password != repassword:
            print("Part 2.2")
            messages.error(request, "The password do not match with each other.")
        else:
            print("Part 3.1")
            if CustomUser.objects.filter(email = email).exists():
                print("Part 3.2")
                messages.error(request, "The email already exists.")
            else:
                print("Part 4.1")
                name = fullname.split()
                user = CustomUser(
                    first_name = name[0],
                    last_name = name[-1],
                    username = username,
                    email = email,
                    contact = phone,
                )
                user.set_password(password)
                user.save()
                messages.success(request, "Registration Successful")
                print("First Name : ", user.first_name)
                print("Last Name : ", user.last_name)
                print("Username : ", user.username)
                print("Email : ", user.email)
                print("Contact : ", user.contact)
                print("Password : ", user.password)
                print("Hello Part 4.2")
                return redirect("login")
    return render(request, "home/index.html")

# def login_view(request):
    # print("_*_*_*_*_*_*_*_*_*_*_*_")
    # print(request.POST)
    # if request.method == 'POST':
    #     login_email = request.POST["email"]
    #     login_password = request.POST["password"]

    #     print(login_email, login_password)

    #     if not login_email or not login_password:
    #         print("Part 1")
    #         messages.error(request, "All fields are required.")
    #     else:
    #         print("Part 2")
    #         registered_user = authenticate(email = login_email, password = login_password)

    #         print(registered_user)
    #         if registered_user is None:
    #             print("Part 3")
    #             print("Login Failed")
    #             return redirect("login")
    #         else:
    #             print("Part 4")
    #             print("Login Success ")
    #             login(request, registered_user)
    #             return redirect("dashboard")
    # print("Hello world ")
    # return render(request, 'home/login.html')

def login_view(request):
    if request.method == 'POST':
        print(request.POST)
        login_email = request.POST["email"]
        print(login_email)
        login_password = request.POST["password"]
        print(login_password)

        user = authenticate(username = login_email, password = login_password)
        if user is not None:
            print("Trace user success")
            login(request, user)
            messages.success(request, "Successfully logged in.")
            return redirect("dashboard")
        else:
            print("Trace failed user")
            messages.error(request, "Login failed.")
            return redirect("login")
    return render(request, "home/login.html")

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, "home/dashboard.html")

def logout_view(request):
    logout(request)
    return redirect("login")

# @login_required(login_url="login")
# def update(request):
#     user = CustomUser.objects.get(id = request.user.id)
#     context = {
#         'user':user,
#     }
#     return render(request, 'home/update.html', context)

# @login_required(login_url='login')
# def edit_view(request):
#     if request.method == 'POST':
#         u_id = request.POST['u_id']
#         profile_picture = request.FILES['profile']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         contact = request.POST['contact']
#         address = request.POST['address']
#         dob = request.POST['dob']
#         summary = request.POST['summary']
#         link = request.POST['link']
#         email = request.POST['email']
#         school_name = request.POST['school_name']
#         school_grade = request.POST['school_grade']
#         school_passed_year = request.POST['school_passed_year']
#         collage_name = request.POST['collage_name']
#         collage_grade = request.POST['collage_grade']
#         collage_passed_year = request.POST['collage_passed_year']
#         skill_name = request.POST['skill_name']
#         company_name = request.POST['company_name']
#         position = request.POST['position']
#         duration = request.POST['duration']
#         password = request.POST['password']

#         user = CustomUser.objects.get(id = u_id)
#         print(user)
        
#         user.profile_pic = profile_picture
#         user.first_name = first_name
#         user.last_name = last_name
#         user.username = username
#         user.contact = contact
#         user.address = address
#         user.dob = dob
#         user.summary = summary
#         user.link = link
#         user.email = email
#         user.set_password(password)
#         user.save()

#         education = Education.objects.get(user = user)
#         school_name = school_name,
#         school_grade = school_grade,
#         school_passed_year = school_passed_year,
#         collage_name = collage_name,
#         collage_grade = collage_grade,
#         collage_passed_year = collage_passed_year
#         education.save()

#         skill = Skill.objects.get(user = user)
#         skill_name = skill_name,
#         skill.save()

#         experience = Experience.objects.get(user = user)
#         company_name = company_name,
#         position = position,
#         duration = duration
#         experience.save()
        
#         return redirect("dashboard")
#     return render(request, 'home/update.html')


@login_required(login_url="login")
def update(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        'user': user,
    }
    return render(request, 'home/update.html', context)

@login_required(login_url='login')
def edit_view(request):
    if request.method == 'POST':
        u_id = request.POST['u_id']
        profile_picture = request.FILES.get('profile')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        summary = request.POST.get('summary')
        link = request.POST.get('link')
        email = request.POST.get('email')
        school_name = request.POST.get('school_name')
        school_grade = request.POST.get('school_grade')
        school_passed_year = request.POST.get('school_passed_year')
        collage_name = request.POST.get('collage_name')
        collage_grade = request.POST.get('collage_grade')
        collage_passed_year = request.POST.get('collage_passed_year')
        skill_name = request.POST.get('skill_name')
        company_name = request.POST.get('company_name')
        position = request.POST.get('position')
        duration = request.POST.get('duration')
        password = request.POST.get('password')

        user = get_object_or_404(CustomUser, id=u_id)
        
        if profile_picture:
            user.profile_pic = profile_picture
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.contact = contact
        user.address = address
        user.dob = dob
        user.summary = summary
        user.link = link
        user.email = email
        if password:
            user.set_password(password)
        user.save()

        education, created = Education.objects.get_or_create(user = user)
        education.school_name = school_name
        education.school_grade = school_grade
        education.school_passed_year = school_passed_year
        education.collage_name = collage_name
        education.collage_grade = collage_grade
        education.collage_passed_year = collage_passed_year
        education.save()

        skill, created = Skill.objects.get_or_create(user = user)
        skill.skill_name = skill_name
        skill.save()

        experience, created = Experience.objects.get_or_create(user = user)
        experience.company_name = company_name
        experience.position = position
        experience.duration = duration
        experience.save()
        
        messages.success(request, "Profile updated successfully")
        return redirect("update")

    return render(request, 'home/update.html')

    # if request.method == "POST":
    #     user_id = request.POST.get('u_id')
    #     user = CustomUser.objects.get(id=user_id)

    #     # Update user fields
    #     user.first_name = request.POST['first_name']
    #     user.last_name = request.POST['last_name']
    #     user.contact = request.POST['contact']
    #     user.address = request.POST['address']
    #     user.dob = request.POST['dob']
    #     user.summary = request.POST['summary']
    #     user.link = request.POST['link']
    #     if 'profile' in request.FILES:
    #         user.profile_pic = request.FILES['profile']
    #     if request.POST['password']:
    #         user.password = make_password(request.POST['password'])
    #     user.save()

    #     # Update skills
    #     Skill.objects.filter(user=user)
    #     skills = request.POST.getlist('skill_name')
    #     for skill_name in skills:
    #         if skill_name.strip(','):
    #             Skill.objects.update(user=user, skill_name=skill_name)

    #     # Update experiences
    #     Experience.objects.filter(user=user)
    #     company_names = request.POST.getlist('company_name')
    #     positions = request.POST.getlist('position')
    #     durations = request.POST.getlist('duration')
    #     for company_name, position, duration in zip(company_names, positions, durations):
    #         if company_name.strip() and position.strip() and duration.strip():
    #             Experience.objects.update(user=user, company_name=company_name, position=position, duration=duration)

    #     # Update education
    #     Education.objects.filter(user=user)
    #     school_names = request.POST.getlist('school_name')
    #     school_grades = request.POST.getlist('school_grade')
    #     school_passed_years = request.POST.getlist('school_passed_year')
    #     collage_names = request.POST.getlist('collage_name')
    #     collage_grades = request.POST.getlist('collage_grade')
    #     collage_passed_years = request.POST.getlist('collage_passed_year')
    #     for school_name, school_grade, school_passed_year, collage_name, collage_grade, collage_passed_year in zip(
    #             school_names, school_grades, school_passed_years, collage_names, collage_grades, collage_passed_years):
    #         if school_name.strip() and school_grade.strip() and school_passed_year.strip():
    #             Education.objects.update(user=user, school_name=school_name, school_grade=school_grade,
    #                                      school_passed_year=school_passed_year, collage_name=collage_name,
    #                                      collage_grade=collage_grade, collage_passed_year=collage_passed_year)

    #     return redirect('update')  # Redirect to a success page after submission

    # return render(request, 'update_profile.html', {'user': request.user})

def sample1(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {
        'user': user,
    }
    return render(request, 'home/sample1.html', context)

def sample2(request):
    return render(request, 'home/sample2.html')

def sample3(request):
    return render(request, 'home/sample3.html')


from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import get_template


def download(request):
    user = CustomUser.objects.get(id = request.user.id)
    template_path = 'home/sample1.html'
    context = {
        'user':user,
        'user.profile_pic.url':user.profile_pic.url,
    }
    response = HttpResponse(content_type = 'application/pdf')
    response['content-Disposition'] = 'filename = "Sample.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response
    )
    if pisa_status.err:
        return HttpResponse('We had a problem.')
    return response