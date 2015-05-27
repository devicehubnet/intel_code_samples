/*
DeviceHUB.net sample code for getting digital actuator state.

In this example an LED is attached to digital pin 13 on the Intel Edison Board.

Download and install PubSubClient library from https://github.com/knolleary/pubsubclient

First open the PubSubClient.h library header file and make the following 
modification in that file. (increase the packet size as shown below). 

// MQTT_MAX_PACKET_SIZE : Maximum packet size
//#define MQTT_MAX_PACKET_SIZE 128
#define MQTT_MAX_PACKET_SIZE 256

created 26 May 2015
by Alexandru Gheorghe

*/

#include <SPI.h>
#include <WiFi.h>
#include <PubSubClient.h>
  
char ssid[] = "paste_your_SSID_here.ro";
char pass[] = "paste_your_SSID_password_here";

int status = WL_IDLE_STATUS;

#define API_KEY         "paste_your_API_KEY_here"
#define PROJECT_ID      "paste_your_PROJECT_ID_here"
#define ACTUATOR_NAME   "paste_your_ACTUATOR_NAME_here"
#define DEVICE_UUID     "paste_your_DEVICE_UUID_here"
#define sec             1000
// Digital pin 5 is the LED output pin
#define LED             13

char clientId[]          = "Intel_Edison";
char actuatorTopic[]     = "/a/"API_KEY"/p/"PROJECT_ID"/d/"DEVICE_UUID"/actuator/"ACTUATOR_NAME"/state";
// server mqtt.devicehub.net ip
char server[]            = "104.155.7.31";  
char message_buffer[150];

WiFiClient apiClient;
PubSubClient client(server, 1883, callback, apiClient);

// handles message arrived on subscribed topic(s)
void callback(char* topic, byte* payload, unsigned int length)
{
  int i = 0;
  
  // create buffer with null terminator
  for(i=0; i<length; i++) {
    message_buffer[i] = payload[i];
  }
  message_buffer[i] = '\0';
  
  String msgString = String(message_buffer).substring(43,44);
  
  Serial.println("message: " + msgString);
  
  if(msgString == "0"){
    digitalWrite(LED,LOW);
  }else {
    digitalWrite(LED,HIGH);
  }
}

void setup() 
{
  // init serial for debugging
  Serial.begin(9600);
  
  //initialize the digital pin as an output.
  pinMode(LED, OUTPUT);
  // light should be off
  digitalWrite(LED,LOW);
  
  while (status != WL_CONNECTED) 
  { 
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid,pass);
    delay(5000);
  } 

  Serial.println("Connected to wifi");
  printWifiStatus();
  
  Serial.println("\nStarting connection to server...");
  
  if(client.connect(clientId))  
  {
    client.subscribe(actuatorTopic);
    Serial.println("Successfuly connected and running!");
  }
  else  
  {
    Serial.println("Connection problem");
  }
}

void loop() 
{
  while (status != WL_CONNECTED) { 
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid,pass);
    delay(5000);
  } 
  
if (!client.connected())
  { 
    Serial.println("reconnecting ...");
    client.connect(clientId);
    delay(3*sec); 
    client.subscribe(actuatorTopic);
  }
  // MQTT client loop processing
  client.loop();
}

void printWifiStatus() 
{
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);
}