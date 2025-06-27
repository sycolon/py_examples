import paho.mqtt.client as mqtt
import random
import time
import json # Für die JSON-Serialisierung des Payloads

class MQTTClient:
    def __init__(self, callback, broker_address="localhost", port=1883,
                 subscribe_topic="messenger/bbq/u27/#", publish_base_topic="messenger/bbq/u27/",
                 client_name="default_user"):
        
        self.broker_address = broker_address
        self.port = port
        self.subscribe_topic = subscribe_topic
        self.publish_base_topic = publish_base_topic
        self.client_name = client_name
        self.client_id = f"client_{self.client_name}_{random.randint(0, 1000)}"
        self.client = mqtt.Client(client_id=self.client_id, clean_session=True)
        
        # Callbacks zuweisen
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.on_disconnect = self._on_disconnect
        self.client.on_publish = self._on_publish
        
        self.is_connected = False # Status, ob der Client verbunden ist
        self.callback=callback

    # --- Private Callback-Methoden ---
    # (Diese werden von paho-mqtt aufgerufen und rufen dann die öffentlichen Methoden auf)

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f"[{self.client_id}] Connected to Broker successfully!")
            self.is_connected = True
            client.subscribe(self.subscribe_topic)
            # Hier könntest du optional eine automatische erste Nachricht senden
            # self.publish_message(self.client_name, f"Hello from {self.client_name}!")
        else:
            print(f"[{self.client_id}] Failed to connect, return code {rc}")
            self.is_connected = False

    def _on_message(self, client, userdata, msg):
        try:
            # Versuche, den Payload als JSON zu dekodieren
            payload = json.loads(msg.payload.decode())
            print(f"[{self.client_id}] Received (JSON): {payload} {type(payload)}, from Topic {msg.topic}")
        except json.JSONDecodeError:
            # Wenn es kein JSON ist, behandle es als einfachen String
            print(f"[{self.client_id}] Received (String): {msg.payload.decode()}, from Topic {msg.topic}")
        self.callback(msg)

    def _on_disconnect(self, client, userdata, rc):
        self.is_connected = False
        if rc != 0:
            print(f"[{self.client_id}] Unexpected disconnection, return code {rc}")
        else:
            print(f"[{self.client_id}] Disconnected successfully.")

    def _on_publish(self, client, userdata, mid):
        print(f"[{self.client_id}] Message with ID {mid} published.")

    # --- Öffentliche Methoden für die Client-Interaktion ---

    def connect_and_loop_start(self):
        """Versucht, eine Verbindung zum Broker herzustellen und den Netzwerk-Loop zu starten."""
        try:
            print(f"[{self.client_id}] Connecting to broker at {self.broker_address}:{self.port}...")
            self.client.connect(self.broker_address, self.port)
            self.client.loop_start() # Startet den Netzwerk-Loop in einem separaten Thread
            # Gib dem Client etwas Zeit, um die Verbindung aufzubauen
            time.sleep(1) 
        except Exception as e:
            print(f"[{self.client_id}] An error occurred during connection: {e}")

    def publish_message(self, sender_name, message_text, qos=0, retain=True):
        """
        Veröffentlicht eine Nachricht auf dem definierten Topic.
        Der Payload ist ein JSON-Objekt.
        """
        if not self.is_connected:
            print(f"[{self.client_id}] Not connected to broker. Message not sent: {message_text}")
            return False

        message_data = {
            "user": sender_name,
            "msg": message_text,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        # Erstelle das vollständige Veröffentlichungsthema
        publish_topic = f"{self.publish_base_topic}{sender_name.lower().replace(' ', '_')}"
        
        payload = json.dumps(message_data)
        
        try:
            result = self.client.publish(publish_topic, payload=payload, qos=qos, retain=retain)
            if result[0] == mqtt.MQTT_ERR_SUCCESS:
                print(f"[{self.client_id}] Publishing '{payload}' to '{publish_topic}' (MID: {result[1]})")
                return True
            else:
                print(f"[{self.client_id}] Failed to publish message: {result[0]}")
                return False
        except Exception as e:
            print(f"[{self.client_id}] Error during publish: {e}")
            return False

    def disconnect(self):
        """Trennt die Verbindung zum MQTT-Broker."""
        if self.is_connected:
            print(f"[{self.client_id}] Disconnecting from broker.")
            self.client.loop_stop() # Stoppt den Netzwerk-Loop-Thread
            self.client.disconnect()
        else:
            print(f"[{self.client_id}] Not connected, no need to disconnect.")

# --- Anwendung der Klasse ---
if __name__ == "__main__":
    # Erstelle einen Client für Benutzer Abdul
    abdul_client = MQTTClient(client_name="Abdul")
    abdul_client.connect_and_loop_start()

    # Erstelle optional einen zweiten Client, um die Kommunikation zu testen
    # Stell sicher, dass du Mosquitto oder einen anderen Broker laufen hast!
    lisa_client = MQTTClient(client_name="Lisa")
    lisa_client.connect_and_loop_start()

    print("\n--- Sending messages ---")
    # Warte kurz, um sicherzustellen, dass die Verbindung stabil ist
    time.sleep(2) 

    # Sende eine Nachricht von Abdul
    abdul_client.publish_message("Abdul", "Hallo vom Abdul (Nachricht 1)!")
    time.sleep(1)
    abdul_client.publish_message("Abdul", "Ich bin U27!")
    
    # Sende eine Nachricht von Lisa
    time.sleep(1)
    lisa_client.publish_message("Lisa", "Hallo Abdul, hier ist Lisa!")

    print("\n--- Keeping clients alive for 10 seconds ---")
    time.sleep(10) # Lass die Clients für 10 Sekunden laufen, um Nachrichten zu empfangen

    print("\n--- Disconnecting clients ---")
    abdul_client.disconnect()
    lisa_client.disconnect()
    print("All clients disconnected. Script finished.")