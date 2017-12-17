from django.shortcuts import render

# Create your views here.


def index (request):
    return render(request, 'personal/home.html')
	
def contact (request):
	return  render(request, 'personal/basic.html', {'content':['connect me on my email','kuldeep.iitkgp@gmail.com']})
	#return (rend, 'personla/basic.html')
def eblog (request):
	return  render(request, 'admin/', {'content':['connect me on my email','kuldeep.iitkgp@gmail.com']})
	#return (rend, 'personla/basic.html')
