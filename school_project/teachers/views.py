from django.http import HttpResponse

def teacher_list(request):
    return HttpResponse("<h1 style='color: blue; background-color: lightgray; border-radius: 10px; padding: 10px;'>O'qituvchilar ro'yxati</h1>")

def teacher_detail(request):
    return HttpResponse("<h1 style='color: green; background-color: lightyellow; border-radius: 10px; padding: 10px;'>O'qituvchi ma'lumotlari</h1>")