import cv2 #opencv k�t�hanesini import ettik.
import numpy as np #numpy k�t�phanesini import ettik.
import pygame #pygame k�t�phanesini import ettik.

cap = cv2.VideoCapture(0) #kameray� a�ar.

pygame.mixer.init() #Pygame'in ses �zelliklerini etkinle�tirir.

# ses �zelli�inin varsay�lan olarak kapal� oldu�u belirtilir.
sound_on = False

while True:

    ret, frame = cap.read() #videodaki kareleri yakalar ve okur.

    frame = cv2.flip(frame, 1) #okunan kare

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #BGR renk uzay�n� HSV renk uzay�na d�n��t�r�r.

    # sar�
    lower_limity = np.array([20, 100, 100]) #sar� rengin tonlar�n� ayarlar(min)
    upper_limity = np.array([30, 255, 255]) #sar� rengin tonlar�n� ayarlar(max)
    maskyellow = cv2.inRange(hsv_frame, lower_limity, upper_limity) #arkay� siyah yapar
    masky = cv2.bitwise_and(frame, frame,mask=maskyellow) #sar� rengi �ekip siyah arka planla birle�tirerek sadece sar� cismin g�r�nmesini sa�lar

    # sar� takip i�in
    contours, hierarchy = cv2.findContours(maskyellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #g�r�nt�deki sar� nesnelerin kenarlar�n� bulur.
    if contours:
        # en b�y�k kontur
        max_contour = max(contours, key=cv2.contourArea) #en b�y�k b�lgeyi bulur.
        # en k���k dikd�rtgen sarmalay�c� (bounding box)
        x, y, w, h = cv2.boundingRect(max_contour) #sar� nesnenin etraf�na dikd�rtgen yerle�tirir ve dikd�tgenin koordinatlar�n� hesaplar.
        # s�n�rlama kutusu (bounding box) �izimi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2) #�izilecek dikd�rtgenin �zellikleri ve �izilmesi.
        # dikd�rtgenin �st�ne metin yazma
        cv2.putText(frame, 'sari', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2) #dikd�rtgenin �zerine hangi renk oldu�una dair olan metni yazar.
        # ses �zelli�i a��ksa ve sar� rengi alg�lad���nda ses �al
        if sound_on:
            pygame.mixer.Sound('sari.mp3').play()

    # k�rm�z�
    lower_limitr = np.array([161, 155, 84]) #k�rm�z� rengin tonlar�n� ayarlar.(min)
    upper_limitr = np.array([179, 255, 255]) #k�rm�z� rengin tonlar�n� ayarlar.(max)
    maskred = cv2.inRange(hsv_frame, lower_limitr, upper_limitr) #arkay� siyah yapar.
    maskr = cv2.bitwise_and(frame, frame,mask=maskred) #k�rm�z� rengi �ekip siyah arka planla birle�tirerek sadece k�rm�z� cismin g�r�nmesini sa�lar.

    # k�rm�z� takip i�in
    contours, hierarchy = cv2.findContours(maskred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #g�r�nt�deki k�rm�z� nesnelerin kenarlar�n� bulur.
    if contours:
        # en b�y�k kontur
        max_contour = max(contours, key=cv2.contourArea) #en b�y�k b�lgeyi bulur.
        # en k���k dikd�rtgen sarmalay�c� (bounding box)
        x, y, w, h = cv2.boundingRect(max_contour) #k�rm�z� nesnenin etraf�na dikd�rtgen yerle�tirir ve dikd�tgenin koordinatlar�n� hesaplar.
        # s�n�rlama kutusu (bounding box) �izimi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) #�izilecek dikd�rtgenin �zellikleri ve �izilmesi.
        # dikd�rtgenin �st�ne metin yazma
        cv2.putText(frame, 'kirmizi', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2) #dikd�rtgenin �zerine hangi renk oldu�una dair olan metni yazar.
        # ses �zelli�i a��ksa ve sar� rengi alg�lad���nda ses �al
        if sound_on:
            pygame.mixer.Sound('kirmizi.mp3').play()

    # mavi
    lower_limitb = np.array([94, 80, 2]) #mavi rengin tonlar�n� ayarlar.(min)
    upper_limitb = np.array([126, 255, 255]) #mavi rengin tonlar�n� ayarlar.(max)
    maskblue = cv2.inRange(hsv_frame, lower_limitb, upper_limitb) #arkay� siyah yapar.
    maskb = cv2.bitwise_and(frame, frame,mask=maskblue) #mavi rengi �ekip siyah arka planla birle�tirerek sadece k�rm�z� cismin g�r�nmesini sa�lar.

    # mavi takip i�in
    contours, hierarchy = cv2.findContours(maskblue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #g�r�nt�deki mavi nesnelerin kenarlar�n� bulur.
    if contours:
        # en b�y�k kontur
        max_contour = max(contours, key=cv2.contourArea) #en b�y�k b�lgeyi bulur.
        # en k���k dikd�rtgen sarmalay�c� (bounding box)
        x, y, w, h = cv2.boundingRect(max_contour) #mavi nesnenin etraf�na dikd�rtgen yerle�tirir ve dikd�tgenin koordinatlar�n� hesaplar.
        # s�n�rlama kutusu (bounding box) �izimi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) #�izilecek dikd�rtgenin �zellikleri ve �izilmesi.
        # dikd�rtgenin �st�ne metin yazma
        cv2.putText(frame, 'mavi', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)  #dikd�rtgenin �zerine hangi renk oldu�una dair olan metni yazar.
        # ses �zelli�i a��ksa ve sar� rengi alg�lad���nda ses �al
        if sound_on:
            pygame.mixer.Sound('mavi.mp3').play()

    # ye�il
    lower_limitg = np.array([36, 50, 70]) #ye�il rengin tonlar�n� ayarlar.(min)
    upper_limitg = np.array([89, 255, 255]) #ye�il rengin tonlar�n� ayarlar.(max)
    maskgreen = cv2.inRange(hsv_frame, lower_limitg, upper_limitg) #arkay� siyah yapar.
    maskg = cv2.bitwise_and(frame, frame,mask=maskgreen) #ye�il rengi �ekip siyah arka planla birle�tirerek sadece ye�il cismin g�r�nmesini sa�lar.

    # ye�il takip i�in
    contours, hierarchy = cv2.findContours(maskgreen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #g�r�nt�deki ye�il nesnelerin kenarlar�n� bulur.
    if contours:
        # en b�y�k kontur
        max_contour = max(contours, key=cv2.contourArea) #en b�y�k b�lgeyi bulur.
        # en k���k dikd�rtgen sarmalay�c� (bounding box)
        x, y, w, h = cv2.boundingRect(max_contour) #ye�il nesnenin etraf�na dikd�rtgen yerle�tirir ve dikd�tgenin koordinatlar�n� hesaplar.
        # s�n�rlama kutusu (bounding box) �izimi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) #�izilecek dikd�rtgenin �zellikleri ve �izilmesi.
        # dikd�rtgenin �st�ne metin yazma
        cv2.putText(frame, 'yesil', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2) #dikd�rtgenin �zerine hangi renk oldu�una dair olan metni yazar.
        # ses �zelli�i a��ksa ve sar� rengi alg�lad���nda ses �al
        if sound_on:
            pygame.mixer.Sound('yesil.mp3').play()

    # mor 
    lower_limitp = np.array([129, 50, 70]) #mor rengin tonlar�n� ayarlar.(min)
    upper_limitp = np.array([158, 255, 255])#mor rengin tonlar�n� ayarlar.(max)
    maskpurple = cv2.inRange(hsv_frame, lower_limitp, upper_limitp) #arkay� siyah yapar.
    maskp = cv2.bitwise_and(frame, frame,mask=maskpurple) #ye�il rengi �ekip siyah arka planla birle�tirerek sadece mor cismin g�r�nmesini sa�lar.

    # mor takip i�in
    contours, hierarchy = cv2.findContours(maskpurple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #g�r�nt�deki mor nesnelerin kenarlar�n� bulur.
    if contours:
        # en b�y�k kontur
        max_contour = max(contours, key=cv2.contourArea) #en b�y�k b�lgeyi bulur.
        # en k���k dikd�rtgen sarmalay�c� (bounding box)
        x, y, w, h = cv2.boundingRect(max_contour) #mor nesnenin etraf�na dikd�rtgen yerle�tirir ve dikd�tgenin koordinatlar�n� hesaplar.
        # s�n�rlama kutusu (bounding box) �izimi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (128, 0, 128), 2) #�izilecek dikd�rtgenin �zellikleri ve �izilmesi.
        # dikd�rtgenin �st�ne metin yazma
        cv2.putText(frame, 'mor', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (128, 0, 128), 2)  #dikd�rtgenin �zerine hangi renk oldu�una dair olan metni yazar.
        # ses �zelli�i a��ksa ve sar� rengi alg�lad���nda ses �al
        # ses �zelli�i a��ksa ve sar� rengi alg�lad���nda ses �al
        if sound_on:
            pygame.mixer.Sound('mor.mp3').play()

    # turuncu
    lower_limito = np.array([10, 50, 70]) #turuncu rengin tonlar�n� ayarlar.(min)
    upper_limito = np.array([24, 255, 255]) #turuncu rengin tonlar�n� ayarlar.(max)
    maskorange = cv2.inRange(hsv_frame, lower_limito, upper_limito) #arkay� siyah yapar.
    masko = cv2.bitwise_and(frame, frame,mask=maskorange) #mor rengi �ekip siyah arka planla birle�tirerek sadece mor cismin g�r�nmesini sa�lar.

    # turuncu takip i�in
    contours, hierarchy = cv2.findContours(maskorange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #g�r�nt�deki turuncu nesnelerin kenarlar�n� bulur.
    if contours:
        # en b�y�k kontur
        max_contour = max(contours, key=cv2.contourArea) #en b�y�k b�lgeyi bulur.
        # en k���k dikd�rtgen sarmalay�c� (bounding box)
        x, y, w, h = cv2.boundingRect(max_contour) #turuncu nesnenin etraf�na dikd�rtgen yerle�tirir ve dikd�tgenin koordinatlar�n� hesaplar.
        # s�n�rlama kutusu (bounding box) �izimi
        # s�n�rlama kutusu (bounding box) �izimi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 165, 255), 2) #�izilecek dikd�rtgenin �zellikleri ve �izilmesi.
        # dikd�rtgenin �st�ne metin yazma
        cv2.putText(frame, 'turuncu', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 165, 255), 2) #dikd�rtgenin �zerine hangi renk oldu�una dair olan metni yazar.
        # ses �zelli�i a��ksa ve sar� rengi alg�lad���nda ses �al
        if sound_on:
            pygame.mixer.Sound('turuncu.mp3').play()

    #farkl� renkler i�in olu�turulmu� maske g�r�nt�lerini ve orjinal g�r�nt�y� ekranda g�sterir.
    cv2.imshow("kamera", frame)
    cv2.imshow("yellow_mask", masky)
    cv2.imshow("red_mask", maskr)
    cv2.imshow("blue_mask", maskb)
    cv2.imshow("green_mask", maskg)
    cv2.imshow("purple_mask", maskp)
    cv2.imshow("orange_mask", masko)


    key = cv2.waitKey(1)
    if key == ord('q'): #q tu�una basld���nda d�ng� sonlan�r.
        break
    # s tu�una bas�ld���nda ses �zelli�i a��l�r
    elif key == ord('s'):
        sound_on = True
    # d tu�una bas�ld���nda ses �zelli�i kapat�l�r
    elif key == ord('d'):
        sound_on = False

cap.release() #kamera serbest kal�r.
cv2.destroyAllWindows() #t�m OpenCV pencerelerini kapat�r ve program� sonland�r�r.