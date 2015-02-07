var names = ["patientname","DOB","patientaddress","patientphone","name",
"street","citytown","state","zipcode","timeperiod","releaseto","obtainfrom",
"purpose","EDR","OPR","LXR","CR","A","DS","EMR","other","DI","CCD","email","consentto",
"refuse","parent","relationship"];

function submit(){
	
	var data = [];
	 for(i=0;i<names.length;i++){
	 	data[i] = (document.getElementById(names[i]).value);
	 }
}

/*
	var patientname = document.getElementById('patientname').value;
	var DOB = document.getElementById('DOB').value;
	var patientaddress = document.getElementById('patientaddress').value;
	var patientphone = document.getElementById('patientphone').value;
	var name = document.getElementById('name').value;
	var street = document.getElementById('street').value;
	var citytown = document.getElementById('citytown').value;
	var state = document.getElementById('state').value;
	var zipcode = document.getElementById('zipcode').value;
	var timeperiod = document.getElementById('timeperiod').value;
	var releasefrom = document.getElementById('releaseto').value;
	var obtainfrom = document.getElementById('obtainfrom').value;

	var purpose = document.getElementById('purpose').value;
	var EDR = document.getElementById('EDR').value;
	var OPR = document.getElementById('OPR').value;
	var LXR = document.getElementById('LXR').value;
	var CR = document.getElementById('CR').value;
	var A = document.getElementById('A').value;
	var DS = document.getElementById('DS').value;
	var EMR = document.getElementById('EMR').value;
	var other = document.getElementById('other').value;
	var DI = document.getElementById('DI').value;
	var CCD = document.getElementById('CCD').value;
	var email = document.getElementById('email').value;
	var consentto = document.getElementById('consentto');
	var refuse = document.getElementById('refuse');
*/