from django.http import HttpResponse
def car_list(request):
    return HttpResponse("<h1>Avtomobillar royxati</h1> <ul><li>BMW</li><li>Mercedes</li><li>Audi</li></ul>")
def car_info(requaest):
    return HttpResponse("<div style='border: 1px solid #ccc; padding: 10px;'><h1>Avtomobillar haqida malumot</h1> <ul><li>BMW - Germaniya kompaniyasi</li><li>Mercedes - Germaniya kompaniyasi</li><li>Audi - Germaniya kompaniyasi</li></ul> </div>")