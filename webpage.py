'''A simple program to create an html file froma given string,
and call the default web browser to display the file.'''

contents = '''<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script type="text/javascript">
var names = ["patientname","DOB","patientaddress","patientphone","name",
"street","citytown","state","zipcode","timeperiod","releaseto","obtainfrom",
"purpose","EDR","OPR","LXR","CR","A","DS","EMR","other","DI","CCD","consentto",
"refuse","parent","relationship"];
var emaildivdata = "Send to Email: <input id=\"email\" type=\"text\" name=\"email\">";
function submit(){
	
	var data = [];
	 for(i=0;i<names.length;i++){
	 	data[i] = (document.getElementById(names[i]).value);
	 }
	 console.log(data);
	 
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
}</script>
</head>
<body>
<div id="textfields">
	Patient Name: 
	<input id="patientname" type="text" name="name">
	Date of Birth: 
	<input id="DOB" type="text" name="DOB">
	<br>Address: 
	<input id="patientaddress" type="text" name="address">
	Phone: 
	<input id="patientphone" type="text" name="phone">
	<br>I authorize Rhode Island Hospital to (choose one): 
	<input name="releaseobtain" type="radio" id="releaseto" value="0"><span>Release To</span>
	<input name="releaseobtain" type="radio" id="obtainfrom" value="0"><span>Obtain From</span>
	<br>Name of Person / Place / Institution: 
	<input id="name" type="text" name="name">
	<br>Street: 
	<input id="street" type="text" name="street">
	City/Town:  
	<input id="citytown" type="text" name="citytown">
	State: 
	<select id="state" name="state">
	<option value="AL">AL</option>
	<option value="AK">AK</option>
	<option value="AZ">AZ</option>
	<option value="AR">AR</option>
	<option value="CA">CA</option>
	<option value="CO">CO</option>
	<option value="CT">CT</option>
	<option value="DE">DE</option>
	<option value="DC">DC</option>
	<option value="FL">FL</option>
	<option value="GA">GA</option>
	<option value="HI">HI</option>
	<option value="ID">ID</option>
	<option value="IL">IL</option>
	<option value="IN">IN</option>
	<option value="IA">IA</option>
	<option value="KS">KS</option>
	<option value="KY">KY</option>
	<option value="LA">LA</option>
	<option value="ME">ME</option>
	<option value="MD">MD</option>
	<option value="MA">MA</option>
	<option value="MI">MI</option>
	<option value="MN">MN</option>
	<option value="MS">MS</option>
	<option value="MO">MO</option>
	<option value="MT">MT</option>
	<option value="NE">NE</option>
	<option value="NV">NV</option>
	<option value="NH">NH</option>
	<option value="NJ">NJ</option>
	<option value="NM">NM</option>
	<option value="NY">NY</option>
	<option value="NC">NC</option>
	<option value="ND">ND</option>
	<option value="OH">OH</option>
	<option value="OK">OK</option>
	<option value="OR">OR</option>
	<option value="PA">PA</option>
	<option value="RI">RI</option>
	<option value="SC">SC</option>
	<option value="SD">SD</option>
	<option value="TN">TN</option>
	<option value="TX">TX</option>
	<option value="UT">UT</option>
	<option value="VT">VT</option>
	<option value="VA">VA</option>
	<option value="WA">WA</option>
	<option value="WV">WV</option>
	<option value="WI">WI</option>
	<option value="WY">WY</option>
</select>
	Zip Code: 
	<input id="zipcode" type="text" name="zipcode" maxlength="5" size="4">
	<br>Date of treatment or time period: 
	<input id="timeperiod" type="text" name="timeperiod">
	<br>Purpose for which disclosure is to be made: 
	<input id="purpose" type="text" name="purpose">
	<br>
	Information to be disclosed (check all applicable):<br>
	<input id="EDR" type="checkbox" name="EDR" value="0"><span>Emergency Dept. Record</span>
	<input id="OPR" type="checkbox" name="OPR" value="0"><span>Operative/Path Report</span>
	<input id="LXR" type="checkbox" name="LXR" value="0"><span>Lab / X-Ray Reports</span>
	<input id="CR" type="checkbox" name="CR" value="0"><span>Clinic Report</span>
	<br>
	<input id="A" type="checkbox" name="A" value="0"><span>Abstract*</span>
	<input id="DS" type="checkbox" name="DS" value="0"><span>Discharge Summary</span>
	<input id="EMR" type="checkbox" name="EMR" value="0"><span>Entire Medical Record</span>
	Other: 
	<input id="other" type="textbox" name="other">
	<br>
	<input id="DI" type="checkbox" name="DI" onchange="change();"><span>Discharge Instructions</span>
	<input id="CCD" type="checkbox" name="CCD" onchange="change();"><span>Cont. of Care Document (CCD)</span>
	<br><div id="emaildiv"></div>
	<br>Please check one: I hereby
	<input name="consentrefuse" type="radio" id="consentto" value="0"><span>Consent to</span>
	<input name="consentrefuse" type="radio" id="refuse" value="0"><span>Refuse</span>
	<br> the release of confidential information concerning: mental health, alcohol and/or drug use, sexual abuse, venereal disease, AIDS or HIV test results.
	<br>
	Name of Parent or Legally Appointed Representative (if applicable): 
	<input name="parent" type="text" id="parent">
	Relationship to Patient: 
	<input name="relationship" type="text" id="relationship" size="10">

	</div>

<div id="submit">
<input id="submit" type="submit" name="submit" onclick="submit();">
</div>
</body>
</html>
'''

def main():
    browseLocal(contents)

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac

main()