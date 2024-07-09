import time  # Module for time management

# Define the AT command you want to send
def SendStartCommand(ser, ip, port_ip):
    command1 = "AT\r\n"
    # Send the AT command
    print(f"Sending command: {command1.strip()}")
    ser.write(command1.encode('utf-8'))
    time.sleep(1)  # Wait a bit to allow Arduino to respond

    # Read Arduino's response
    response = ser.read_all().decode('utf-8')
    if "OK" in response:
        print("AT command executed successfully!")

    # Define the AT command you want to send
    command_PDP = "AT+CGDCONT=1,'IP','PDP link'\r\n"   # Define the PDP link name

    # Send the AT command
    print(f"Sending command: {command_PDP.strip()}")
    ser.write(command_PDP.encode('utf-8'))
    time.sleep(1)  # Wait a bit to allow Arduino to respond

    # Read Arduino's response
    response = ser.read_all().decode('utf-8')
    print(f"Arduino's response: {response.strip()}")

    # Define the AT command you want to send
    command_verifier_profilPDP = "AT+CGACT?\r\n"

    # Send the AT command
    print(f"Sending command: {command_verifier_profilPDP.strip()}")
    ser.write(command_verifier_profilPDP.encode('utf-8'))
    time.sleep(1)  # Wait a bit to allow Arduino to respond

    # Read Arduino's response
    response = ser.read_all().decode('utf-8')
    if "+CGACT: 1,1" in response:
        print("PDP profile activated!")

    # Define the AT commands you want to send
    command_etat_connection = ["AT+CSQ\r\n",
                               "AT+CGATT?\r\n"]

    for command in command_etat_connection:
        print(f"Sending command: {command.strip()}")
        ser.write(command.encode('utf-8'))
        time.sleep(1)  # Wait a bit to allow Arduino to respond
        response = ser.read_all().decode('utf-8')
        print(f"Arduino's response: {response.strip()}")

    if "+CGATT: 1" in response:
        print("Connected to the network!")

    # Define the AT commands you want to send
    command_mqtt = ['AT+UMQTT=0,"LTE-M_Sam"\r\n',
                    f"AT+UMQTT=1,{port_ip}\r\n",
                    'AT+UMQTT=2,"homeass"\r\n',
                    f'AT+UMQTT=3,"{ip}",{port_ip}\r\n',
                    'AT+UMQTT=4,"Name","password"\r\n'  # Replace Name and password with your MQTT credentials
                    ]

    for command in command_mqtt:
        print(f"Sending command: {command.strip()}")
        ser.write(command.encode('utf-8'))
        time.sleep(1)  # Wait a bit to allow Arduino to respond
        response = ser.read_all().decode('utf-8')
        print(f"Arduino's response: {response.strip()}")

    # Define the AT command you want to send AT+UMQTTC=1
    command_connection = 'AT+UMQTTC=1\r\n'

    # Send the AT command
    print(f"Sending command: {command_connection.strip()}")
    ser.write(command_connection.encode('utf-8'))
    time.sleep(1)  # Wait a bit to allow Arduino to respond

    # Read Arduino's response
    response = ser.read_all().decode('utf-8')
    print(f"Arduino's response: {response.strip()}")

    # Define the AT command you want to send AT+UMQTTC=8,"85.10.77.144"
    command_ping_serveur = f'AT+UMQTTC=8,"{ip}"\r\n'

    # Send the AT command
    print(f"Sending command: {command_ping_serveur.strip()}")
    ser.write(command_ping_serveur.encode('utf-8'))
    time.sleep(5)  # Wait a bit to allow Arduino to respond

    # Read Arduino's response
    response = ser.read_all().decode('utf-8')
    print(f"Arduino's response: {response.strip()}")
    if "+UMQTTC: 8,1" in response:
        print("MQTT server is reachable!")