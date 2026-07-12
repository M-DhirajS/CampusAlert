from django.shortcuts import render, redirect
from mongodb import users, db

def home(request):
    return render(request, "home.html")

def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = users.find_one({
            "email": email,
            "password": password
        })

        if user:
            request.session["email"] = email
            return redirect("/dashboard/")
        else:
            return render(request, "login.html", {
                "error": "Invalid Email or Password"
            })

    return render(request, "login.html")

def register(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        users.insert_one({
            "name": name,
            "email": email,
            "phone": phone,
            "password": password
        })

        return redirect("/login/")

    return render(request, "register.html")

def dashboard(request):
    return render(request, "dashboard.html")

def admin_login(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if email == "admin@gmail.com" and password == "admin123":
            return redirect("/admin-dashboard/")
        else:
            return render(request, "admin_login.html", {
                "error": "Invalid Admin Credentials"
            })

    return render(request, "admin_login.html")
    
def alerts_page(request):

    alerts = db["alerts"].find()

    return render(request, "alerts.html", {
        "alerts": alerts
    })

def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

def create_alert(request):

    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")
        priority = request.POST.get("priority")
        alert_type = request.POST.get("alert_type")
        date = request.POST.get("date")
        time = request.POST.get("time")

        alerts = db["alerts"]

        alerts.insert_one({
            "title": title,
            "description": description,
            "priority": priority,
            "type": alert_type,
            "date": date,
            "time": time
        })

        return redirect("/alerts/")

    return render(request, "create_alert.html")

def history(request):

    alerts = db["alerts"].find()

    return render(request, "history.html", {
        "alerts": alerts
    })

def profile(request):
    email = request.session.get("email")

    student = users.find_one({"email": email})

    return render(request, "profile.html", {
        "student": student
    })