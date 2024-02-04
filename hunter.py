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

def download_files(storage_account_name, destination_folder):

    try:
        blob_service_client = BlobServiceClient.from_connection_string(f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};")
        for container in blob_service_client.list_containers():
            print(f"Container: {container.name}")
            for blob in blob_service_client.get_container_client(container.name).list_blobs():
                print(f"Downloading: {blob.name}")
                with open(os.path.join(destination_folder, blob.name), "wb") as file:
                    blob_client = blob_service_client.get_blob_client(container=container.name, blob=blob.name)
                    file.write(blob_client.download_blob().readall())
    except Exception as e:
        print(f"Error accessing the storage account: {e}")

if __name__ == "__main__":
    storage_account_name = input("Enter the name of your Azure Storage Account: ")
    destination_folder = input("Enter the destination folder path: ")

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    download_files(storage_account_name, destination_folder)

