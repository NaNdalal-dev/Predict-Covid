from django.shortcuts import render
from . import ex

def home(request):
	if request.POST:
		pulse = int(request.POST['pulse'])
		oxygen = int(request.POST['oxygen'])
		temperature = int(request.POST['temp'])
		data = [[pulse, oxygen, temperature]]
		model=ex.model
		result = int(model.predict(data)[0])

		if result == 1:
			result = "Covid Positive"
			alert = "danger"
		else:
			result = "Covid Negative"
			alert = "success"

		return render(request,'home.html',{
			"result":result,"alert":alert,"data":data,
			"pulse":pulse,"oxygen":oxygen,"temperature":temperature})

	return render(request,'home.html')