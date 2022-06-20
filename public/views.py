from django.shortcuts import render
from django.http import HttpResponse
from admins.models import FamilyMember, Services, VolunteerRating
from Volunteers.models import VolunteerRegistrationModel


# Create your views here.
def publicHome(request):
    return render(request, 'public/publichome.html')


def publicsideFamilyDetails(request):
    if request.method == 'POST':
        mobileNo = request.POST.get('mobileNo')
        aadharNo = request.POST.get('aadharNo')
        rationNo = request.POST.get('rationNo')
        if mobileNo != None:
            try:
                familyDetails = FamilyMember.objects.filter(mobileNo=mobileNo)

                volunteerId = familyDetails.first().volunteer_id
                volunteerDetails = VolunteerRegistrationModel.objects.get(
                    id=volunteerId)
                if familyDetails:
                    return render(request, 'public/familyDetails.html', {'familyDetails': familyDetails, 'volunteerDetails': volunteerDetails})
                else:

                    return render(request, 'public/publichome.html', {'msg': 'No Details Found'})
            except Exception as e:
                print('exception', e)
                return render(request, 'public/publichome.html', {'msg': e})
        elif aadharNo != None:
            try:
                familyDetails = FamilyMember.objects.filter(aadharNo=aadharNo)
                if familyDetails:
                    return render(request, 'public/familyDetails.html', {'familyDetails': familyDetails})
                else:

                    return render(request, 'public/publichome.html', {'msg': 'No Details Found'})
            except Exception as e:
                print('exception', e)
                return render(request, 'public/publichome.html', {'msg': e})
        elif rationNo != None:
            try:
                familyDetails = FamilyMember.objects.filter(rationNo=rationNo)
                if familyDetails:
                    return render(request, 'public/familyDetails.html', {'familyDetails': familyDetails})
                else:

                    return render(request, 'public/publichome.html', {'msg': 'No Details Found'})
            except Exception as e:
                print('exception', e)
                return render(request, 'public/publichome.html', {'msg': e})
    else:
        return render(request, 'public/publichome.html', {'msg': 'No Details Found'})


def memberRecentActivity(request):
    memberId = request.GET.get('memberId')
    memberDetails = FamilyMember.objects.get(id=memberId)
    memberRecentActivity = Services.objects.filter(
        aadharNo=memberDetails.aadharNo)
    return render(request, 'public/familyDetails.html', {'memberRecentActivities': memberRecentActivity})


def submitRating(request):
    if request.method == 'POST':
        rating = request.POST.get('rate')
        volunteerLoginId = request.POST.get('volunteerLoginId')
        VolunteerRating = VolunteerRating(
            volunteer=volunteerLoginId, rating=rating)
        VolunteerRating.save()
    return render(request, 'public/publichome.html')
