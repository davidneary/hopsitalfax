var names = ["patientname","DOB","patientaddress","patientphone","name",
"street","citytown","state","zipcode","timeperiod","releaseto","obtainfrom",
"purpose","consentto",
"refuse","parent","relationship"];
var emaildivdata = "Send to Email: <input id=\"email\" type=\"text\" name=\"email\">";
var json = {};
var bool;
var checkboxes = ["EDR","OPR","LXR","CR","A","DS","EMR","DI","CCD"];
var indexes 
function submit(){
	
	var data = {};
	 for(i=0;i<names.length;i++){
	 	data[names[i]] = (document.getElementById(names[i]).value);
	 }
	for (i=0;i<checkboxes.length;i++){
		data[checkboxes[i]] = document.getElementById(checkboxes[i]).checked;
	}
	console.log(data);
	postdata(data);
}
function change(){
	var DI = document.getElementById('DI').checked;
	var CCD = document.getElementById('CCD').checked;
	console.log(DI);
	console.log(CCD);
	if (DI == true | CCD == true){
		document.getElementById('emaildiv').innerHTML = emaildivdata;
		names[names.length] = "email";
	}
	else{
		document.getElementById('emaildiv').innerHTML = "";
		var id = names.indexOf("email");
		if (id > -1){
			names = names.splice(id,1);
		}
	}
		
}
function postdata(data){
	
	/*var formData = new FormData();
	formData.append("name": "Molly");
*/
	$.ajax({
		type: "POST",
		contentType: "application/json; charset=utf-8",
		crossDomain: true,
		url: "http://127.0.0.1:5000/",
		data: JSON.stringify(json),
		success: function(data){
			console.log(data);
		},
		dataType: "json"
	});
}