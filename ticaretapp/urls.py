from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "ticaretapp"

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('case/',views.casepage,name='casepage'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('kalem/',views.kalem,name='kalem'),
    path('case/kalem/',views.casepagekalem,name='casepagekalem'),
    path('kalemtıraş/',views.kalemtıraş,name='kalemtıraş'),
    path('case/kalemtıraş/',views.casepagekalemtıraş,name='casepagekalemtıraş'),
    path('tükenmez/',views.tükenmez,name='tükenmez'),
    path('case/tükenmez/',views.casepagetükenmez,name='casepagetükenmez'),
    path('bilgisayar',views.bilgisayar,name='bilgisayar'),
    path('case/bilgisayar/',views.casepagebilgisayar,name='casepagebilgisayar'),
    path('telefon/',views.telefon,name='telefon'),
    path('case/telefon/',views.casepagetelefon,name='casepagetelefon'),
    path('saat/',views.saat,name='saat'),
    path('case/saat/',views.casepagesaat,name='casepagesaat'),
    path('araba/',views.araba,name='araba'),
    path('case/araba',views.casepagearaba,name='casepagearaba'),
    path('bebek/',views.bebek,name='bebek'),
    path('case/bebek/',views.casepagebebek,name='casepagebebek'),
    path('top',views.top,name='top'),
    path('case/top/',views.casepagetop,name='casepagetop'),
    path('çamaşır/',views.çamaşır,name='çamaşır'),
    path('case/çamaşır/',views.casepageçamaşır,name='casepageçamaşır'),
    path('deterjan/',views.deterjan,name='deterjan'),
    path('case/deterjan/',views.casepagedeterjan,name='casepagedeterjan'),
    path('havlu/',views.havlu,name='havlu'),
    path('case/havlu/',views.casepagehavlu,name='casepagehavlu'),
    path('kola/',views.kola,name='kola'),
    path('case/kola/',views.casepagekola,name='casepagekola'),
    path('limonata/',views.limonata,name='limonata'),
    path('case/limonata/',views.casepagelimonata,name='casepagelimonata'),
    path('su/',views.su,name='su'),
    path('case/su/',views.casepagesu,name='casepagesu'),
    path('şampuan/',views.şampuan,name='şampuan'),
    path('case/şampuan/',views.casepageşampuan,name='casepageşampuan'),
    path('sabun/',views.sabun,name='sabun'),
    path('case/sabun/',views.casepagesabun,name='casepagesabun'),
    path('parfüm/',views.parfüm,name='parfüm'),
    path('case/parfüm/',views.casepageparfüm,name='casepageparfüm')
]
