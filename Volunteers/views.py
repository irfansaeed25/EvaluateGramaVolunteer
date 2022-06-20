from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .forms import VolunteerRegistrationForm
from .models import VolunteerRegistrationModel
from admins.models import FamilyMember
from admins.models import Services


# Create your views here.
def VolunteerRegisterActions(request):
    form = VolunteerRegistrationForm()
    if request.method == 'POST':
        form = VolunteerRegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = VolunteerRegistrationForm()
            return render(request, 'VolunteerRegister.html', {'form': form})
        else:
            messages.success(
                request, 'Email or Mobile or LoginId Already Existed')
            print("Invalid form")
    else:
        form = VolunteerRegistrationForm()
    return render(request, 'VolunteerRegister.html', {'form': form})


def VolunteerLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = VolunteerRegistrationModel.objects.get(
                loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == True:
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email

                print("User id At", check.id, status)
                return render(request, 'Volunteer/VolunteerHome.html')
            else:
                messages.error(request, 'Your Account Not at activated')
                return render(request, 'VolunteerLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'VolunteerLogin.html', {})


def VolunteerHome(request):
    return render(request, 'Volunteer/VolunteerHome.html', {})


def familyDetails(request):
    if request.method == 'POST':
        mobileNo = request.POST.get('mobileNo')
        aadharNo = request.POST.get('aadharNo')
        rationNo = request.POST.get('rationNo')
        if mobileNo != None:
            try:
                familyDetails = FamilyMember.objects.filter(mobileNo=mobileNo)
                print(familyDetails)
                if familyDetails:
                    return render(request, 'Volunteer/familyDetails.html', {'familyDetails': familyDetails})
                else:

                    return render(request, 'Volunteer/VolunteerHome.html', {'msg': 'No Details Found'})
            except Exception as e:
                print('exception', e)
                return render(request, 'Volunteer/VolunteerHome.html', {'msg': e})
        elif aadharNo != None:
            try:
                familyDetails = FamilyMember.objects.filter(aadharNo=aadharNo)
                if familyDetails:
                    return render(request, 'Volunteer/familyDetails.html', {'familyDetails': familyDetails})
                else:

                    return render(request, 'Volunteer/VolunteerHome.html', {'msg': 'No Details Found'})
            except Exception as e:
                print('exception', e)
                return render(request, 'Volunteer/VolunteerHome.html', {'msg': e})
        elif rationNo != None:
            try:
                familyDetails = FamilyMember.objects.filter(rationNo=rationNo)
                if familyDetails:
                    return render(request, 'Volunteer/familyDetails.html', {'familyDetails': familyDetails})
                else:

                    return render(request, 'Volunteer/VolunteerHome.html', {'msg': 'No Details Found'})
            except Exception as e:
                print('exception', e)
                return render(request, 'Volunteer/VolunteerHome.html', {'msg': e})
    else:
        return render(request, 'Volunteer/VolunteerHome.html', {'msg': 'No Details Found'})


def viewMember(request):
    memberId = request.GET.get('memberId')
    memberDetails = FamilyMember.objects.get(id=memberId)
    return render(request, 'Volunteer/familyDetails.html', {'memberDetails': memberDetails})


def services(request):
    servicesId = request.GET.get('memberServices')
    memberDetails = FamilyMember.objects.get(id=servicesId)
    return render(request, 'Volunteer/services.html', {'memberDetails': memberDetails})


def submitServices(request):
    memberDetailsId = request.POST.get('memberDetailsId')
    scheme1 = request.POST.get('scheme1')
    scheme2 = request.POST.get('scheme2')
    scheme3 = request.POST.get('scheme3')
    scheme4 = request.POST.get('scheme4')
    scheme5 = request.POST.get('scheme5')
    schemes_list = [scheme1, scheme2, scheme3, scheme4, scheme5]
    if all(scheme == None for scheme in schemes_list):
        msg = 'Select atleast one service'
        return render(request, 'Volunteer/services.html', {'msg1': msg})
    else:
        # schemes = [scheme for scheme in schemes_list if scheme]
        schemes = list(filter(None, schemes_list))
        memberDetails = FamilyMember.objects.get(id=memberDetailsId)
        submitService = Services(mobileNo=memberDetails.mobileNo,
                                 aadharNo=memberDetails.aadharNo,
                                 name=memberDetails.name,
                                 serviceSelected=schemes
                                 )
        submitService.save()
        return render(request, 'Volunteer/services.html', {'msg2': 'Request Submitted'})
    return HttpResponse('success')
