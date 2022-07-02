from django.shortcuts import render
from . import pool
import joblib
import pandas as pd
reloadmodel = joblib.load('./model/logisticReg.pkl')
def PredictCovid(request):
    return render(request,'predictCovid.html',{'msg':''})

def preCovid (request):
    if request.method == "POST":
        temp={}
        temp['fever']=request.POST.get('fever')
        temp['bodypain']=request.POST.get('bodypain')
        temp['age']=request.POST.get('age')
        temp['runnyNose']=request.POST.get('runnyNose')
        temp['diffBreath']=request.POST.get('breathrate')
        testdata=pd.DataFrame({'x':temp}).transpose()
        scoreVal = reloadmodel.predict_proba(testdata.values)[:,1]
        scoreVal = str(scoreVal * 100)
        score = str(scoreVal)
        print(score)
        context = {'scoreval':score}
        return render(request, 'predictCovid.html', context)

def submitCovid(request):
    pass


