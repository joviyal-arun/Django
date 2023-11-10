from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from django.shortcuts import redirect
from django.urls import reverse


def home_page(request):
    return render(request,'home_page.html')

def sign_in(request):
    return render(request,'sign_in.html')

def log_in(request):
    return render(request,'log_in.html')



def sign_details(request):

    output_dictionary={}

    if request.method=='POST':

        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        mobile_number=request.POST.get('mobilenumber')
        email=request.POST.get('email')
        psw=request.POST.get('psw')

        output_dictionary['first_name']=first_name
        output_dictionary['last_name']=last_name
        output_dictionary['mobile_number']=mobile_number
        output_dictionary['email']=email
        output_dictionary['psw']=psw
        output_dictionary['main_balance']=1000

        df=pd.DataFrame(output_dictionary, index=[0])
        df.to_csv('sign_details.csv',index=False)

        return render(request,'home_page.html')


def log_in_details(request):

    if request.method=='POST':
        mobile_number=request.POST.get('mobilenumber')
        psw=str(request.POST.get('psw'))

        df=pd.read_csv('sign_details.csv')
        sign_password=str(df['psw'][0])

        if psw==sign_password:
            return render(request,'services.html')
        else:
            return redirect(reverse('log_in_details'))

def profile(request):
    
    df=pd.read_csv('sign_details.csv')
    first_name=df['first_name'][0]
    last_name=df['last_name'][0]
    full_name=first_name+' '+last_name
    mail_id=df['email'][0]
    mobile_number=df['mobile_number'][0]
    main_balance=df['main_balance'][0]

    context = {
        'name': full_name,
        'mail_id': mail_id,
        'mobile_number': mobile_number,
        'balance': main_balance,}

    return render(request,'profile.html',context)


def with_draw(request):
    return render(request,'amount_withdraw.html')


def amount_with_draw_details(request):
    
    if request.method=='POST':
        with_draw_amount=int(request.POST.get('with_draw_amount'))
        df=pd.read_csv('sign_details.csv')
        main_balance=df['main_balance'][0]
        sub_operation=main_balance-with_draw_amount
        df['main_balance']=sub_operation
        df.to_csv('sign_details.csv',index=False)
        context={'with_draw_amount':with_draw_amount,'balance':sub_operation}

        return render(request,'display_with_draw_amount.html',context)

def deposit(request):
    return render(request,'amount_deposit.html')

def amount_deposit_details(request):
    if request.method=='POST':
        deposit_amount=int(request.POST.get('deposit_amount'))
        df=pd.read_csv('sign_details.csv')
        main_balance=df['main_balance'][0]
        addition_operation=main_balance+deposit_amount
        df['main_balance']=addition_operation
        df.to_csv('sign_details.csv',index=False)
        context={'deposit_amount':deposit_amount,'balance':addition_operation}
        return render(request,'display_deposit_amount.html',context)

def balance(request):
    df=pd.read_csv('sign_details.csv')
    main_balance=df['main_balance'][0]
    context={'main_balance':main_balance}
    return render(request,'balance.html',context)


def service_parameters(request):

    if request.method=='POST':
        service=request.POST.get('radio')
        if service=='Profile':
            return redirect(reverse('profile'))
        elif service=='Withdraw':
            return redirect(reverse('with_draw'))
        elif service=='Deposit':
            return redirect(reverse('deposit'))
        elif service=='Exit':
            return redirect(reverse('log_in_details'))
        elif service=='Balance':
            return redirect(reverse('balance'))


    





















