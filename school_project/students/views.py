from django.http import HttpResponse

def student_list(request):
    return HttpResponse("<div><h1>O'quvchilar ro'yxati </h1> <br> <input type='text' placeholder='Sarching...'> <div/>" )

def student_info(request):
    return HttpResponse("<h1 style='color: red; background-color: yellow;border-radius: 10px; padding: 10px;'>O'quvchi haqida batafsil ma'lumot</h1>")