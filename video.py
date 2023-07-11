import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # можно вставить название и путь к другому файлу 

        #img = cv2.imread('faceTest.jpeg') 
        #img = cv2.resize(img, (700, 500))
        #img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #faces = face_cascades.detectMultiScale(img_gray)

        #for (x, y, w, h) in faces:
            #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # координаты, цвет и ширина рамки

        # cv2.imshow('Result', img)

        #cv2.waitKey(0)


cap = cv2.VideoCapture(0) # подсоединение вебки

while True: # получаем кадр, конверт. его в серый, рисуем прямоугольник и выводим лицо с линией на экран
    _, frame = cap.read() # считывание кадров и рамки, success покажет, получен кадр или нет
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    cv2.imshow('Preview', frame)
    faces = face_cascades.detectMultiScale(img_gray)   

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Result', frame)

    if cv2.waitKey(0) & 0xff == ord('q'): # поможет выйти из бесконечного цикла, нажав на q
        break