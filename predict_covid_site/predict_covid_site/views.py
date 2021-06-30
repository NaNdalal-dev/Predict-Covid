from django.shortcuts import render
from . import ex
print(ex)
def home(request):
	data = ''
	if request.POST:
		pulse = int(request.POST['pulse'])
		oxygen = int(request.POST['oxygen'])
		temperature = int(request.POST['temp'])
		data = [[pulse, oxygen, temperature]]
		
		
		result = ''
		print(result)

		return render(request,'home.html',{"result":result,"data":data,"pulse":pulse,"oxygen":oxygen,"temperature":temperature})

	return render(request,'home.html')