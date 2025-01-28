import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector
import pyaudio
import numpy as np
import time

# Initialize sound detection
CHUNK = 1024
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
THRESHOLD = 0.3  # Adjust this value based on testing

# Initialize PyAudio outside the loop
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

detector = HandDetector(detectionCon=0.8, maxHands=1)
video = cv2.VideoCapture(0)

# Add state variable for LED status
leds_on = False
last_snap_time = time.time()

try:
    while True:
        ret, frame = video.read()
        frame = cv2.flip(frame, 1)
        hands, img = detector.findHands(frame)

        # Sound detection
        try:
            data = np.frombuffer(stream.read(CHUNK, exception_on_overflow=False), dtype=np.float32)
            peak = np.average(np.abs(data)) * 10
            
            # Detect snap with cooldown to prevent multiple triggers
            current_time = time.time()
            if peak > THRESHOLD and (current_time - last_snap_time) > 0.5:
                leds_on = not leds_on
                if leds_on:
                    cnt.all_leds_on()
                    cv2.putText(frame, 'LEDs ON', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                else:
                    cnt.all_leds_off()
                    cv2.putText(frame, 'LEDs OFF', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                last_snap_time = current_time

        except Exception as e:
            print(f"Error reading audio: {e}")

        # Hand gesture detection
        if hands:
            lmList = hands[0]
            fingerUp = detector.fingersUp(lmList)
            print(fingerUp)
            cnt.led(fingerUp)
            
            if fingerUp == [0,0,0,0,0]:
                cv2.putText(frame, 'Finger count:0', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            elif fingerUp == [0,1,0,0,0]:
                cv2.putText(frame, 'Finger count:1', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)    
            elif fingerUp == [0,1,1,0,0]:
                cv2.putText(frame, 'Finger count:2', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            elif fingerUp == [0,1,1,1,0]:
                cv2.putText(frame, 'Finger count:3', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            elif fingerUp == [0,1,1,1,1]:
                cv2.putText(frame, 'Finger count:4', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            elif fingerUp == [1,1,1,1,1]:
                cv2.putText(frame, 'Finger count:5', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)

        cv2.imshow("frame", frame)
        k = cv2.waitKey(1)
        if k == ord("k"):
            break

finally:
    # Cleanup
    video.release()
    stream.stop_stream()
    stream.close()
    p.terminate()
    cv2.destroyAllWindows()