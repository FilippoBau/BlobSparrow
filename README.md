# BlobSparrow

BlobSparrow is a tool designed to hunt and download blobs from Azure storage with anonymous access enabled. It provides a straightforward way to download blobs using a wordlist for blob names.

## Features

- Download blobs from an Azure storage account.
- Specify a container or use a list of container names.
- Download to a specified local path.
- Use different wordlists for blob names.

## Prerequisites

- Python 3.6 or higher
- Azure Storage SDK for Python
- `concurrent.futures.ThreadPoolExecutor` for parallel downloads

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/BlobSparrow.git
   cd BlobSparrow
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python hunter.py -a <storage_account_url> [-c <container_name>] [-l <local_path>] [-w <wordlist>]
```

### Arguments

- `-a`: URL of the storage account (e.g., `https://<storage_account_name>.blob.core.windows.net`) (required)
- `-c`: Name of the container (optional). If not provided, it will use a list of container names from `container_names.txt`.
- `-l`: Local path to download blobs (optional, default is `./loot`).
- `-w`: Wordlist for blob names (optional, default is `./wordlist/normal.txt`)

### Examples

1. Download blobs from a specific container to the default path:

   ```bash
   python hunter.py -a https://mystorageaccount.blob.core.windows.net -c mycontainer
   ```

2. Download blobs from a list of containers to a specified path using a custom wordlist:

   ```bash
   python hunter.py -a https://mystorageaccount.blob.core.windows.net -l ./myloot -w ./mywordlist.txt
   ```

3. Download blobs using a predefined "crazy" wordlist:

   ```bash
   python hunter.py -a https://mystorageaccount.blob.core.windows.net -w crazy
   ```

## File Structure

- `hunter.py`: Main script to run the Blob Hunter tool.
- `utils_blob.py`: Utility functions for downloading blobs and printing the logo.
- `wordlist/normal.txt`: Default wordlist for blob names.
- `container_names.txt`: List of container names to use if no container name is provided.

## Credits

The lists of container names and blob names are from:

- https://github.com/emadshanab/WordLists-20111129/blob/master/Filenames_or_Directories_All.wordlist
- https://github.com/koaj/aws-s3-bucket-wordlist/blob/master/list.txt
