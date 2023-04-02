import blocking_pb2
import blocking_pb2_grpc
import grpc 
from concurrent import futures 
import os 
fileuid=[]
filenames=[]

class activateserversServicer(blocking_pb2_grpc.activateserversServicer):
    def readfile(self, request, context):
        if(request.id in fileuid):
            x=fileuid.index(request.id)
            name=filenames[x]
            if(name in filenames and name!="Empty"):
                exfile=open(os.path.join('directorytwo',name), 'r')
                cont=exfile.read()
                readstatus="Success"
                filename=name
                contents=cont
                version=os.path.getmtime(os.path.join('directorytwo',name))
                return blocking_pb2.filecontent(readstatus=readstatus,filename=filename,contents=contents,version=version)
            else:
                readstatus="File is deleted"
                return blocking_pb2.filecontent(readstatus=readstatus)
        else:
                readstatus="File does not exist"
                return blocking_pb2.filecontent(readstatus=readstatus)

        

    def delete(self, request, context):
        if(request.id in fileuid):
            fname=filenames[fileuid.index(request.id)]
            if(fname in filenames and fname!="Empty"):
                channel=grpc.insecure_channel('localhost:50076')
                stub=blocking_pb2_grpc.activateserversStub(channel)
                dr=stub.senddeltoprime(blocking_pb2.deleterequest(id=request.id))
                if(dr.reply=="go ahead"):
                    message="Success"
                return blocking_pb2.deletereply(reply=message)
            else:
                return blocking_pb2.deletereply(reply="File is already deleted")
        else:
            return blocking_pb2.deletereply(reply="File does not exist")
        






    def sendall(self, request, context):
        if(request.filename not in filenames and request.uuid not in fileuid):
            if(os.path.exists('directorytwo')==False):
                os.mkdir('directorytwo')    
            newfile=open(os.path.join('directorytwo',request.filename), 'w')
            newfile.write(request.content)
            if(request.filename not in filenames and request.uuid not in fileuid):
                filenames.append(request.filename)
                fileuid.append(request.uuid)
            reply="Success"
            return blocking_pb2.confirm(reply=reply)

    def senddelall(self, request, context):
        if(request.id in fileuid):
            fname=filenames[fileuid.index(request.id)]
            if(fname in filenames):
                os.remove(os.path.join('directorytwo',fname))
                filenames[filenames.index(fname)]="Empty"
                tell="Success"
                return blocking_pb2.deletereply(reply=tell)
            else:
                return blocking_pb2.deletereply(reply="Failed")


        
    def writefile(self, request, context):
        print(request.filename,request.uuid,request.content)
        if(os.path.exists('directorytwo')==False):
            os.mkdir('directorytwo')
        if(request.filename not in filenames and request.uuid not in fileuid):
            print("Creating new file ", request.filename)
            channel=grpc.insecure_channel('localhost:50076')
            stub=blocking_pb2_grpc.activateserversStub(channel)
            confirm=stub.sendtoprimary(blocking_pb2.writerequest(filename=request.filename,uuid=request.uuid,content=request.content))
            if(confirm.reply=="go ahead"):
                thepath=os.path.join('directorytwo',request.filename)
                creationtime=os.path.getmtime(thepath)
                status="Success"
                print(status,request.uuid,creationtime)
                return blocking_pb2.filestatus(status=status,uid=request.uuid,timestamp=creationtime)
        elif(request.filename not in filenames and request.uuid in fileuid):
            return blocking_pb2.filestatus(status="File deleted") 
        elif(request.filename in filenames and request.uuid not in fileuid):
            return blocking_pb2.filestatus(status="File with the same name exists")
        elif(request.filename in filenames and request.uuid in fileuid):
            print("Modifying existing file ", request.filename)
            channel=grpc.insecure_channel('localhost:50076')
            stub=blocking_pb2_grpc.activateserversStub(channel)
            confirm=stub.sendtoprimary(blocking_pb2.writerequest(filename=request.filename,uuid=request.uuid,content=request.content))
            if(confirm.reply=="go ahead"):
                thepath=os.path.join('directorytwo',request.filename)
                modtime=os.path.getmtime(thepath)
                status="Success"
                return blocking_pb2.filestatus(status=status,uid=request.uuid,timestamp=modtime)
         
           
            #newfile=open(os.path.join('directoryone',request.filename), 'w')
            #newfile.write(request.content)
            #filenames.append(request.filename)
            #fileuid.append(request.uuid)




    

def main(): 
    channel=grpc.insecure_channel('localhost:50051')
    stub=blocking_pb2_grpc.activateserversStub(channel)
    print("Joining the registery server")
    connectreply=stub.register(blocking_pb2.connectrequest(serveraddress='localhost:50081'))
    print("Success,primary replica is",connectreply.reply)
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    blocking_pb2_grpc.add_activateserversServicer_to_server(activateserversServicer(),server)
    print("new server has started")
    server.add_insecure_port('localhost:50081')
    server.start()
    server.wait_for_termination()

main()