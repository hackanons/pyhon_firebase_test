#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>
// Set these to run example.
#define FIREBASE_HOST "esri-eea51.firebaseio.com"
#define FIREBASE_AUTH "qULRQbnuzJ3qkAdYunMasgcLlKtpXic1UQ1FxHvM"
#define WIFI_SSID "kavin"
#define WIFI_PASSWORD "1123581321"
float fire;
void setup() {
Serial.begin(9600);
pinMode(D1, OUTPUT);
pinMode(D5, OUTPUT);
pinMode(A0, INPUT);
// connect to wifi.
WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
Serial.print("connecting");
while (WiFi.status() != WL_CONNECTED) {
Serial.print(".");
delay(500);
}
Serial.println();
Serial.print("connected: ");
Serial.println(WiFi.localIP());
Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
Firebase.set("LED_STATUS", 0);
}
int n = 0;
void loop() {
// get value
fire = analogRead(A0);
Serial.println(fire);
if(fire<250){
  digitalWrite(D5,HIGH);

  Firebase.setInt("fire_sensor_status",1);
}
n = Firebase.getInt("LED_STATUS");
// handle error
if (n==1) {
Serial.println("LED ON");
digitalWrite(D1,HIGH);  
return;
delay(10);
}
else {
Serial.println("LED OFF");
digitalWrite(D1,LOW);  
digitalWrite(D5,LOW);  
Firebase.setInt("fire_sensor_status",0);
return;
}
}


