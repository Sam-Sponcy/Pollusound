# domain_to_ip.py
import socket

def domaine_vers_ip(nom_domaine):
    try:
        adresse_ip = socket.gethostbyname(nom_domaine)
        return adresse_ip
    except socket.gaierror:
        return None  # Return None if the domain name cannot be resolved