#include<Servo.h>

Servo servo;
int currentAngle = 90;// in the middle of a rotation, which means it should be facing forward

void setup() {
  Serial.begin(9600);
  servo.attach(9);// the servo pin
  servo.write(10);
}

void loop() {
  
  if (Serial.available())// if there is a cereived serial command
    {
      char command = Serial.read();
      Serial.print(command);
      Serial.print("  ");
      convertCommand(command);// convert the command to an angle monvement degree
    }

  servo.write(currentAngle);
  Serial.print(currentAngle);
  Serial.println();
}


void convertCommand(char command){// convert the command to an angle monvement degree
  
  int angleMovement;
  
  if(command == 'R')
    angleMovement = -5;
  else if(command == 'L')
    angleMovement = 5;
  else 
    angleMovement = 0;

  currentAngle+= angleMovement;

  if(currentAngle > 90)
    currentAngle = 90;
  else if(currentAngle < 0)
    currentAngle = 0;
}


