from datetime import datetime
import locale

print(locale.setlocale(locale.LC_ALL,""))




şu_an = datetime.now()


print(tarih - şu_an)

print(şu_an)
print(şu_an.year)
print(şu_an.month)
print(şu_an.hour)
print(şu_an.ctime())

print(datetime.strftime(şu_an,"%Y"))

print(datetime.strftime(şu_an,"%D"))

print(datetime.strftime(şu_an,"%Y & %B"))

saniye = datetime.timestamp(şu_an)

print(saniye)

şu_an2 = datetime.fromtimestamp(saniye)

print(şu_an2)
print(datetime.fromtimestamp(0))

tarih = datetime(2023,2,12)

print(tarih - şu_an)
