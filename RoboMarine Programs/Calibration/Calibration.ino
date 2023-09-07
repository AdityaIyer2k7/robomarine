#include <Servo.h>

/* Do NOT change any values here */
#define MOTOR_FRONT_LEFT 1
#define MOTOR_FRONT_RIGHT 2
#define MOTOR_BACK_LEFT 4
#define MOTOR_BACK_RIGHT 3

/* Edit this line to choose the motor*/
#define MOTOR_TO_CALIBRATE MOTOR_FRONT_LEFT

/* Do NOT change any of the following code */
Servo motor;

void setup() {
  motor.attach(MOTOR_TO_CALIBRATE)

void loop() {
  // put your main code here, to run repeatedly:

}
