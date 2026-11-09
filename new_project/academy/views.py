from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .catalog import COURSES
from .forms import InquiryForm


def home(request):
    return render(request, "academy/home.html", {"courses": COURSES[:3]})


def course_list(request):
    return render(request, "academy/courses.html", {"courses": COURSES})


def course_detail(request, slug):
    course = next((item for item in COURSES if item["slug"] == slug), None)
    if course is None:
        raise Http404("Course not found")
    return render(request, "academy/course_detail.html", {"course": course})


def contact(request):
    initial = {}
    selected_course = request.GET.get("course", "")
    if selected_course in {course["title"] for course in COURSES}:
        initial["course"] = selected_course

    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out! Our learning team will be in touch soon.")
            return redirect("contact")
    else:
        form = InquiryForm(initial=initial)

    return render(request, "academy/contact.html", {"form": form})
