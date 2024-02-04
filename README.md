# StorageHunter

A tool that can extract all the blobs from storage accounts that allow anonymous access

## Introduction

This Python script allows you to download files from an Azure Storage Account using the Azure Storage Blob service.

## Prerequisites

Before running this script, ensure you have installed the `azure-storage-blob` library using pip. You can install it with the following command:

```
pip install azure-storage-blob
```

## Usage

1. Run the script using Python:

   ```
   python azure_blob_downloader.py
   ```

2. Enter the name of your Azure Storage Account when prompted.
3. Enter the destination folder path where you want to save the downloaded files.

## Notes

- Make sure you have the necessary permissions to access the Azure Storage Account.
- This script requires an active internet connection to access the Azure Storage Account.
- If the destination folder does not exist, the script will create it automatically.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
