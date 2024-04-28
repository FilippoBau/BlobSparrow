import os
import argparse
from concurrent.futures import ThreadPoolExecutor
from utils_blob import print_logo, download_blobs_from_container, read_names_from_file

def download_from_container(storage_account_url, container_name, local_path, blob_file):
    download_blobs_from_container(storage_account_url, container_name, local_path, blob_file)

def main():
    parser = argparse.ArgumentParser(description="Blob Hunter - A tool to hunt and download blobs from Azure storage.")
    parser.add_argument("-a", type=str, help="URL of the storage account (e.g., 'https://<storage_account_name>.blob.core.windows.net')")
    parser.add_argument("-c", type=str, help="Name of the container", nargs='?', default=None)
    parser.add_argument("-l", type=str, help="Local path to download blobs", nargs='?', default="./loot")
    parser.add_argument("-w", type=str, help="Wordlist for blob names", nargs='?',  default="./wordlist/normal.txt")

    args = parser.parse_args()

    if args.w == "crazy": 
        blob_file = "./wordlist/crazy.txt"
    elif args.w == "insane":
        blob_file = "./wordlist/insane.txt"
    else:
        blob_file = args.w

    os.makedirs(args.l,exist_ok=True)
    print_logo()
    print(blob_file)
    print("🦜 Welcome! Setting sail to plunder Azure blobs...")

    if args.c is None:
        names = read_names_from_file("./container_names.txt")
    else:
        names = [args.c]

    with ThreadPoolExecutor(max_workers=5) as executor:
        for name in names:
            print(name)
            executor.submit(download_from_container, args.a, name, args.l, blob_file)

    print("🦜 All plundered blobs safely stowed away!")

if __name__ == "__main__":
    main()
