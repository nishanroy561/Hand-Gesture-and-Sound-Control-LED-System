# Hand Gesture and Sound Control LED System

This project combines computer vision and sound detection to control LED lights using hand gestures and finger snaps. It uses OpenCV for hand tracking and PyAudio for sound detection.

## Demo
D:\Hackathon\Hand-Gesture-and-Sound-Control-LED-System\video.mp4

## Features

- **Hand Gesture Control**: Control individual LEDs by showing different numbers of fingers
  - 1 finger: First LED
  - 2 fingers: First two LEDs
  - 3 fingers: First three LEDs
  - 4 fingers: First four LEDs
  - 5 fingers: All LEDs
  - 0 fingers (closed hand): All LEDs off

- **Sound Control**:
  - Snap your fingers to toggle all LEDs on/off
  - Built-in cooldown system to prevent multiple triggers

- **Visual Feedback**:
  - Real-time hand tracking visualization
  - Finger count display
  - LED status indicators

## Hardware Requirements

- Arduino board (tested with Arduino Uno)
- 5 LEDs
- 5 resistors (220Ω recommended)
- Breadboard and jumper wires
- Webcam
- Microphone

## Software Requirements

Required Python packages:
- OpenCV (cv2)
- cvzone
- PyAudio
- numpy
- pyfirmata

## Circuit Setup

1. Connect LEDs to Arduino digital pins:
   - LED 1 → Pin 8
   - LED 2 → Pin 9
   - LED 3 → Pin 10
   - LED 4 → Pin 11
   - LED 5 → Pin 12

2. Don't forget to use appropriate resistors with each LED

## Software Setup

1. Upload StandardFirmata to Arduino:
   - Open Arduino IDE
   - File → Examples → Firmata → StandardFirmata
   - Upload to your board

2. Install Python dependencies:
   ```bash
   pip install opencv-python cvzone pyaudio numpy pyfirmata
   ```

3. Update COM port:
   - Check your Arduino's COM port
   - Update `comport` variable in `controller.py`

## Running the Project

1. Connect Arduino and ensure correct COM port is set
2. Run the main program:
   ```bash
   python run.py
   ```
3. Position your hand in front of the camera
4. Use hand gestures or finger snaps to control LEDs
5. Press 'k' to exit the program

## Troubleshooting

- **No LED response**: Check Arduino COM port and connections
- **Sound detection issues**: Adjust `THRESHOLD` value in `hello.py`
- **Hand detection problems**: Ensure good lighting and clear background
- **PyAudio errors**: Make sure your microphone is properly connected and recognized

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
