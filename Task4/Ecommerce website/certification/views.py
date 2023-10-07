from django.shortcuts import render, redirect
from .models import CertificateData
# Create your views here.

def certification(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST['user']
            relation = request.POST['relation']
            tagline = request.POST['tagline']
            resever = request.POST['resever']

            certificate = CertificateData(user = request.user, full_name = name, relation= relation, tag_line=tagline, resiver=resever)
            certificate.save()
       
            print("certificate data saved")

            return redirect('/certification/certificate')
        else:
            return render(request, "certification/input.html")
    else:
        return redirect("/login")
    
def certificate(request):
    if request.user.is_authenticated:
        certificate = CertificateData.objects.get(user = request.user)
        name = certificate.full_name
        relation = certificate.relation
        tagline = certificate.tag_line
        resever = certificate.resiver
        return render(request, "certification/certificate.html", context={
                                                                    "name" : name, 
                                                                    "relation" : relation, 
                                                                    "tagline" : tagline,
                                                                    "resever" : resever
                                                                })
    else:
        return redirect("/login")
