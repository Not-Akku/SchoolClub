from django.shortcuts import render

# Create your views here.
#=============================================================
# This is the view for the Home page of the website.
#=============================================================

def home (request):
    
    return render(request, "webpage/home.html")

#=============================================================
# This is the view for the Events page of the website.
#=============================================================

def events (request):
    programs = [
        {
            "name": "Coding Workshop",
            "date": "2024-07-15",
            "description": "Learn the basics of coding in Python.",
        },
        {
            "name": "Robotics Competition",
            "date": "2024-08-20",
            "description": "Compete with your own robot design.",
        },
        {
            "name": "Tech Talk: AI and the Future",
            "date": "2024-09-10",
            "description": "Join us for a discussion on artificial intelligence and its impact on our future.",
        },
    ]

    context = {
        "events": programs,
    }

    return render(request, "webpage/event.html", context)