import requests
import urllib

# Definieren Sie die Basis-URL
base_url = "http://juice-sh.op/#/"

# Machen Sie einen GET-Antrag an die Basis-URL und speichern Sie den Statuscode
base_response = requests.get(base_url)
base_inhalt = base_response.content
#print(base_inhalt)

# Definieren Sie eine Liste von möglichen Unterverzeichnissen
subdirectories = ["admin", "administrator", "scoreboard", "score-board"]

# Durchlaufen Sie die Liste der Unterverzeichnisse
for subdirectory in subdirectories:
    # Erstellen Sie die vollständige URL
    full_url = base_url + subdirectory

    # Machen Sie einen GET-Antrag an die vollständige URL
    response = requests.get(full_url)

    # Überprüfen Sie den Statuscode der Antwort
    status = response.status_code
    inhalt = response.content
    #print(inhalt)

    # Überprüfen Sie, ob der Inhalt der Antwort mit dem Inhalt der Basis-URL übereinstimmt
    if base_inhalt == inhalt:
        print(f"URL: {full_url}, Statuscode: {status}, Inhalt: gleich")
    else:
        print(f"URL: {full_url}, Statuscode: {status}, Inhalt: ungleich")