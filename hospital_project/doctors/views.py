from django.http import HttpResponse

def doctor_list(request):
    return HttpResponse("<h1 style='color: white; background-color: blue; padding: 20px;'>Shifokorlar ro'yxati</h1>")

def doctor_info(request):
    return HttpResponse("<h1 style='color: blue; border: 2px solid blue; padding: 10px;'>Shifokor haqida ma'lumot</h1>")