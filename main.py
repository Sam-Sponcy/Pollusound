import time                # Module for time management
import json                # Module for JSON processing
import re                  # Module for regular expressions
import dateparser          # Module for date parsing
import datetime            # Module for date and time manipulation
import serial              # Module for serial communication
from domain_to_ip import domaine_vers_ip  # Function to convert domain name to IP address
from command_start import SendStartCommand  # Function to send configuration commands to SARA R410M module
from send_mqtt import SendMqtt  # Function to send MQTT messages
from birdnet_to_mqtt import bird_json  # Function to fetch BirdNET JSON data

def DnsToIP(nom_domaine):
    """
    Function to convert a domain name to an IP address.
    Uses the domaine_vers_ip function from the domain_to_ip module.
    """
    adresse_ip = domaine_vers_ip(nom_domaine)
    if adresse_ip:
        print(f"The IP address of {nom_domaine} is: {adresse_ip}")
    else:
        print(f"Unable to resolve IP address for {nom_domaine}")
    return adresse_ip

if __name__ == "__main__":
    try:
        port = '/dev/ttyACM0'   # Serial port of raspbeery definition
        nom_domaine = "myserver.com" 
        ip = DnsToIP(nom_domaine)  
        # If you want to use a static IP address instead of resolving the domain name,
        # uncomment the following line and comment out the ip = DnsToIP(nom_domaine) line above.
        # ip = "0.0.0.0"

        port_ip = "1883"  # MQTT port

        ser = serial.Serial(port, 115200, timeout=1)  # Serial communication initialization
        
        # Sending configuration to SARA R410M module
        SendStartCommand(ser, ip, port_ip)
        
        topic = "birdnet/status"  # MQTT topic for status
        message = "ready"  # Message to send
        SendMqtt(ser, topic, message)  # Sending MQTT message
        
        # Sending BirdNET detection data
        topic = "birdnet/detection"  # MQTT topic for detections
        while True:
            file_bird = bird_json()  # Getting detection data in JSON format
            SendMqtt(ser, topic, file_bird)  # Sending MQTT data
            print(f"Sending detection: {file_bird}")  # Display for confirmation
            
    except Exception as e:
        print(f"General error: {e}")  # Displaying errors
        
    finally:
        ser.close()  # Closing serial connection at the end of the program