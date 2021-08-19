#include "DHT.h"

#define DHTPIN 2     
#define DHTTYPE DHT22   

DHT dht(DHTPIN, DHTTYPE);
void setup() {
  Serial.begin(9600);
  Serial.println(F("DHTxx test!"));
  dht.begin();
  pinMode(12,OUTPUT);    //relay 
}

void loop() { 
  delay(3000);  
  float h = dht.readHumidity();  
  float t = dht.readTemperature(); 
  float f = dht.readTemperature(true); 
 
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  
  float hif = dht.computeHeatIndex(f, h); 
  float hic = dht.computeHeatIndex(t, h, false);
 
     if(t >= 26 || h > 70) {
        digitalWrite(12,HIGH);
     }
     else {
        digitalWrite(12,LOW);  
     }

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F(" C "));
  Serial.print(f);
  Serial.print(F(" F  Heat index: "));
  Serial.print(hic);
  Serial.print(F(" C "));
  Serial.print(hif);
  Serial.println(F(" F"));
}
