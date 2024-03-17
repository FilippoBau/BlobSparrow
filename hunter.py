import os
import argparse
from utils import read_blob_names_from_file, download_blob
from azure.core.exceptions import HttpResponseError
from azure.storage.blob import BlobServiceClient, BlobClient

def download_blob_from_list(account_url, container_name, blob_names, local_folder):
    for blob_name in blob_names:
        try:
            blob_client = BlobClient(account_url=account_url, container_name=container_name, blob_name=blob_name)
            local_file_path = os.path.join(local_folder, blob_name)
            download_blob(blob_client, local_file_path)
            print(f"🏴‍☠️ '{blob_name}' successfully downloaded.")
        except Exception as e:
            print(f"🏝️ Error downloading '{blob_name}': {str(e)}")


def handle_http_response_error(e, account_url, container_name, local_folder):
    if e.status_code == 403 and "AuthorizationFailure" in str(e):
        blob_names = read_blob_names_from_file("blob_name.txt")
        download_blob_from_list(account_url, container_name, blob_names, local_folder)
    else:
        print(f"🌴 HTTP Error: {str(e)}")


def download_blobs_from_container(account_url, container_name, local_folder):
    try:
        blob_service_client = BlobServiceClient(account_url=account_url)
        container_client = blob_service_client.get_container_client(container_name)
        blobs_list = container_client.list_blobs()
        blob_names = [blob.name for blob in blobs_list]
        download_blob_from_list(account_url, container_name, blob_names, local_folder)
    except HttpResponseError as e:
        handle_http_response_error(e, account_url, container_name, local_folder)
    except Exception as e:
        print(f"🌊 An error occurred: {str(e)}")


def main():
    parser = argparse.ArgumentParser(description="Blob Hunter - A tool to hunt and download blobs from Azure storage.")
    parser.add_argument("account_url", type=str, help="URL of the storage account (e.g., 'https://<storage_account_name>.blob.core.windows.net')")
    parser.add_argument("container_name", type=str, help="Name of the container")
    parser.add_argument("local_folder", type=str, help="Local path to download blobs")
    args = parser.parse_args()

    os.makedirs(args.local_folder, exist_ok=True)

    print("🦜 Welcome! Setting sail to plunder Azure blobs...")
    download_blobs_from_container(args.account_url, args.container_name, args.local_folder)
    print("💰 All plundered blobs safely stowed away!")

if __name__ == "__main__":
    main()
