import os
import dropbox
from dropbox.files import WriteMode 

class TransferData():
    def __init__(self,accessToken):
        self.accessToken=accessToken

    def uploadFile(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.accessToken)

        for root,dirs,files in os.walk(file_from):
            for fileName in files:
                local_path=os.path.join(root,fileName)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                with open(local_path,'rb')as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode("overwrite"))
          
def main():
    accessToken='IjNQ7UdZDicAAAAAAAAAAfMPhNlUI3Z2c1XTUKJIHOjZIwdG-pbph3mUafo5zt99'
    TransferData_obj=TransferData(accessToken)
    file_from=input("Enter the file to be uploaded: ")
    file_to=input("Enter the path to upload in dropbox: ")
    TransferData_obj.uploadFile(file_from,file_to)
    print("File has been successfully transferred !!!")

main()