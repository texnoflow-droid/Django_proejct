from django.http import HttpResponse

def patient_list(request):
    return HttpResponse("<h1 style='color: white; background-color: green; padding: 20px;'>Bemorlar ro'yxati</h1>")

def patient_report(request):
    return HttpResponse("<h1 style='color: green; border: 2px dashed green; padding: 10px;'>Bemorning kasallik varaqasi</h1>")