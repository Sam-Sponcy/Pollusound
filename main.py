import serial              
import time                
import json                
import re                  # Module pour les expressions régulières
import dateparser          # Module pour l'analyse des dates
import datetime            # Module pour la manipulation des dates et heures
from domain_to_ip import domaine_vers_ip  # Fonction pour convertir un nom de domaine en adresse IP
from command_start import SendStartCommand  # Fonction pour envoyer les commandes de configuration au module SARA R410M
from send_mqtt import SendMqtt  # Fonction pour envoyer des messages MQTT
from birdnet_to_mqtt import bird_json  # Fonction pour obtenir des données JSON de BirdNET

def DnsToIP(nom_domaine):
  
    adresse_ip = domaine_vers_ip(nom_domaine)
    if adresse_ip:
        print(f"L'adresse IP de {nom_domaine} est : {adresse_ip}")
    else:
        print(f"Impossible de résoudre l'adresse IP pour {nom_domaine}")
    return adresse_ip

if __name__ == "__main__":
    try:
        port = '/dev/ttyACM0'   # Définition du port série
        nom_domaine = "polusound.ddns.net" 
        ip = DnsToIP(nom_domaine)  
        # Si l'on souhaite utiliser une adresse IP statique plutôt que de résoudre le nom de domaine,
        # décommentez la ligne suivante et commentez la ligne ip = DnsToIP(nom_domaine) ci-dessus.
        # ip = "0.0.0.0"

        port_ip = "1883"  # Port MQTT

        ser = serial.Serial(port, 115200, timeout=1)  # Initialisation de la communication série
        
        # Envoi de la configuration du module SARA R410M
        SendStartCommand(ser, ip, port_ip)
        
        topic = "birdnet/status"  # Topic MQTT pour le statut
        message = "ready"  # Message à envoyer
        SendMqtt(ser, topic, message)  # Envoi du message MQTT
        
        # Envoi des données de détection BirdNET
        topic = "birdnet/detection"  # Topic MQTT pour les détections
        while True:
            file_bird = bird_json()  # Obtention des données de détection au format JSON
            SendMqtt(ser, topic, file_bird)  # Envoi des données MQTT
            print(f"Envoi de la détection : {file_bird}")  # Affichage pour confirmation
            
    except Exception as e:
        print(f"Erreur générale: {e}")  # Affichage des erreurs
        
    finally:
        ser.close()  # Fermeture de la connexion série à la fin du programme
