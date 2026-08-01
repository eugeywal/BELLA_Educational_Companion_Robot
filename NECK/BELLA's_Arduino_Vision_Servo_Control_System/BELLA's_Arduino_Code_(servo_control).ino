// Include the official Servo library to interface with the motor
#include <Servo.h>

// Create a Servo object to manage motor output signals
Servo myServo;

void setup() {
  // Initialize serial communication at a high speed (115200 baud) for low latency
  Serial.begin(115200);

  // Attach the control line of the servo motor to digital pin 9
  myServo.attach(9);

  // Set the initial physical position of the servo motor to center (90 degrees)
  myServo.write(90);
}

void loop() {
  // Check if new serial data bytes are available from the Python script
  if (Serial.available() > 0) {

    // Read and parse the incoming integer angle value from the serial buffer
    int angle = Serial.parseInt();

    // Validate that the angle is within safe servo mechanical boundaries (0 to 180 degrees)
    if (angle >= 0 && angle <= 180) {

      // Command the servo motor to rotate to the received target angle
      myServo.write(angle);
    }
  }
}