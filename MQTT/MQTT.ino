#include "Wire.h"

#include "math.h"

#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"
#include <WiFi.h>

int lastState = HIGH; 
int currentState;   

#define WLAN_SSID   "WiFiCJP-Alumnos"
#define WLAN_PASS   "cjpalumnos2021"

#define HOST        "190.104.149.31"

#define PORT        1883
#define USERNAME    "linux"
#define PASSWORD    "linux"

//time out loop count
const int timeout = 200;

WiFiClient client;
Adafruit_MQTT_Client mqtt(&client, HOST, PORT, USERNAME, PASSWORD);
Adafruit_MQTT_Publish acelera_x = Adafruit_MQTT_Publish(&mqtt, "acelerometro/ax");
Adafruit_MQTT_Publish acelera_y = Adafruit_MQTT_Publish(&mqtt, "acelerometro/ay");
Adafruit_MQTT_Publish acelera_z = Adafruit_MQTT_Publish(&mqtt, "acelerometro/az");
Adafruit_MQTT_Publish button = Adafruit_MQTT_Publish(&mqtt, "acelerometro/button");
Adafruit_MQTT_Publish msg = Adafruit_MQTT_Publish(&mqtt, "msg/hola");


void MQTT_connect();

void setup() { 
  delay(1); 
  WiFi.mode(WIFI_STA);  
  Serial.begin(115200);
  Serial.print("Connecting to ");
  Serial.println(WLAN_SSID);

  WiFi.begin(WLAN_SSID, WLAN_PASS);
  int i = 0;
  for (; i < timeout; i++)
  {
    if(WiFi.status() == WL_CONNECTED) break;
    delay(100);
    Serial.print(".");
  }
  if(i == timeout)
    Serial.println("No Conectado");

  Serial.println("IP address: "); Serial.println(WiFi.localIP());

  MQTT_connect();
}
  void loop() 
{
  msg.publish("HOLA");
  // acelera_x.publish(ax_d);
  // delay(1);
  // acelera_y.publish(ay_d);
  // delay(1);
  // acelera_z.publish(az_d);


}

void MQTT_connect() {
  int8_t ret;
  if (mqtt.connected()) {
    return;
  }

  Serial.print("Connecting to MQTT... ");
  uint8_t retries = 10;
  while ((ret = mqtt.connect()) != 0) { // connect will return 0 for connected
       Serial.println(mqtt.connectErrorString(ret));
       Serial.println("Retrying MQTT connection in 1 second...");
       mqtt.disconnect();
       delay(1000);
       retries--;
       if (retries == 0)
         Serial.println("No Conectado");

  }
  Serial.println("MQTT Connected!");
}

