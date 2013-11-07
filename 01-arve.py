BMW = "{:^90}"
print BMW.format("arve")
print
print

BMW1 ="{:<20}{:<35}{:<15}{:>20}"

print BMW1.format("Arve V2ljastaja" , "Arve Saaja" , "Arve number" , "1")
print BMW1.format("Tiit Kull" , " Tark Mees" , "Arve kuup2ev:" , "05.03.2008")
print BMW1.format("V2imela" , "3 Yhiselamu" , "Makse t2htaeg" , "10.12.2013")

BMW2 = "{:<45}{:<15}{:<15}{:>15}"
print
print
print BMW2.format("Kaup" , "Hind" , "Kogus" , "Kokku")
print BMW2.format("6unamahl" , "6.00" , "5" , "30.00")
print BMW2.format("Porgandi6unamahl" , "6.00" , "3" , "18.00")
print BMW2.format("Glogi" , "7.00" , "10" , "70.00")
print
print
BMW3 = "{:<60}{:<15}{:>15}"
print
print BMW3.format(" " , "K2ibemaksuta Kokku" , "118.00")
print BMW3.format(" " , "K2ibemaks 20%" , "23.60")
print BMW3.format(" " , "Kokku" , "141.60")
BMW4 = "{:<30}{:<35}"
print
print
print
print
print BMW4.format("Kontaktid" , "Arveldus nuber")
print BMW4.format("E-post: maheveski@gmail.com" , "Pank: SWEDPANK")
print BMW4.format("Telefon 56695354" , "Konto nr: 15616456845684")
