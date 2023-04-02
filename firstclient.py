import grpc
import blocking_pb2
import blocking_pb2_grpc
import time
import datetime
import uuid


unique_id=str(uuid.uuid1()) #client id
uidar=[]
file=[]

def main():
    channel=grpc.insecure_channel('localhost:50051')
    stub=blocking_pb2_grpc.activateserversStub(channel)
    x=1
    print("Requesting for list of replicas")
    response=stub.getserverlist(blocking_pb2.serverlistrequest(clientaddress=unique_id))
    string_list=response.items
    print(string_list)
    while(x==1):
        address=input("Type the address of the server you want to connect to: ")
        otherchannel=grpc.insecure_channel(address)
        stub=blocking_pb2_grpc.activateserversStub(otherchannel) 
        answer=input("You want to write a new file? ")
        if(answer=="yes"):
            f=input("Enter file name ")
            u=str(uuid.uuid1())
            c=input("Enter content of the file ")
            filestatus=stub.writefile(blocking_pb2.writerequest(filename=f,uuid=u,content=c))
            print(filestatus.status)
            print(filestatus.uid)
            print(datetime.datetime.fromtimestamp(int(filestatus.timestamp)))
            file.append(f)
            uidar.append(u)
        secondanswer=input("You want to update an existing file? ")
        if(secondanswer=="yes"):
            print("filenames ",file)
            print("Uids ",uidar)
            f=input("Enter file name ")
            u=input("Enter uid of the file ")
            c=input("Enter new content of the file ")
            filestatus=stub.writefile(blocking_pb2.writerequest(filename=f,uuid=u,content=c))
            print(filestatus.status)
            print(filestatus.uid)
            print(datetime.datetime.fromtimestamp(int(filestatus.timestamp)))
        thirdanswer=input("You want to read a file? ")
        if(thirdanswer=="yes"):
            print("Uids ",uidar)
            u=input("Enter uid of the file ")
            filecontent=stub.readfile(blocking_pb2.readrequest(id=u))
            print(filecontent.readstatus)
            print(filecontent.filename)
            print(filecontent.contents)
            print(datetime.datetime.fromtimestamp(int(filecontent.version)))
        fourthanswer=input("You want to delete a file? ")
        if(fourthanswer=="yes"):
            print("Uids ",uidar)
            u=input("Enter uid of the file ")
            deletereply=stub.delete(blocking_pb2.deleterequest(id=u))
            print(deletereply.reply)
            





main()