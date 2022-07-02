from django.shortcuts import render
from . import pool
from django.http import JsonResponse


def Register(request):
    return render(request,'Register.html',{'msg':''})

def RegisterInsert(request):
    try:
        db,cmd=pool.ConnectionPooling()
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        email=request.POST['email']
        mobileNo=request.POST['mobileNo']
        address=request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        gender=request.POST['Gender']
        password=request.POST['password']
        q = "insert into register(FirstName,LastName,emailid, mobileNo, address ,city, state, gender,password) values('{0}','{1}','{2}',{3},'{4}','{5}','{6}','{7}','{8}')".format(FirstName,LastName ,email, mobileNo, address,city,state, gender,password)

        cmd.execute(q)
        print(q)
        cmd.execute(q)
        db.commit()
        return render(request, "register.html", {'msg': 'Record Submitted'})

    except Exception as e:
        print(e)
        return render(request, "register.html", {'msg': 'Fail to submitted'})