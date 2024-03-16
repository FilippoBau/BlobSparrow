import os
import argparse
from azure.storage.blob import BlobServiceClient, BlobClient

def download_blobs_from_container(account_url, container_name, local_folder):
    # Create Blob service client
    blob_service_client = BlobServiceClient(account_url=account_url)

    # Get client for the specified container
    container_client = blob_service_client.get_container_client(container_name)

    # List blobs in the container
    blobs_list = container_client.list_blobs()

    # Download each blob in the container
    for blob in blobs_list:
        # Get blob name
        blob_name = blob.name
        
        # Create local file path to download the blob
        local_file_path = os.path.join(local_folder, blob_name)

        # Create Blob client
        blob_client = BlobClient(account_url=account_url, container_name=container_name, blob_name=blob_name)

        # Download blob to local path
        with open(local_file_path, "wb") as f:
            download_stream = blob_client.download_blob()
            f.write(download_stream.readall())
        
        print(f"🏹 Blob '{blob_name}' captured and successfully downloaded.")

def main():
    parser = argparse.ArgumentParser(description="Blob Hunter - A tool to hunt and download blobs from Azure storage.")
    parser.add_argument("account_url", type=str, help="URL of the storage account (e.g., 'https://<storage_account_name>.blob.core.windows.net')")
    parser.add_argument("container_name", type=str, help="Name of the container")
    parser.add_argument("local_folder", type=str, help="Local path to download blobs")
    args = parser.parse_args()
    
    # Create local folder if it doesn't exist
    os.makedirs(args.local_folder, exist_ok=True)
    
    # Download blobs from the container
    download_blobs_from_container(args.account_url, args.container_name, args.local_folder)

if __name__ == "__main__":
    main()
