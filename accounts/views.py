from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.

def user_login(request):
    if request.method=="POST": #Agar request methodi post methodiga teng bo'lsa
        form=LoginForm(request.POST)
        if form.is_valid(): #Agar forma valid( yaroqli bo'lsa)
            data=form.cleaned_data # Ya'ni yuborilgan ma'lumotni data deb olyabmzi
            print(data)
            user=authenticate(request,
                              username=data['username'],
                              password=data['password']) # User agar bor bo'lsa authenticate qidiradi
            print(user)
            if user is not None: # Agar bizda bor bo'ladigan bo'lsa
                if user.is_active: #Agar user bizda avtive bo'lsa To'g'ri bo'lsa
                    login(request, user) #User login qilinadi
                    return HttpResponse("Muvaffaqiyatli login amalga oshirildi") # Hamda HttpResponse qaytaradi

                else:
                    return HttpResponse("Sizning profilingiz faol holatda emas")

            else:
                return HttpResponse("Login va parolda xatolik bor!")
    else:
        form=LoginForm()
        context={
            "form":form
        }
    return render(request, 'registration/login.html', context=context)


def dashboard_view(request):
    user=request.user
    context={
        "user":user
    }
    return render(request,'pages/user_profile.html', context=context)

