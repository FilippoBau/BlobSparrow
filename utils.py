def read_blob_names_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            blob_names = [line.strip() for line in file if line.strip()]
        return blob_names
    except FileNotFoundError:
        print(f"Errore: Il file '{file_path}' non è stato trovato.")
        return []
    except Exception as e:
        print(f"Errore durante la lettura del file '{file_path}': {e}")
        return []
    
def download_blob(blob_client, local_file_path):
    with open(local_file_path, "wb") as f:
        download_stream = blob_client.download_blob()
        f.write(download_stream.readall())



