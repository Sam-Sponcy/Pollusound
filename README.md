FR

- But du projet Pollusound
Le but du projet Pollusound est d'analyser les sons dans la ville de Bruxelles. Pour cela, nous utiliserons une carte LTE-M RAPID dev Kit Orange.

- BirdNET-Analyzer
Nous utiliserons l'IA de BirdNet afin de proposer une solution simple et abordable d'une IA de type CNN qui utilise le traitement d'image pour reconnaître un son.

Cette IA fonctionne sur un Raspberry Pi 4B. Celle-ci est fortement recommandée dans le dépôt (https://github.com/mcguirepr89/BirdNET-Pi).

Attention ! Il faut utiliser comme image dans le Raspberry le "Raspberry Pi OS Legacy 64 bits Bullseye" et non la version Bookworm.

- Carte Sodaq

Tutoriel ici : https://docs.allthingstalk.com/examples/hardware/get-started-sodaq-sara/

Nous utiliserons la carte "SODAQ SARA AFF REV 3" avec le code "nbIOT_serial_passthrough". Ce code assure la communication entre le Raspberry et le module SARA-R410M via une liaison série.

- main.py : Ce fichier permet de paramétrer le module SARA-R410M afin d'assurer la connexion au réseau cellulaire, au serveur MQTT et d'envoyer les détections de sons.

- birdnet_to_mqtt.py : Ce fichier permet de vérifier les logs du fichier '/var/log/syslog' afin de récupérer les données des oiseaux détectés par BirdNet. Ce code est une version modifiée de celui disponible sur (git: deepcoder / birdnet_to_mqtt.py). (https://gist.github.com/deepcoder/c309087c456fc733435b47d83f4113ff#file-birdnet_to_mqtt-py)



EN

-Goal of the Pollusound Project
The goal of the Pollusound project is to analyze sounds in the city of Brussels. For this, we will use an Orange LTE-M RAPID dev Kit.

- BirdNET-Analyzer
We will use BirdNet AI to provide a simple and affordable solution of a CNN-type AI that uses image processing to recognize a sound.

This AI runs on a Raspberry Pi 4B. This setup is highly recommended in the repository (https://github.com/mcguirepr89/BirdNET-Pi).

Attention! Use the "Raspberry Pi OS Legacy 64 bits Bullseye" as the image for the Raspberry, not the Bookworm version.

- Sodaq Board

Tutorial here: https://docs.allthingstalk.com/examples/hardware/get-started-sodaq-sara/

We will use the "SODAQ SARA AFF REV 3" board with the provided code "nbIOT_serial_passthrough". This code ensures communication between the Raspberry and the SARA-R410M module via serial connection.

- main.py: This file configures the SARA-R410M module to ensure connection to the cellular network, the MQTT server, and to send sound detections.

- birdnet_to_mqtt.py: This file checks the logs in '/var/log/syslog' to retrieve the data of birds detected by BirdNet. This code is a modified version of the one available at (git: deepcoder / birdnet_to_mqtt.py). (https://gist.github.com/deepcoder/c309087c456fc733435b47d83f4113ff#file-birdnet_to_mqtt-py)
