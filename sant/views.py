from django.shortcuts import render,redirect,HttpResponseRedirect
from . import forms,models
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate ,login,logout,update_session_auth_hash
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from django.db.models import Q
import os
from django.contrib.auth.models import auth, User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def sant_login(request):
        if request.method == "POST":
            fm=forms.LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return redirect('AfterLogin')
        else:
            fm=forms.LoginForm()
        return render(request, 'form.html', {'form': fm})

def AfterLogin(request):
    if request.user.is_superuser == True:
        return redirect('dashboard')

def sant_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def santkrupa_invoice(request,id):
    if request.user.is_authenticated:
        data = models.customers.objects.all()
        if request.method == "POST":
            lenth =  request.POST['totallength']
            billno =  request.POST['billno']
            cname = request.POST['company_name']
            address = request.POST['company-address']
            city = request.POST['company-city']
            state = request.POST['company-state']
            gst = request.POST['company-gst']
            date = request.POST['dated']
            word = request.POST['textword']
            total = request.POST['total']
            
            laborer = request.POST['laborer']
            lvno = request.POST['vhno']
            ltrip = request.POST['ltrip']
            lrate = request.POST['lrate']
            lamount = request.POST['frate']
            if id == 1:
                cgst = request.POST['cgst']
                sgst = request.POST['sgst']
                tgst = request.POST['tgst']
                cgst_amount = request.POST['cgst-amount']
                sgst_amount = request.POST['sgst-amount']
                tgst_amount = request.POST['tgst-amount']
                grand_total = request.POST['grand-total']

                data = models.report(bill_no=billno,company=cname,address=address,city=city,state=state,
                gst=gst,date=date,total_amount=total,cgst=cgst,sgst=sgst,tgst=tgst,cgst_amount=cgst_amount,
                sgst_amount=sgst_amount,tgst_amount=tgst_amount,grand_total=grand_total,word_total=word,
                laborer=laborer,lvno=lvno,ltrip=ltrip,lrate=lrate,lamount=lamount,invoice_type=id
                )
                data.save()
            elif id == 2:
                data = models.report(bill_no=billno,company=cname,address=address,city=city,state=state,
                gst=gst,date=date,total_amount=total,word_total=word,
                laborer=laborer,lvno=lvno,ltrip=ltrip,lrate=lrate,lamount=lamount,invoice_type=id
                )
                data.save()
            i = 0
            for index in range(i,int(lenth)):
                formc =""
                toc =""
                vehical =""
                trip =""
                rate =""
                famount =""
                flag=0
                if 'po_number'+str(index) in request.POST:
                    formc= request.POST['po_number'+str(index)]
                    flag = 1
                if 'jc_number'+str(index) in request.POST:
                    toc= request.POST['jc_number'+str(index)]
                    flag = 1
                if 'weight'+str(index) in request.POST:
                    vehical= request.POST['weight'+str(index)]
                    flag = 1
                if 'quantity'+str(index) in request.POST:
                    trip= request.POST['quantity'+str(index)]
                    flag = 1
                if 'amount'+str(index) in request.POST:
                    rate= request.POST['amount'+str(index)]
                    flag = 1
                if 'famount'+str(index) in request.POST:
                    famount= request.POST['famount'+str(index)]
                    flag = 1
                if flag == 1: 
                    trip = models.trip(from_company=formc,to_company=toc,vehical=vehical,trip=trip,rate=rate,amount=famount)              
                    trip.save()
                    trip.Report.add(data)
                    messages.success(request, 'Print Invoice')
        data = models.customers.objects.all()
       
        return render(request,'santkrupa_invoice.html',{'data':data,'id':id})
    else:
        return redirect('login')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'Dashboard.html')
    else:
        return redirect('login')


def addcustomer(request):
    if request.user.is_authenticated:
        data = models.customers.objects.all()
        fm=forms.AddcustomerForm()
        if request.method == 'POST':
            fm=forms.AddcustomerForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Data added successfully...!!!')
                fm=forms.AddcustomerForm()
        else:
            fm=forms.AddcustomerForm()

        return render(request,'AddCustomer.html',{'form':fm,'data':data})
    else:
        return redirect('login')

def loaddata(request):
    if request.user.is_authenticated:
        d_id = request.GET.get('cid')
        d = models.customers.objects.filter(company_name=d_id)
        return render(request, 'loaddata.html',{'i':d})
    else:
        return redirect('login')


# ======================================================================
# ============================invoice Pdf=============================
# ======================================================================


import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse




def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return



def download_pdf_view(request):
    data=models.report.objects.all().last()
    data1 = models.trip.objects.filter(Report=data.id)
    dict={
        'data':data,
        'data1':data1
    }
    return render_to_pdf('generate_santkrupa.html',dict)
    



# ==========================================================================
# ============================invoice Pdf end=============================
# ==========================================================================


def pdf_view(request):
    data=models.report.objects.all().last()
    data1 = models.trip.objects.filter(Report=data.id)
    dict={
        'data':data,
        'data1':data1
    }
    return render(request, 'generate_invoice.html',dict)


def santkrupa_list(request,id):
    if request.user.is_authenticated:
        data=models.report.objects.order_by('-id')
        return render(request, 'santkrupa_invoice_list.html',{'data':data,'id':id})
    else:
        return redirect('login')

def santkrupa_list_view(request,id):
    if request.user.is_authenticated:
        data=models.report.objects.get(pk=id)
        data1 = models.trip.objects.filter(Report=data.id)
        dict={
        'data':data,
        'data1':data1
    }
        return render_to_pdf('generate_santkrupa.html',dict)
    else:
        return redirect('login')

def delete_customer(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi=models.customers.objects.get(pk=id)
            pi.delete()
            return redirect(addcustomer)

    else:
        return redirect('login')

def santkrupa_delete(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi=models.report.objects.get(pk=id)
            x = models.trip.objects.filter(Report=pi.id)
            x.delete()
            pi.delete()
            return redirect('santkrupa_list')

    else:
        return redirect('login')