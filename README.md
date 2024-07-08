
FR

- Le but du projet pollusound est d analiser des sons dans la ville de bruxelles. Pour cela nous utiliserons une carte LTE-M RAPID dev Kit Orange.

- BirdNET-Analyzer
Nous utiliserons l'IA de BirdNet afin d'avoir une solution simple et abordable d'une IA de type CNN qui utilise le traitement d'image afin de pourvoir reconaitre un son.

Cette IA tourne sur une raspberry Pi 4B. Celle ci est grandement conseiller dans le depos (https://github.com/mcguirepr89/BirdNET-Pi).

Attention ! Il faut mettre comme img dans la raspberry le (raspberry pi OS legacy 64bits bullseye).
Et non la version bookworm.

- Carte Sodaq

Tuto ici : https://docs.allthingstalk.com/examples/hardware/get-started-sodaq-sara/
On mettra dans la carte "SODAQ SARA AFF REV 3" le code donné "nbIOT_serial_passthrough". Celui ci assure la communication entre la raspberry et le module SARA-R410M via liaison serial.

- main.py : permet de parametrer le module SARA-R410M afin d assure la connextion au reseau celulaire, au serveur MQTT et d envoyer les detections de son.

- birdnet_to_mqtt.py : Permet de verifier les logs du fichier '/var/log/syslog' afin d'avoir les données des oiseau detecter par BirdNet.
Ce code est une version modifier de celui de (git: deepcoder / birdnet_to_mqtt.py).







EN
