from django.shortcuts import render , redirect
from . import models
from django.urls import reverse, reverse_lazy
from ticaretapp.forms import SignUpForm , SignUpModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView

# Create your views here.

def homepage(request):
    if request.method == "post":
        form = SignUpForm(request.post)
        if form.is_valid():
            username = form.cleaned_data["username_input"]
            models.Ticaret.objects.create(username=username)
            return redirect(reverse('ticaretapp:casepage'))
        else:
            print("error in form!")
            return render(request,'ticaretapp/homepage.html', context={"form":form})
    else:
        form = SignUpForm()
        return render(request,'ticaretapp/homepage.html', context={"form":form})

def casepage(request):
    return render(request,'ticaretapp/casepage.html')

@login_required(login_url="/login")
def kalem(request):
    return render(request,'ticaretapp/kalem.html')

@login_required(login_url="/login")
def casepagekalem(request):
    return render(request,'ticaretapp/casepagekalem.html')

@login_required(login_url="/login")
def kalemtıraş(request):
    return render(request,'ticaretapp/kalemtıraş.html')

@login_required(login_url="/login")
def casepagekalemtıraş(request):
    return render(request,'ticaretapp/casepagekalemtıraş.html')

@login_required(login_url="/login")
def tükenmez(request):
    return render(request,'ticaretapp/tükenmez.html')

@login_required(login_url="/login")
def casepagetükenmez(request):
    return render(request,'ticaretapp/casepagetükenmez.html')

@login_required(login_url="/login")
def bilgisayar(request):
    return render(request,'ticaretapp/bilgisayar.html')

@login_required(login_url="/login")
def casepagebilgisayar(request):
    return render(request,'ticaretapp/casepagebilgisayar.html')

@login_required(login_url="/login")
def telefon(request):
    return render(request,'ticaretapp/telefon.html')

@login_required(login_url="/login")
def casepagetelefon(request):
    return render(request,'ticaretapp/casepagetelefon.html')

@login_required(login_url="/login")
def saat(request):
    return render(request,'ticaretapp/saat.html')

@login_required(login_url="/login")
def casepagesaat(request):
    return render(request,'ticaretapp/casepagesaat.html')

@login_required(login_url="/login")
def araba(request):
    return render(request,'ticaretapp/araba.html')

@login_required(login_url="/login")
def casepagearaba(request):
    return render(request,'ticaretapp/casepagearaba.html')

@login_required(login_url="/login")
def bebek(request):
    return render(request,'ticaretapp/bebek.html')

@login_required(login_url="/login")
def casepagebebek(request):
    return render(request,'ticaretapp/casepagebebek.html')

@login_required(login_url="/login")
def top(request):
    return render(request,'ticaretapp/top.html')

@login_required(login_url="/login")
def casepagetop(request):
    return render(request,'ticaretapp/casepagetop.html')

@login_required(login_url="/login")
def çamaşır(request):
    return render(request,'ticaretapp/çamaşır.html')

@login_required(login_url="/login")
def casepageçamaşır(request):
    return render(request,'ticaretapp/casepageçamaşır.html')

@login_required(login_url="/login")
def deterjan(request):
    return render(request,'ticaretapp/deterjan.html')

@login_required(login_url="/login")
def casepagedeterjan(request):
    return render(request,'ticaretapp/casepagedeterjan.html')

@login_required(login_url="/login")
def havlu(request):
    return render(request,'ticaretapp/havlu.html')

@login_required(login_url="/login")
def casepagehavlu(request):
    return render(request,'ticaretapp/casepagehavlu.html')

@login_required(login_url="/login")
def kola(request):
    return render(request,'ticaretapp/kola.html')

@login_required(login_url="/login")
def casepagekola(request):
    return render(request,'ticaretapp/casepagekola.html')

@login_required(login_url="/login")
def limonata(request):
    return render(request,'ticaretapp/limonata.html')

@login_required(login_url="/login")
def casepagelimonata(request):
    return render(request,'ticaretapp/casepagelimonata.html')

@login_required(login_url="/login")
def su(request):
    return render(request,'ticaretapp/su.html')

@login_required(login_url="/login")
def casepagesu(request):
    return render(request,'ticaretapp/casepagesu.html')

@login_required(login_url="/login")
def şampuan(request):
    return render(request,'ticaretapp/şampuan.html')

@login_required(login_url="/login")
def casepageşampuan(request):
    return render(request,'ticaretapp/casepageşampuan.html')

@login_required(login_url="/login")
def sabun(request):
    return render(request,'ticaretapp/sabun.html')

@login_required(login_url="/login")
def casepagesabun(request):
    return render(request,'ticaretapp/casepagesabun.html')

@login_required(login_url="/login")
def parfüm(request):
    return render(request,'ticaretapp/parfüm.html')

@login_required(login_url="/login")
def casepageparfüm(request):
    return render(request,'ticaretapp/casepageparfüm.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
