from django.shortcuts import render
from . import ex

def home(request):
	path = 'https://dr-covid.herokuapp.com'
	if request.POST:
		pulse = int(request.POST['pulse'])
		oxygen = int(request.POST['oxygen'])
		temperature = int(request.POST['temp'])
		data = [[pulse, oxygen, temperature]]
		model=ex.model
		result = int(model.predict(data)[0])
		proba = model.predict_proba(data)[0]
		yes,no = str(proba[0]*100)[:5], str(proba[1]*100)[:5]
		print(yes, no)
		yesnum,nonum = int(proba[0]*10), int(proba[1]*10)
		print(yesnum,nonum)
		if result == 1:
			result = "Covid Positive"
			alert = "danger"
		else:
			result = "Covid Negative"
			alert = "success"
			
		data = {
			
			"result":result,"alert":alert,"data":data,
			"pulse":pulse,"oxygen":oxygen,"temperature":temperature,'path':path,
			'yes':yes,'no':no,'yesnum':yesnum,'nonum':nonum}

		return render(request,'home.html',data)

	return render(request,'home.html',{'path':path})
