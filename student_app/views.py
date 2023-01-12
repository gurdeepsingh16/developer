from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from student_app.models import Student_profile, student_question, Comment
from django.contrib import messages


# Create your views here.


def student_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(
                    request, "USER NAME IS ALREADY EXISTS PLEASE TRY AGAIN")
                return redirect('student_register')
            if User.objects.filter(email=email).exists():
                messages.info(
                    request, "EMAIL IS ALREADY EXISTS PLEASE TRY AGAIN")
                return redirect('student_register')

            data = User.objects.create_user(
                username=username, email=email, password=password)
            data.save()
            return redirect('/')

    return render(request, 'register.html')


def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def profile(request):
    user = request.user
    data = Student_profile.objects.filter(username__exact=user).values('first_name')
    if data:
        student_q = student_question.objects.filter(upload_by__exact=user)
        data2 = Student_profile.objects.filter(
            username__exact=user).values()
        return render(request, 'profile2.html', {'data': data2, 'student_data': student_q})
    else:
        if request.method == "POST":
            username = request.user
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            image = request.FILES['image']
            email = request.POST['email']

            data = Student_profile(
                username=username, first_name=firstname, profile_pic=image, last_name=lastname, email=email)
            data.save()
            return redirect('profile')
        return render(request, 'student_profile.html')


def stushow(request):
    data = student_question.objects.all()
    
    return render(request, 'student_show.html', {'data': data})


def stuadd(request):
    if request.method == "POST":
        question = request.POST['question']
        program = request.POST['program']
        upload_by = request.user

        data = student_question(
            question=question, Program=program, upload_by=upload_by)
        data.save()
        return redirect('stushow')

    return render(request, 'student_add_data.html')


def delete(request, id):
    data = student_question.objects.get(id=id)
    data.delete()
    return redirect('profile')


def delete_comment(request, id):
    data2 = Comment.objects.get(id=id)
    data2.delete()
    # return redirect('stushow');
    return redirect('stushow')


def update(request, id):
    data = student_question.objects.get(id=id)
    try:
        if request.method == "POST":
            question = request.POST['question']
            program = request.POST['program']
            upload_by = request.user

            data = student_question(
                id=id, question=question, Program=program, upload_by=upload_by)
            data.save()
            return redirect('stushow')
    except Exception as e:
        return e

    return render(request, 'student_update_data.html', {'data': data})


def comment_func(request):
    # data = student_question.objects.get(id=id)
    if request.method == "POST":
        comment = request.POST['comment']
        ques = request.POST['ques']
        data = Comment(question=ques, user=request.user, comment=comment)
        data.save()
        return redirect('stushow')
    else:
        data = Comment.objects.all()
        return render(request, 'student_show.html',)


def show_comment(request, id):
    data = student_question.objects.get(id=id)
    comment = Comment.objects.filter(question__exact=data)
    return render(request, 'show_comment.html', {'comment': comment})
