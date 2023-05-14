from django.shortcuts import render


def calculator(request):
    return render(request,"calculator.html")

def data(request):
    n1=str(request.POST.get('result'))
    ans=eval(n1)
    print(ans)
    ansdict={
        'ans':ans
    }
    return render(request,"calculator.html",ansdict)