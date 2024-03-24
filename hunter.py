import os
import argparse
from utils_blob import print_logo, download_blobs_from_container, read_names_from_file



def main():
    parser = argparse.ArgumentParser(description="Blob Hunter - A tool to hunt and download blobs from Azure storage.")
    parser.add_argument("account_url", type=str, help="URL of the storage account (e.g., 'https://<storage_account_name>.blob.core.windows.net')")
    parser.add_argument("container_name", type=str, help="Name of the container", nargs='?', default=None)
    parser.add_argument("local_folder", type=str, help="Local path to download blobs", nargs='?', default="./loot")
    args = parser.parse_args()

    os.makedirs(args.local_folder, exist_ok=True)
    print_logo()
    print("🦜 Welcome! Setting sail to plunder Azure blobs...")
    if args.container_name is None:
        names=read_names_from_file("./container_names.txt")
    else:
        names=[args.container_name]
    for name in names:
        download_blobs_from_container(args.account_url, name, args.local_folder)
    print("🦜 All plundered blobs safely stowed away!")

if __name__ == "__main__":
    main()
