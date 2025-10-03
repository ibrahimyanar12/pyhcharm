birinci_sayı=int(input("birinci sayıyı giriniz: "))
ikinci_sayı=int(input("ikinci sayıyı giriniz: "))
islem=input("""yapmak istediğiniz işlemi giriniz
toplama:+,çıkarma:-,bölme:/,çarpma:* """)
if islem=="+":
    print(birinci_sayı + ikinci_sayı)
elif islem=="-":
    print(birinci_sayı - ikinci_sayı)
elif islem=="/":
    print(birinci_sayı / ikinci_sayı)
elif islem=="*":
    print(birinci_sayı * ikinci_sayı)
else:
    print("doğru işlemi giriniz!!!!!!")



