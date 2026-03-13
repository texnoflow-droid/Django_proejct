from django.http import HttpResponse

def spare_parts_list(request):
    return HttpResponse("<div style='border: 1px solid #ccc; padding: 10px;'><h1>Ehtiyot qismlar ro'yxati</h1></div>")

def spare_parts_info(request):
    return HttpResponse("<div style='border: 1px solid #ccc; padding: 10px;'><h1>Ehtiyot qismlar haqida ma'lumot</h1></div>")