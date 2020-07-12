from django.shortcuts import render
from .models import *
import collections

# Create your views here.

def get_Com_numbrt():       #返回每个公司及申请数量：按数量排序
    list_all = ChartInfo.objects.all()
    list_comp_all = []
    for i in list_all:
        list_comp_all.append((i.PA))
    Counter_comp = collections.Counter(list_comp_all)
    dict_comp = dict(Counter_comp)
    list_1 = sorted(dict_comp.items(), key=lambda x: x[1], reverse=True)
    return list_1
def chart(request):            #返回数量排名前8的公司及数量
    list_comp=[]
    list_comp_freq=[]
    list_1=get_Com_numbrt()
    for i in range(0,8):
        list_comp.append(list_1[i][0])
        list_comp_freq.append(list_1[i][1])
    return render(request,'chart.html',{'list_comp':list_comp,'list_comp_freq':list_comp_freq})