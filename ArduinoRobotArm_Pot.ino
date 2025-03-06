/*        
       DIY Arduino Robot Arm with Potentiometer Control
       by MatekDev
*/

#include <Servo.h>

Servo servo01;
Servo servo02;
Servo servo03;
Servo servo04;
Servo servo05;
Servo servo06;
int servo1PPos, servo2PPos, servo3PPos, servo4PPos, servo5PPos, servo6PPos; // previous position

int potin1 = 5;
int potin2 = 4;
int potin3 = 3;
int potin4 = 2;
int potin5 = 1;
int potin6 = 0;

int val1, val2, val3, val4, val5, val6;

// int pot2serv(input_pin) {
//   int val = analogRead(input_pin);
//   val = map(val, 0, 1023, 0, 180);
// }

void setup() {
  servo01.attach(10);
  servo02.attach(9);
  servo03.attach(8);
  servo04.attach(13);
  servo05.attach(12);
  servo06.attach(11);

  // Robot arm initial position
  servo1PPos = 90; // Initial 90
  servo01.write(servo1PPos);
  servo2PPos = 140; // Initial 150
  servo02.write(servo2PPos);
  servo3PPos = 33; // Initial 35
  servo03.write(servo3PPos);
  servo4PPos = 135; // Initial 140
  servo04.write(servo4PPos);
  servo5PPos = 85; // Initial 85
  servo05.write(servo5PPos);
  servo6PPos = 5; // Initial 80
  servo06.write(servo6PPos);
  delay(20);
}

void loop() {

  // Move servo 1
  val1 = analogRead(potin1);
  val1 = map(val1, 0, 1023, 0, 180);
  if (val1 != servo1PPos) {
    // We use for loops so we can control the speed of the servo
    // If previous position is bigger then current position
    if (servo1PPos > val1) {
      for ( int j = servo1PPos; j >= val1; j--) {   // Run servo down
        servo01.write(j);
        delay(20);    // defines the speed at which the servo rotates
      }
    }
    // If previous position is smaller then current position
    if (servo1PPos < val1) {
      for ( int j = servo1PPos; j <= val1; j++) {   // Run servo up
        servo01.write(j);
        delay(20);
      }
    }
    servo1PPos = val1;   // set current position as previous position
  }

  // Move servo 2
  val2 = analogRead(potin2);
  val2 = map(val2, 0, 1023, 0, 180);
  if (val2 != servo2PPos) {
    // We use for loops so we can control the speed of the servo
    // If previous position is bigger then current position
    if (servo2PPos > val2) {
      for ( int j = servo2PPos; j >= val2; j--) {   // Run servo down
        servo02.write(j);
        delay(20);    // defines the speed at which the servo rotates
      }
    }
    // If previous position is smaller then current position
    if (servo2PPos < val2) {
      for ( int j = servo2PPos; j <= val2; j++) {   // Run servo up
        servo02.write(j);
        delay(20);
      }
    }
    servo2PPos = val2;   // set current position as previous position
  }
    
  // Move servo 3
  val3 = analogRead(potin3);
  val3 = map(val3, 0, 1023, 0, 180);
  if (val3 != servo3PPos) {
    // We use for loops so we can control the speed of the servo
    // If previous position is bigger then current position
    if (servo3PPos > val3) {
      for ( int j = servo3PPos; j >= val3; j--) {   // Run servo down
        servo03.write(j);
        delay(20);    // defines the speed at which the servo rotates
      }
    }
    // If previous position is smaller then current position
    if (servo3PPos < val3) {
      for ( int j = servo3PPos; j <= val3; j++) {   // Run servo up
        servo03.write(j);
        delay(20);
      }
    }
    servo3PPos = val3;   // set current position as previous position
  }

  // Move servo 4
  val4 = analogRead(potin4);
  val4 = map(val4, 0, 1023, 0, 180);
  if (val4 != servo4PPos) {
    // We use for loops so we can control the speed of the servo
    // If previous position is bigger then current position
    if (servo4PPos > val4) {
      for ( int j = servo4PPos; j >= val4; j--) {   // Run servo down
        servo04.write(j);
        delay(20);    // defines the speed at which the servo rotates
      }
    }
    // If previous position is smaller then current position
    if (servo4PPos < val4) {
      for ( int j = servo4PPos; j <= val4; j++) {   // Run servo up
        servo04.write(j);
        delay(20);
      }
    }
    servo4PPos = val4;   // set current position as previous position
  }

  // Move servo 5
  val5 = analogRead(potin5);
  val5 = map(val5, 0, 1023, 0, 180);
  if (val5 != servo5PPos) {
    // We use for loops so we can control the speed of the servo
    // If previous position is bigger then current position
    if (servo5PPos > val5) {
      for ( int j = servo5PPos; j >= val5; j--) {   // Run servo down
        servo05.write(j);
        delay(20);    // defines the speed at which the servo rotates
      }
    }
    // If previous position is smaller then current position
    if (servo5PPos < val5) {
      for ( int j = servo5PPos; j <= val5; j++) {   // Run servo up
        servo05.write(j);
        delay(20);
      }
    }
    servo5PPos = val5;   // set current position as previous position
  }

  // Move servo 6
  val6 = analogRead(potin6);
  val6 = map(val6, 0, 1023, 0, 180);
  if (val6 != servo6PPos) {
    // We use for loops so we can control the speed of the servo
    // If previous position is bigger then current position
    if (servo6PPos > val6) {
      for ( int j = servo6PPos; j >= val6; j--) {   // Run servo down
        servo06.write(j);
        delay(20);    // defines the speed at which the servo rotates
      }
    }
    // If previous position is smaller then current position
    if (servo6PPos < val6) {
      for ( int j = servo6PPos; j <= val6; j++) {   // Run servo up
        servo06.write(j);
        delay(20);
      }
    }
    servo6PPos = val6;   // set current position as previous position
  }
}
