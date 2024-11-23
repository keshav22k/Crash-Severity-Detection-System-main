
#include <TinyGPS++.h>
#include <SoftwareSerial.h>

int fsr=A5;
int col=4;
int fsrData=0;
int colData=1;
String latStr, lngStr, finalStr=";17.489824;78.396641";

TinyGPSPlus gps;
SoftwareSerial gpsSerial(2,3); 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  gpsSerial.begin(9600);
  pinMode(fsr,INPUT);
  pinMode(col,INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  colData=digitalRead(col);
  fsrData= analogRead(fsr);
  if(colData==0){
    Serial.print(fsrData);
    if(gpsSerial.available()>0){
      if(gps.encode(gpsSerial.read()) && gps.location.isValid())
      {
        latStr= String(gps.location.lat(),6);
        lngStr= String(gps.location.lng(),6);

        finalStr= ";"+latStr+";"+lngStr;
        Serial.println(finalStr);
    }
      else
        Serial.println(finalStr);
      delay(1000);
      }
  } 
}

