from azure.core.exceptions import HttpResponseError
from azure.storage.blob import BlobServiceClient, BlobClient
import os


def read_names_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            names = [line.strip() for line in file if line.strip()]
        return names
    except FileNotFoundError:
        print(f"Error: file '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error while reading the file '{file_path}': {e}")
        return []
    
def download_blob(blob_client, local_file_path):
    with open(local_file_path, "wb") as f:
        download_stream = blob_client.download_blob()
        f.write(download_stream.readall())

def print_logo():
    logo =r'''
 ___  _       _     ___                                 
| . >| | ___ | |_  / __> ___  ___  _ _  _ _  ___  _ _ _ 
| . \| |/ . \| . \ \__ \| . \<_> || '_>| '_>/ . \| | | |
|___/|_|\___/|___/ <___/|  _/<___||_|  |_|  \___/|__/_/ 
                        |_|                                
'''
    print(logo)




def download_blob_from_list(account_url, container_name, blob_names, local_folder):
    found=False
    local_folder_cont = os.path.join(local_folder,container_name)
    os.makedirs(local_folder_cont,exist_ok=True)
    for blob_name in blob_names:
        try:
            blob_client = BlobClient(account_url=account_url, container_name=container_name, blob_name=blob_name)
            local_file_path = os.path.join(local_folder_cont, blob_name)
            download_blob(blob_client, local_file_path)
            print(f"💰 '{blob_name}' successfully downloaded.")
            found=True
        except Exception as e:
            os.remove(local_file_path)
    if not found:
        os.rmdir(local_folder_cont) 


def download_blobs_from_container(account_url, container_name, local_folder, blob_file):
    try:
        blob_service_client = BlobServiceClient(account_url=account_url)
        container_client = blob_service_client.get_container_client(container_name)
        blobs_list = container_client.list_blobs()
        blob_names = [blob.name for blob in blobs_list]
        download_blob_from_list(account_url, container_name, blob_names, local_folder)
    except HttpResponseError as e:
        handle_http_response_error(e, account_url, container_name, local_folder,blob_file)
    except Exception as e:
        print(f"🌊 An error occurred: {str(e)}")            


def handle_http_response_error(e, account_url, container_name, local_folder,blob_file):
    if e.status_code == 403 and "AuthorizationFailure" in str(e):
        blob_names = read_names_from_file(blob_file)
        download_blob_from_list(account_url, container_name, blob_names, local_folder)
    else:
        print(f"🌴  HTTP Error:{str(e)}")
