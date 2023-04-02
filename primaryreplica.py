import blocking_pb2
import blocking_pb2_grpc
import grpc 
from concurrent import futures 
import os

filenames=[]
fileuid=[]
serverslist=[]
class activateserversServicer(blocking_pb2_grpc.activateserversServicer):
    def readfile(self, request, context):
        if(request.id in fileuid):
            x=fileuid.index(request.id)
            name=filenames[x]
            if(name in filenames and name!="Empty"):
                exfile=open(os.path.join('maindirectory',name), 'r')
                cont=exfile.read()
                readstatus="Success"
                filename=name
                contents=cont
                version=os.path.getmtime(os.path.join('maindirectory',name))
                return blocking_pb2.filecontent(readstatus=readstatus,filename=filename,contents=contents,version=version)
            else:
                readstatus="File is deleted"
                return blocking_pb2.filecontent(readstatus=readstatus)
        else:
                readstatus="File does not exist"
                return blocking_pb2.filecontent(readstatus=readstatus)
        

    def informprimaryreplica(self, request, context):
        print("Join request to register server from: ",request.replicaaddress)
        done=""
        if(len(serverslist)<=3):
            serverslist.append(request.replicaaddress)
            done="Success"
        else:
            print("No space for more replicas")
            done="Failed"
        return blocking_pb2.informstatus(done=done)
    
    def sendtoprimary(self, request, context):
        if(os.path.exists('maindirectory')==False):
            os.mkdir('maindirectory')
        if(request.filename not in filenames and request.uuid not in fileuid):
            print("Creating new file",request.filename)
            newfile=open(os.path.join('maindirectory',request.filename), 'w')
            newfile.write(request.content)
            filenames.append(request.filename)
            fileuid.append(request.uuid)
            count=0
            for address in serverslist:
                channel=grpc.insecure_channel(address)
                stub=blocking_pb2_grpc.activateserversStub(channel)
                confirm=stub.sendall(blocking_pb2.writerequest(filename=request.filename,uuid=request.uuid,content=request.content))
                if(confirm.reply=="Success"):
                    count=count+1
            if(count==len(serverslist)):
                reply="go ahead"
            else:
                reply="failed"
            return blocking_pb2.confirm(reply=reply)
        elif(request.filename in filenames and request.uuid in fileuid):
            print("Modifying existing file",request.filename)
            newfile=open(os.path.join('maindirectory',request.filename), 'w')
            newfile.write(request.content)
            #filenames.append(request.filename)
            #fileuid.append(request.uuid)
            count=0
            for address in serverslist:
                channel=grpc.insecure_channel(address)
                stub=blocking_pb2_grpc.activateserversStub(channel)
                confirm=stub.sendall(blocking_pb2.writerequest(filename=request.filename,uuid=request.uuid,content=request.content))
                if(confirm.reply=="Success"):
                    count=count+1
            if(count==len(serverslist)):
                reply="go ahead"
            else:
                reply="failed"
            return blocking_pb2.confirm(reply=reply)
        elif(request.filename not in filenames and request.uuid in fileuid):
            return blocking_pb2.confirm(reply="File is deleted")
        elif(request.filename in filenames and request.uuid not in fileuid):
            return blocking_pb2.confirm(reply="File exists with the same name")

        
    
    def senddeltoprime(self, request, context):
        if(request.id in fileuid):
            fname=filenames[fileuid.index(request.id)]
            if(fname in filenames and fname!="Empty"):
                os.remove(os.path.join('maindirectory',fname))
                filenames[filenames.index(fname)]="Empty" 
                count=0
                for address in serverslist:
                    channel=grpc.insecure_channel(address)
                    stub=blocking_pb2_grpc.activateserversStub(channel)
                    confirm=stub.senddelall(blocking_pb2.deleterequest(id=request.id))
                    if(confirm.reply=="Success"):
                        count=count+1
                if(count==len(serverslist)):
                    reply="go ahead"
                else:
                    reply="failed"
                return blocking_pb2.deletereply(reply=reply)
            
    def delete(self, request, context):
        if(request.id in fileuid):
            fname=filenames[fileuid.index(request.id)]
            if(fname in filenames and fname!="Empty"):
                os.remove(os.path.join('maindirectory',fname))
                filenames[filenames.index(fname)]="Empty" 
                count=0
                for address in serverslist:
                    channel=grpc.insecure_channel(address)
                    stub=blocking_pb2_grpc.activateserversStub(channel)
                    confirm=stub.senddelall(blocking_pb2.deleterequest(id=request.id))
                    if(confirm.reply=="Success"):
                        count=count+1
                if(count==len(serverslist)):
                    reply="Success"
                else:
                    reply="Failed"
                return blocking_pb2.deletereply(reply=reply)
            else:
                return blocking_pb2.deletereply(reply="File is already deleted")
        else:
            return blocking_pb2.deletereply(reply="File does not exist")
    
    def writefile(self, request, context):
        if(os.path.exists('maindirectory')==False):
            os.mkdir('maindirectory')
        if(request.filename not in filenames and request.uuid not in fileuid):
            print("Creating new file",request.filename)
            newfile=open(os.path.join('maindirectory',request.filename), 'w')
            newfile.write(request.content)
            filenames.append(request.filename)
            fileuid.append(request.uuid)
            thepath=os.path.join('maindirectory',request.filename)
            modtime=os.path.getmtime(thepath)
            count=0
            for address in serverslist:
                channel=grpc.insecure_channel(address)
                stub=blocking_pb2_grpc.activateserversStub(channel)
                confirm=stub.sendall(blocking_pb2.writerequest(filename=request.filename,uuid=request.uuid,content=request.content))
                if(confirm.reply=="Success"):
                    count=count+1
            if(count==len(serverslist)):
                reply="Success"
            else:
                reply="failed"
            return blocking_pb2.filestatus(status=reply,uid=request.uuid,timestamp=modtime)
        elif(request.filename in filenames and request.uuid in fileuid):
            print("Modifying existing file",request.filename)
            newfile=open(os.path.join('maindirectory',request.filename), 'w')
            newfile.write(request.content)
            #filenames.append(request.filename)
            #fileuid.append(request.uuid)
            count=0
            for address in serverslist:
                channel=grpc.insecure_channel(address)
                stub=blocking_pb2_grpc.activateserversStub(channel)
                confirm=stub.sendall(blocking_pb2.writerequest(filename=request.filename,uuid=request.uuid,content=request.content))
                if(confirm.reply=="Success"):
                    count=count+1
            if(count==len(serverslist)):
                reply="Success"
            else:
                reply="failed"
            return blocking_pb2.confirm(reply=reply)
        elif(request.filename not in filenames and request.uuid in fileuid):
            return blocking_pb2.confirm(reply="File is deleted")
        elif(request.filename in filenames and request.uuid not in fileuid):
            return blocking_pb2.confirm(reply="File exists with the same name")
    
        



def main():
    channel=grpc.insecure_channel('localhost:50051')
    stub=blocking_pb2_grpc.activateserversStub(channel)
    connectreply=stub.register(blocking_pb2.connectrequest(serveraddress='localhost:50076'))
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    blocking_pb2_grpc.add_activateserversServicer_to_server(activateserversServicer(),server)
    print("new server has started")
    server.add_insecure_port('localhost:50076')
    server.start()
    print(connectreply.reply)
    server.wait_for_termination()

main()

        
