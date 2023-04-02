import blocking_pb2
import blocking_pb2_grpc
import grpc 
from concurrent import futures 
import os
filenames=[]
fileuid=[]

serverslist=[]
class activateserversServicer(blocking_pb2_grpc.activateserversServicer):
    def register(self, request, context):
        print("Join request from: ",request.serveraddress)
        reply=""
        if(len(serverslist)<=4):
            serverslist.append(request.serveraddress)
            if(len(serverslist)>1):
                channel=grpc.insecure_channel('localhost:50076')
                stub=blocking_pb2_grpc.activateserversStub(channel)
                informstatus=stub.informprimaryreplica(blocking_pb2.newreplica(replicaaddress=request.serveraddress))
                if(informstatus.done=="Success"):
                    reply="localhost:50076"
            else:
                reply="Success, you are primary replica"
        else:
            reply="Failed"
        return blocking_pb2.connectreply(reply=reply)
    
    def getserverlist(self, request, context):
        print("Server List request from ",request.clientaddress)
        return blocking_pb2.serverlist(items=serverslist)
 
        
def main():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    blocking_pb2_grpc.add_activateserversServicer_to_server(activateserversServicer(),server)
    server.add_insecure_port('localhost:50051')
    server.start()
    print("Register server started")
    server.wait_for_termination()

main()
    
