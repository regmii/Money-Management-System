from django.shortcuts import redirect, render, HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.views import View
from .models import *
from .forms import *
# Create your views here.

class DepositListView(View):
    def get(self, request):
        person_detail = PersonDetail.objects.all()
        deposit_detail = Deposits.objects.all()
        context = {
            'person_detail':person_detail,
            'deposit_detail':deposit_detail,

        }
        return render(request, 'deposit/deposit-list-view.html', context=context)

class NewDeposit(View):
    def get(self, request):
        form = DepositCreateForm
        context = {
            'form': form,

            }
        return render(request, 'deposit/new-deposit.html', context)
    
    def post(self, request, *args, **kwargs):
        form = DepositCreateForm(request.POST)
        if form.is_valid():
            print('-----------here pass')
            form.save()
            return redirect('/deposit/new/')
        else:
            print('-----------here fail')
            # print(form)
        # return redirect('deposit:deposit-list')
            
class NewPersonCreate(View):
    def get(self, request):
        form = PersonCreateForm
        context = {'form': form}
        return render(request, 'deposit/new-person.html', context=context) 
    
    def post(self, request):
        form = PersonCreateForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('/abc')

def person_ajax(request):
    name = request.GET.get('name')
    try:
        nam = PersonDetail.objects.get(name=name)
        nm = {
            'name':name,
        }
        return JsonResponse(nm)
    except:
        return JsonResponse({'name':None})
        
    