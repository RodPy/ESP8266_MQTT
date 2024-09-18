import paho.mqtt.client as mqtt

# Configuración de MQTT
BROKER_ADDRESS = "broker.mqtt-dashboard.com"  # Cambia al broker que estés utilizando
TOPIC = "test/topic"  # Cambia al tópico que desees utilizar
CLIENT_ID = "mqtt_client"

# Funciones de callback MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker MQTT")
        client.subscribe(TOPIC)  # Suscripción al tópico cuando te conectas al broker
    else:
        print(f"Error de conexión: {rc}")

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Mensaje recibido: {message} en el tópico: {msg.topic}")

# Función para publicar un mensaje
def publish_message(client, topic, message):
    result = client.publish(topic, message)
    if result.rc == 0:
        print(f"Mensaje enviado exitosamente al tópico {topic}")
    else:
        print(f"Fallo al enviar el mensaje al tópico {topic}")

# Inicialización de MQTT
def mqtt_client():
    client = mqtt.Client(CLIENT_ID)
    client.on_connect = on_connect
    client.on_message = on_message
    return client

# Ejecutar el cliente MQTT
def run():
    client = mqtt_client()
    client.connect(BROKER_ADDRESS, 1883, 60)  # Conexión al broker en el puerto 1883
    client.loop_start()

    # Publicar un mensaje de ejemplo
    publish_message(client, TOPIC, "Hola desde MQTT y Python sin base de datos")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Desconectando...")
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    run()
