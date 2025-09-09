import cv2
import mediapipe as mp

#webcam
cap = cv2.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hand = mp_hands.Hands()

#loop
while True:
    #get image from webcam 
    success, img = cap.read()  #cap.read retorna um boolean e um array(imagem)
    if success:
        RBG_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hand.process(RBG_img)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                print(hand_landmarks)
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        img = cv2.flip(img, 1)

        #display image
        cv2.imshow("image", img)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.rectangle(img,(100,100), (200,200), (225,225,225), cv2.FILLED)
cap.release()
cv2.destroyAllWindows()
