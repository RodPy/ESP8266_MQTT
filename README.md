
# ESP8266 MQTT

Este proyecto demuestra cómo conectar un ESP8266 a un broker MQTT para intercambiar mensajes de manera eficiente. El código permite que el ESP8266 actúe tanto como un publicador como un suscriptor, ideal para aplicaciones de IoT (Internet of Things) donde se necesita comunicación en tiempo real entre dispositivos.

## Características

- Conexión Wi-Fi utilizando el ESP8266.
- Comunicación a través del protocolo MQTT.
- Publicación de datos a un tópico MQTT.
- Suscripción a un tópico para recibir mensajes.
- Fácilmente adaptable para múltiples proyectos de IoT.

## Requisitos

### Hardware
- [ESP8266](https://www.espressif.com/en/products/socs/esp8266) (NodeMCU o cualquier variante compatible).
- Fuente de alimentación para el ESP8266 (MicroUSB o batería).
  
### Software
- Arduino IDE (o cualquier otro entorno compatible).
- Librerías de MQTT y ESP8266WiFi instaladas en el Arduino IDE.

### Librerías necesarias

Para que este proyecto funcione correctamente, debes instalar las siguientes librerías en el Arduino IDE:

1. **ESP8266WiFi**: Maneja la conexión Wi-Fi del ESP8266.
   - Se incluye automáticamente con la instalación de las placas ESP8266 en Arduino IDE.
   
2. **PubSubClient**: Librería para el protocolo MQTT.
   - Se puede instalar desde el Administrador de Librerías de Arduino IDE.

## Instalación de la placa ESP8266 en Arduino IDE

Antes de cargar el código en el ESP8266, debes instalar el soporte para las placas ESP8266 en el Arduino IDE. Sigue estos pasos:

1. Abre el **Arduino IDE**.
2. Ve a **Archivo > Preferencias**.
3. En el campo **Gestor de URLs adicionales de tarjetas**, pega la siguiente URL:
   ```
   https://arduino.esp8266.com/stable/package_esp8266com_index.json
   ```
4. Haz clic en **Aceptar** para guardar los cambios.
5. Ve a **Herramientas > Placa > Gestor de tarjetas**.
6. En el campo de búsqueda, escribe `esp8266` y selecciona **ESP8266 by ESP8266 Community**.
7. Haz clic en **Instalar**.
8. Después de la instalación, ve a **Herramientas > Placa** y selecciona **NodeMCU 1.0 (ESP-12E Module)** o el modelo ESP8266 que estés utilizando.

¡Con esto ya tienes instalada la placa ESP8266 en el Arduino IDE!

## Configuración del proyecto

1. **Configuración de Arduino IDE**: 
    - Asegúrate de haber seguido los pasos anteriores para instalar la placa ESP8266.
    - Selecciona tu placa ESP8266 desde **Herramientas > Placa > NodeMCU 1.0 (ESP-12E Module)**.

2. **Broker MQTT**: 
    - Este proyecto se conecta a un broker MQTT. Puedes usar un broker público como `broker.hivemq.com`, o configurar tu propio broker utilizando Mosquitto o servicios como AWS IoT, Google Cloud IoT, etc.

3. **Configuración de la red Wi-Fi**:
    - Edita el archivo `.ino` del proyecto para agregar tu SSID y contraseña en las siguientes líneas:
      ```cpp
      const char* ssid = "NOMBRE_DE_TU_WIFI";
      const char* password = "CONTRASEÑA_DE_TU_WIFI";
      ```

4. **Broker MQTT y Tópico**:
    - Configura la dirección del broker MQTT y el tópico al que deseas publicar o suscribirte:
      ```cpp
      const char* mqtt_server = "broker.hivemq.com";
      const char* mqtt_topic = "tu/topico";
      ```

## Instalación

1. Clona este repositorio en tu entorno local:
   ```bash
   git clone https://github.com/RodPy/ESP8266_MQTT.git
   ```

2. Abre el archivo `.ino` en el Arduino IDE.

3. Asegúrate de tener todas las librerías instaladas (WiFi y MQTT).

4. Sube el código a tu ESP8266 conectándolo a tu computadora a través de un cable USB.

## Uso

Una vez que el código esté cargado en tu ESP8266:

1. El ESP8266 intentará conectarse a la red Wi-Fi configurada.
2. Luego, se conectará al broker MQTT definido.
3. Publicará un mensaje en el tópico especificado o recibirá mensajes desde dicho tópico.

### Ejemplo de publicación:
Cada vez que el ESP8266 se conecta al broker, enviará un mensaje de saludo:
```cpp
client.publish(mqtt_topic, "Hello from ESP8266");
```

### Ejemplo de suscripción:
Cada vez que se recibe un mensaje en el tópico suscrito, se imprimirá en el monitor serie:
```cpp
void callback(char* topic, byte* payload, unsigned int length) {
    Serial.print("Message arrived [");
    Serial.print(topic);
    Serial.print("] ");
    for (int i = 0; i < length; i++) {
        Serial.print((char)payload[i]);
    }
    Serial.println();
}
```

## Personalización

Puedes modificar este proyecto para ajustarlo a tus necesidades. Aquí algunos ejemplos de personalización:

- **Sensores**: Conecta sensores (temperatura, humedad, movimiento, etc.) y publica los datos recolectados a través de MQTT.
- **Actuadores**: Suscríbete a tópicos para controlar actuadores (motores, luces, etc.) de manera remota.

## Recursos adicionales

- [Documentación oficial del ESP8266](https://www.espressif.com/en/products/socs/esp8266)
- [PubSubClient MQTT library](https://pubsubclient.knolleary.net/)

## Licencia

Este proyecto está licenciado bajo la MIT License - consulta el archivo [LICENSE](LICENSE) para más detalles.
