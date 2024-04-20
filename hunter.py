import os
import argparse
from utils_blob import print_logo, download_blobs_from_container, read_names_from_file



def main():
    parser = argparse.ArgumentParser(description="Blob Hunter - A tool to hunt and download blobs from Azure storage.")
    parser.add_argument("-a", type=str, help="URL of the storage account (e.g., 'https://<storage_account_name>.blob.core.windows.net')")
    parser.add_argument("-c", type=str, help="Name of the container", nargs='?', default=None)
    parser.add_argument("-l", type=str, help="Local path to download blobs", nargs='?', default="./loot")
    args = parser.parse_args()

    os.makedirs(args.l, exist_ok=True)
    print_logo()
    print("🦜 Welcome! Setting sail to plunder Azure blobs...")
    if args.c is None:
        names=read_names_from_file("./container_names.txt")
    else:
        names=[args.c]
    for name in names:
        download_blobs_from_container(args.a, name, args.l)
    print("🦜 All plundered blobs safely stowed away!")

if __name__ == "__main__":
    main()
