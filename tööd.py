tekst=raw_input("Sisesta tekst:")
midagi=raw_input("Midagi veel:")
if len(tekst)>10:
	print "Tekst on yle 10 t2hem2rgi"
else:
	print "Telst ei ole yle 10 t2hem2rgi"
if " " in tekst:
	print "Sisaldab tyhikut"
else :
	print "Ei sialda tyhikut"
if "z" not in tekst:
	print "Tekst ei sisalda z"
else :
	print "Sisaldab z"
if midagi in tekst:
	print tekst + " Sisaldab " + midagi
else :
	print tekst + " Ei sialda " + midagi
if tekst.isupper():
	print "Ei sisalda"
else :
	print "Sisaltab suurt"
print
print
print "YL 4"
print
x=raw_input("sisesta suured t2hed:")
y="###"
u=raw_input("Sisesta number")
fmt ="{:20}{:20}{:20}"
print fmt.format(x,""+ y,u)
