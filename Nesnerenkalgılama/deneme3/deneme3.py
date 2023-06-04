import cv2 #opencv kütühanesini import ettik.
import numpy as np #numpy kütüphanesini import ettik.
import pygame #pygame kütüphanesini import ettik.

cap = cv2.VideoCapture(0) #kamerayý açar.

pygame.mixer.init() #Pygame'in ses özelliklerini etkinleþtirir.

# ses özelliðinin varsayýlan olarak kapalý olduðu belirtilir.
sound_on = False

while True:

    ret, frame = cap.read() #videodaki kareleri yakalar ve okur.

    frame = cv2.flip(frame, 1) #okunan kare

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #BGR renk uzayýný HSV renk uzayýna dönüþtürür.

    # sarý
    lower_limity = np.array([20, 100, 100]) #sarý rengin tonlarýný ayarlar(min)
    upper_limity = np.array([30, 255, 255]) #sarý rengin tonlarýný ayarlar(max)
    maskyellow = cv2.inRange(hsv_frame, lower_limity, upper_limity) #arkayý siyah yapar
    masky = cv2.bitwise_and(frame, frame,mask=maskyellow) #sarý rengi çekip siyah arka planla birleþtirerek sadece sarý cismin görünmesini saðlar

    # sarý takip için
    contours, hierarchy = cv2.findContours(maskyellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #görüntüdeki sarý nesnelerin kenarlarýný bulur.
    if contours:
        # en büyük kontur
        max_contour = max(contours, key=cv2.contourArea) #en büyük bölgeyi bulur.
        # en küçük dikdörtgen sarmalayýcý (bounding box)
        x, y, w, h = cv2.boundingRect(max_contour) #sarý nesnenin etrafýna dikdörtgen yerleþtirir ve dikdötgenin koordinatlarýný hesaplar.
        # sýnýrlama kutusu (bounding box) çizimi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2) #çizilecek dikdörtgenin özellikleri ve çizilmesi.
        # dikdörtgenin üstüne metin yazma
        cv2.putText(frame, 'sari', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2) #dikdörtgenin üzerine hangi renk olduðuna dair olan metni yazar.
        # ses özelliði açýksa ve sarý rengi algýladýðýnda ses çal
        if sound_on:
            pygame.mixer.Sound('sari.mp3').play()

    # kýrmýzý
    lower_limitr = np.array([161, 155, 84]) #kýrmýzý rengin tonlarýný ayarlar.(min)
    upper_limitr = np.array([179, 255, 255]) #kýrmýzý rengin tonlarýný ayarlar.(max)
    maskred = cv2.inRange(hsv_frame, lower_limitr, upper_limitr) #arkayý siyah yapar.
    maskr = cv2.bitwise_and(frame, frame,mask=maskred) #kýrmýzý rengi çekip siyah arka planla birleþtirerek sadece kýrmýzý cismin görünmesini saðlar.

    # kýrmýzý takip için
    contours, hierarchy = cv2.findContours(maskred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #görüntüdeki kýrmýzý nesnelerin kenarlarýný bulur.
    if contours:
        # en büyük kontur
        max_contour = max(contours, key=cv2.contourArea) #en büyük bölgeyi bulur.
        # en küçük dikdörtgen sarmalayýcý (bounding box)
        x, y, w, h = cv2.boundingRect(max_contour) #kýrmýzý nesnenin etrafýna dikdörtgen yerleþtirir ve dikdötgenin koordinatlarýný hesaplar.
        # sýnýrlama kutusu (bounding box) çizimi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) #çizilecek dikdörtgenin özellikleri ve çizilmesi.
        # dikdörtgenin üstüne metin yazma
        cv2.putText(frame, 'kirmizi', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2) #dikdörtgenin üzerine hangi renk olduðuna dair olan metni yazar.
        # ses özelliði açýksa ve sarý rengi algýladýðýnda ses çal
        if sound_on:
            pygame.mixer.Sound('kirmizi.mp3').play()

    # mavi
    lower_limitb = np.array([94, 80, 2]) #mavi rengin tonlarýný ayarlar.(min)
    upper_limitb = np.array([126, 255, 255]) #mavi rengin tonlarýný ayarlar.(max)
    maskblue = cv2.inRange(hsv_frame, lower_limitb, upper_limitb) #arkayý siyah yapar.
    maskb = cv2.bitwise_and(frame, frame,mask=maskblue) #mavi rengi çekip siyah arka planla birleþtirerek sadece kýrmýzý cismin görünmesini saðlar.

    # mavi takip için
    contours, hierarchy = cv2.findContours(maskblue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #görüntüdeki mavi nesnelerin kenarlarýný bulur.
    if contours:
        # en büyük kontur
        max_contour = max(contours, key=cv2.contourArea) #en büyük bölgeyi bulur.
        # en küçük dikdörtgen sarmalayýcý (bounding box)
        x, y, w, h = cv2.boundingRect(max_contour) #mavi nesnenin etrafýna dikdörtgen yerleþtirir ve dikdötgenin koordinatlarýný hesaplar.
        # sýnýrlama kutusu (bounding box) çizimi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) #çizilecek dikdörtgenin özellikleri ve çizilmesi.
        # dikdörtgenin üstüne metin yazma
        cv2.putText(frame, 'mavi', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)  #dikdörtgenin üzerine hangi renk olduðuna dair olan metni yazar.
        # ses özelliði açýksa ve sarý rengi algýladýðýnda ses çal
        if sound_on:
            pygame.mixer.Sound('mavi.mp3').play()

    # yeþil
    lower_limitg = np.array([36, 50, 70]) #yeþil rengin tonlarýný ayarlar.(min)
    upper_limitg = np.array([89, 255, 255]) #yeþil rengin tonlarýný ayarlar.(max)
    maskgreen = cv2.inRange(hsv_frame, lower_limitg, upper_limitg) #arkayý siyah yapar.
    maskg = cv2.bitwise_and(frame, frame,mask=maskgreen) #yeþil rengi çekip siyah arka planla birleþtirerek sadece yeþil cismin görünmesini saðlar.

    # yeþil takip için
    contours, hierarchy = cv2.findContours(maskgreen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #görüntüdeki yeþil nesnelerin kenarlarýný bulur.
    if contours:
        # en büyük kontur
        max_contour = max(contours, key=cv2.contourArea) #en büyük bölgeyi bulur.
        # en küçük dikdörtgen sarmalayýcý (bounding box)
        x, y, w, h = cv2.boundingRect(max_contour) #yeþil nesnenin etrafýna dikdörtgen yerleþtirir ve dikdötgenin koordinatlarýný hesaplar.
        # sýnýrlama kutusu (bounding box) çizimi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) #çizilecek dikdörtgenin özellikleri ve çizilmesi.
        # dikdörtgenin üstüne metin yazma
        cv2.putText(frame, 'yesil', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2) #dikdörtgenin üzerine hangi renk olduðuna dair olan metni yazar.
        # ses özelliði açýksa ve sarý rengi algýladýðýnda ses çal
        if sound_on:
            pygame.mixer.Sound('yesil.mp3').play()

    # mor 
    lower_limitp = np.array([129, 50, 70]) #mor rengin tonlarýný ayarlar.(min)
    upper_limitp = np.array([158, 255, 255])#mor rengin tonlarýný ayarlar.(max)
    maskpurple = cv2.inRange(hsv_frame, lower_limitp, upper_limitp) #arkayý siyah yapar.
    maskp = cv2.bitwise_and(frame, frame,mask=maskpurple) #yeþil rengi çekip siyah arka planla birleþtirerek sadece mor cismin görünmesini saðlar.

    # mor takip için
    contours, hierarchy = cv2.findContours(maskpurple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #görüntüdeki mor nesnelerin kenarlarýný bulur.
    if contours:
        # en büyük kontur
        max_contour = max(contours, key=cv2.contourArea) #en büyük bölgeyi bulur.
        # en küçük dikdörtgen sarmalayýcý (bounding box)
        x, y, w, h = cv2.boundingRect(max_contour) #mor nesnenin etrafýna dikdörtgen yerleþtirir ve dikdötgenin koordinatlarýný hesaplar.
        # sýnýrlama kutusu (bounding box) çizimi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (128, 0, 128), 2) #çizilecek dikdörtgenin özellikleri ve çizilmesi.
        # dikdörtgenin üstüne metin yazma
        cv2.putText(frame, 'mor', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (128, 0, 128), 2)  #dikdörtgenin üzerine hangi renk olduðuna dair olan metni yazar.
        # ses özelliði açýksa ve sarý rengi algýladýðýnda ses çal
        # ses özelliði açýksa ve sarý rengi algýladýðýnda ses çal
        if sound_on:
            pygame.mixer.Sound('mor.mp3').play()

    # turuncu
    lower_limito = np.array([10, 50, 70]) #turuncu rengin tonlarýný ayarlar.(min)
    upper_limito = np.array([24, 255, 255]) #turuncu rengin tonlarýný ayarlar.(max)
    maskorange = cv2.inRange(hsv_frame, lower_limito, upper_limito) #arkayý siyah yapar.
    masko = cv2.bitwise_and(frame, frame,mask=maskorange) #mor rengi çekip siyah arka planla birleþtirerek sadece mor cismin görünmesini saðlar.

    # turuncu takip için
    contours, hierarchy = cv2.findContours(maskorange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #görüntüdeki turuncu nesnelerin kenarlarýný bulur.
    if contours:
        # en büyük kontur
        max_contour = max(contours, key=cv2.contourArea) #en büyük bölgeyi bulur.
        # en küçük dikdörtgen sarmalayýcý (bounding box)
        x, y, w, h = cv2.boundingRect(max_contour) #turuncu nesnenin etrafýna dikdörtgen yerleþtirir ve dikdötgenin koordinatlarýný hesaplar.
        # sýnýrlama kutusu (bounding box) çizimi
        # sýnýrlama kutusu (bounding box) çizimi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 165, 255), 2) #çizilecek dikdörtgenin özellikleri ve çizilmesi.
        # dikdörtgenin üstüne metin yazma
        cv2.putText(frame, 'turuncu', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 165, 255), 2) #dikdörtgenin üzerine hangi renk olduðuna dair olan metni yazar.
        # ses özelliði açýksa ve sarý rengi algýladýðýnda ses çal
        if sound_on:
            pygame.mixer.Sound('turuncu.mp3').play()

    #farklý renkler için oluþturulmuþ maske görüntülerini ve orjinal görüntüyü ekranda gösterir.
    cv2.imshow("kamera", frame)
    cv2.imshow("yellow_mask", masky)
    cv2.imshow("red_mask", maskr)
    cv2.imshow("blue_mask", maskb)
    cv2.imshow("green_mask", maskg)
    cv2.imshow("purple_mask", maskp)
    cv2.imshow("orange_mask", masko)


    key = cv2.waitKey(1)
    if key == ord('q'): #q tuþuna basldýðýnda döngü sonlanýr.
        break
    # s tuþuna basýldýðýnda ses özelliði açýlýr
    elif key == ord('s'):
        sound_on = True
    # d tuþuna basýldýðýnda ses özelliði kapatýlýr
    elif key == ord('d'):
        sound_on = False

cap.release() #kamera serbest kalýr.
cv2.destroyAllWindows() #tüm OpenCV pencerelerini kapatýr ve programý sonlandýrýr.