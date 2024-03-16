starter= '''
                                                                                                                                 
 .M"""bgd   mm                                                   `7MMF'  `7MMF'                          mm                      
,MI    "Y   MM                                                     MM      MM                            MM                      
`MMb.     mmMMmm   ,pW"Wq.  `7Mb,od8  ,6"Yb.   .P"Ybmmm  .gP"Ya    MM      MM  `7MM  `7MM  `7MMpMMMb.  mmMMmm   .gP"Ya  `7Mb,od8 
  `YMMNq.   MM    6W'   `Wb   MM' "' 8)   MM  :MI  I8   ,M'   Yb   MMmmmmmmMM    MM    MM    MM    MM    MM    ,M'   Yb   MM' "' 
.     `MM   MM    8M     M8   MM      ,pm9MM   WmmmP"   8M""""""   MM      MM    MM    MM    MM    MM    MM    8M""""""   MM     
Mb     dM   MM    YA.   ,A9   MM     8M   MM  8M        YM.    ,   MM      MM    MM    MM    MM    MM    MM    YM.    ,   MM     
P"Ybmmd"    `Mbmo  `Ybmd9'  .JMML.   `Moo9^Yo. YMMMMMb   `Mbmmd' .JMML.  .JMML.  `Mbod"YML..JMML  JMML.  `Mbmo  `Mbmmd' .JMML.   
                                              6'     dP                                                                          
                                              Ybmmmd'                                                                           
'''
print(starter)

import os
from azure.storage.blob import BlobServiceClient

def load_container_names(file_path):
    try:
        with open(file_path, "r") as file:
            container_names = [line.strip() for line in file.readlines() if line.strip()]
        return container_names
    except Exception as e:
        print(f"Errore durante il caricamento dei nomi dei container dal file: {e}")
        return []

def download_files(storage_account_name, destination_folder, container_names=None):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};")

        container_names = container_names or load_container_names("container_names.txt")

        for container_name in container_names:
            container_client = blob_service_client.get_container_client(container_name)
            if not container_client.exists():
                print(f"Container '{container_name}' non trovato.")
                continue

            print(f"Container: {container_name}")

            try:
                blobs = list(container_client.list_blobs())
            except Exception as e:
                print(f"Errore durante l'elenco dei blob nel container '{container_name}': {e}")
                continue

            if not blobs:
                print(f"Il container '{container_name}' non contiene alcun blob.")
                continue

            for blob in blobs:
                print(f"Downloading: {blob.name}")
                with open(os.path.join(destination_folder, blob.name), "wb") as file:
                    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob.name)
                    file.write(blob_client.download_blob().readall())
            break  # Esce dal ciclo se il download è stato eseguito con successo da un container

        else:
            print("Nessun container valido trovato.")

    except Exception as e:
        print(f"Errore durante l'accesso all'account di archiviazione: {e}")

if __name__ == "__main__":
    storage_account_name = input("Inserisci il nome del tuo Azure Storage Account: ")
    destination_folder = input("Inserisci il percorso della cartella di destinazione: ")
    container_names_file = input("Inserisci il percorso del file contenente i nomi dei container: ")

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    download_files(storage_account_name, destination_folder, load_container_names(container_names_file))
