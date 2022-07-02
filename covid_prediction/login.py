from django.shortcuts import render
from . import pool
from django.http import JsonResponse


def LogIn(request):
    return render(request,'login.html',{'msg':''})

def CheckLogin(request):
    try:
        db,cmd=pool.ConnectionPooling()
        email=request.POST['email']
        print(email)
        password=request.POST['password']
        print(password)
        q = "select * from register where emailid='{0}' and password='{1}'  ".format(email,password)
        cmd.execute(q)
        records = cmd.fetchone()
        print(records)
        if(records):
         return render(request, 'predictCovid.html', {'msg': "", 'result':records})
        else:
         return render(request, 'login.html', {'msg': "Invalid EmailId/Password"})

    except Exception as e:
        print(e)
        return render(request, 'login.html', {'msg': 'Server Error'})


