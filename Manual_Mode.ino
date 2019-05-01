////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Group Name: Team Autoshade
//Members: I'munique Hill, Jeffery Shorter,and Lowell Wilson
//Date
//Description: This code allows for communication between the arduino and the Raspberry pi to create a manual mode of the blinds
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
int INL = 4; // pin 5 for Left Relay
int INR = 5; // pin 4 for Right Relay
#define ON  0 // sets on as 0
#define OFF 1 // sets off as 1
int Value; //

void setup()  // put your setup code here, to run once:
{
  relay_init(); // initialize both relays as off
  Serial.begin(9600); //sets serial communication baud rate to 9600
  pinMode(INL, OUTPUT); // same as relay_init function
  pinMode(INR, OUTPUT); // same as relay_init function
  relay_SetStatus(OFF, OFF); //turn off all the relay
}
void loop() // put your main code here, to run repeatedly:
{ 
if(Serial.available()>0)  //if serial is active
{
 Value = Serial.read(); // = the data for Value is recieve through the serial port from python and is then red and processed by arduino
}
if (Value == '1') // if values send from python is 1 do this function
{
    Serial.println("Blinds Going down"); // prints function action
    relay_SetStatus(OFF, ON); // sets Right relay on
    delay(1500);              // run for 5 seconds
    relay_SetStatus(OFF, OFF);// set both relays off 
    delay(10);
    Value = '3'; //returns value to a different value to halt lowering till a button is pressed again
}
else if (Value == '0') // if value sent from python is 0 do this function
{
    Serial.println("Blinds Going Up");  // prints function action
    relay_SetStatus(ON, OFF); //turn left relay on
    delay(1500);              // run for 5 seconds
    relay_SetStatus(OFF, OFF); //turn both relays off
    delay(100);  //stops relays
    Value = '3'; //returns value to a different value to halt raising till a button is pressed again
}
}

void relay_SetStatus( unsigned char status_1,  unsigned char status_2) // function assigned unsigned char to each relay status
{
  digitalWrite(INL, status_1); // sets the left relay switch to status 1
  digitalWrite(INR, status_2); // sets the right relay switch to status 2
}
void relay_init(void)//initialize the relay
{
  //set all the relays OUTPUT
  pinMode(INL, OUTPUT); // INL is left relay
  pinMode(INR, OUTPUT); // INR is right relay
  relay_SetStatus(OFF, OFF); //turn off all the relay
}
