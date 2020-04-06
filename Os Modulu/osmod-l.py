import os
from datetime import datetime

#print(dir(os)) os deki fuctionlar

f"""or klasör_yolu,klasör_isimleri,dosya_isimler  in os.walk("C:/Users/mac/Desktop/MOOCs/Udemy/Ileri Seviye Python/Os Modulu/osmod-l.py"):
    for i in klasör_isimleri:
        if (i.startswith("kr")):
            print(i)"""




#Isletim sisteminde islemler gosterebiliyoruz.
            
        


from datetime import datetime



print(os.getcwd()) #modulum nerde oldugunu gosterdi
print(os.listdir()) #bu modulde hangi dosyalarin oldugunu gorursun.


# Dosyanimn bulundugu moduldeyim

os.mkdir("Deneme1")    #dosya olusturduk

os.makedirs("Deneme2/Deneme3")     #mkdirs function !!!

os.rmdir("Deneme2/Deneme3")     #deneme3 u remove ediyoruz.


os.removedirs("Deneme2/Deneme3") #hem Deneme2 yi hem Deneme3 u siliyoruz.

os.rename("text.txt","test2.txt")

print(os.stat("test2.txt"))

degistirilme = os.stat("test2.txt").st_mtime

print(datetime.fromtimestamp(degistirilme))

# print(os.listdir()) dosyalari listeler

#os.mkdir("Deneme1")

#os.makedirs("Deneme2/Deneme3")

#os.rmdir("Deneme2/Deneme3")

# os.rename("Deneme1","Deneme2")
# os.removedirs("Deneme2/Deneme3")

# os.rename("test.txt","test2.txt")

# print(os.stat("test2.txt"))

# degistirilme = os.stat("test2.txt").st_mtime

# print(datetime.fromtimestamp(degistirilme))


for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("/Users/mac/Desktop"):


    print("Current Path",klasör_yolu)
    print("Directories",klasör_isimleri)
    print("Dosyalar",dosya_isimleri)
    print("**********************************")
    
    
for klasör_yolu,klasör_isimleri,dosya_isimleri in os.walk("/Users/mac/Desktop"):
    for i in dosya_isimleri:
        if (i.endswith(".txt")):
            print(i)
                
        
       

#os.walk("ada") fonksiyonu cok onemli cok


