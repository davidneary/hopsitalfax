from fpdf import FPDF
["patientname","DOB","patientaddress","patientphone","name",
"street","citytown","state","zipcode","timeperiod","releaseto","obtainfrom",
"purpose","EDR","OPR","LXR","CR","A","DS","EMR","other","DI","CCD","consentto",
"refuse","parent","relationship"] ["patientname","DOB","patientaddress","patientphone","name",
"street","citytown","state","zipcode","timeperiod","releaseto","obtainfrom",
"purpose","EDR","OPR","LXR","CR","A","DS","EMR","other","DI","CCD","consentto",
"refuse","parent","relationship","email"]=RETURNEDJAVASCRIPTINPUT
pdf=FPDF()
pdf.add_page()
pdf.add_font('Signature', '', '/home/david/Documents/hospitalfax/font/Biloxi Script.ttf', uni=True)

pdf.set_font('Arial','B',10)

pdf.set_y(79)
pdf.set_x(40)
pdf.cell(1,txt=patientname)

pdf.set_y(79)
pdf.set_x(140)
pdf.cell(1,txt=DOB)

pdf.set_y(87)
pdf.set_x(30)
pdf.cell(1,txt=patientaddress)

pdf.set_y(87)
pdf.set_x(165)
pdf.cell(1,txt=patientphone)

pdf.set_y(105)
pdf.set_x(25)
pdf.cell(1,txt=name)

pdf.set_y(118)
pdf.set_x(25)
pdf.cell(1,txt=street)

pdf.set_y(118)
pdf.set_x(100)
pdf.cell(1,txt=citytown)

pdf.set_y(118)
pdf.set_x(130)
pdf.cell(1,txt=state)

pdf.set_y(118)
pdf.set_x(165)
pdf.cell(1,txt=zipcode)

pdf.set_y(130)
pdf.set_x(80)
pdf.cell(1,txt=timeperiod)

pdf.set_y(137)
pdf.set_x(95)
pdf.cell(1,txt=purpose)

pdf.set_y(168)
pdf.set_x(127)
pdf.cell(1,txt=email)

pdf.set_font('Signature','',24)

pdf.set_y(256)
pdf.set_x(20)
pdf.cell(1,txt=patientname)

pdf.set_font('Arial','B',10)

pdf.set_y(258)
pdf.set_x(100)
pdf.cell(1,txt="02/08/15")

pdf.set_y(258)
pdf.set_x(133)
pdf.cell(1,txt=patientname)

pdf.set_y(270)
pdf.set_x(20)
pdf.cell(1,txt=parent)

pdf.set_y(270)
pdf.set_x(125)
pdf.cell(1,txt=relationship)

pdf.output('/home/david/Documents/hospitalfax/test2.pdf','F')