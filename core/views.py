from django.views.generic import TemplateView
from django.shortcuts import render
class PageView(TemplateView):
	template_name = 'page.html'

class PageOneView(TemplateView):
	template_name = 'page-1.html'

class PageTwoView(TemplateView):
	template_name = 'page-2.html'
	def get_context_data(self, *args, **kwargs):
		context = super(PageTwoView, self).get_context_data(*args, **kwargs)
		context['name'] = ''
		context['id'] = '1'
		return context

def add(request):
    try:
        val1=int(request.POST['num1'])
        val2 = int(request.POST['num2'])
        t=f(request)
        res=round(integrate(t,val1, val2),2)
        return render(request,'result.html',{'result' : res} )

    except:
        return render(request,'result.html',{'error' : 'Niepoprawne działanie!'} )

def integrate(function, a, b):
    i=10000
    dx = (b - a) / i
    integr = 0
    for x in range(i):
        x = x * dx + a
        integr += dx * eval(function)
    return integr

def f(request):
    val3 = request.POST['num3']
    return val3

def add2(request):
 try:
    A1 = int(request.POST['A1'])
    A2 = int(request.POST['A2'])
    A3 = int(request.POST['A3'])
    A4 = int(request.POST['A4'])
    A5 = int(request.POST['A5'])
    A6 = int(request.POST['A6'])
    A7 = int(request.POST['A7'])
    A8 = int(request.POST['A8'])
    A9 = int(request.POST['A9'])

    B1 = int(request.POST['B1'])
    B2 = int(request.POST['B2'])
    B3 = int(request.POST['B3'])
    # A = [[2, 1, 4], [6, 6, 14], [4, 14, 19]]
    # b = [1, 8, 25]
    # x = [0, 0, 0]

    A=[[A1,A2,A3], [A4,A5,A6], [A7,A8,A9]]
    b=[B1,B2,B3]
    x=[0,0,0]
    x=gauss(A,b)


    return render(request, 'result2.html', {'result2': x[0],'result3': x[1],'result4': x[2]})
 except:
     return render(request, 'result2.html', {'error': 'Niepoprawne działanie!'})




def POM(L, b):
 x=[0 for x in range(len(b))]
 for k in range(len(L)-1,-1,-1):
     suma=0
     for i in range(len(L)-1,k,-1):
         suma=suma+L[k][i]*x[i]
     x[k]=round((b[k]-suma) / L[k][k],2)

 return x


def gauss(A,b):
    n=3
    for i in range(0,n):
        for j in range(i+1,n):
            m =(A[j][i])/(A[i][i])
            b[j]=b[j]-m*b[i]
            for k in range(i,n):
             A[j][k]=A[j][k]-(m*A[i][k])


    return POM(A,b)
