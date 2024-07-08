import time

def SendMqtt(ser, topic, message):
    command_mqtt = f'AT+UMQTTC=2,0,0,"{topic}","{message}"\r\n'
    print(f"Envoi de la commande : {command_mqtt.strip()}")
    ser.write(command_mqtt.encode('utf-8'))
    time.sleep(1)  # wait a bit to let the Arduino respond
    response = ser.read_all().decode('utf-8')
    print(f"Réponse de l'Arduino : {response.strip()}")