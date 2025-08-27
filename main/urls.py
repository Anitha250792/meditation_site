
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("index/", views.index, name="index"),
    path("therapy/", views.therapy, name="therapy"),
    path("family-therapy/", views.family_therapy, name="family_therapy"),
    path("about/", views.about, name="about"),
    path("meditation/", views.meditation, name="meditation"),
    path("contact/", views.contact_view, name="contact"),
    path("course/", views.course, name="course"),
    path("happiness/", views.happiness, name="happiness"),
    path("approach/", views.approach_form_view, name="approach"),
    path('free-trial/', views.free_trial_view, name='free_trial'),
    path("payment/", views.payment_view, name="payment"),
    path("success/", views.success_view, name="success"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),

]