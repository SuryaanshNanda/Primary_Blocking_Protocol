# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import blocking_pb2 as blocking__pb2


class activateserversStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.register = channel.unary_unary(
                '/activateservers/register',
                request_serializer=blocking__pb2.connectrequest.SerializeToString,
                response_deserializer=blocking__pb2.connectreply.FromString,
                )
        self.informprimaryreplica = channel.unary_unary(
                '/activateservers/informprimaryreplica',
                request_serializer=blocking__pb2.newreplica.SerializeToString,
                response_deserializer=blocking__pb2.informstatus.FromString,
                )
        self.getserverlist = channel.unary_unary(
                '/activateservers/getserverlist',
                request_serializer=blocking__pb2.serverlistrequest.SerializeToString,
                response_deserializer=blocking__pb2.serverlist.FromString,
                )
        self.writefile = channel.unary_unary(
                '/activateservers/writefile',
                request_serializer=blocking__pb2.writerequest.SerializeToString,
                response_deserializer=blocking__pb2.filestatus.FromString,
                )
        self.readfile = channel.unary_unary(
                '/activateservers/readfile',
                request_serializer=blocking__pb2.readrequest.SerializeToString,
                response_deserializer=blocking__pb2.filecontent.FromString,
                )
        self.sendtoprimary = channel.unary_unary(
                '/activateservers/sendtoprimary',
                request_serializer=blocking__pb2.writerequest.SerializeToString,
                response_deserializer=blocking__pb2.confirm.FromString,
                )
        self.sendall = channel.unary_unary(
                '/activateservers/sendall',
                request_serializer=blocking__pb2.writerequest.SerializeToString,
                response_deserializer=blocking__pb2.confirm.FromString,
                )
        self.delete = channel.unary_unary(
                '/activateservers/delete',
                request_serializer=blocking__pb2.deleterequest.SerializeToString,
                response_deserializer=blocking__pb2.deletereply.FromString,
                )
        self.senddeltoprime = channel.unary_unary(
                '/activateservers/senddeltoprime',
                request_serializer=blocking__pb2.deleterequest.SerializeToString,
                response_deserializer=blocking__pb2.deletereply.FromString,
                )
        self.senddelall = channel.unary_unary(
                '/activateservers/senddelall',
                request_serializer=blocking__pb2.deleterequest.SerializeToString,
                response_deserializer=blocking__pb2.deletereply.FromString,
                )


class activateserversServicer(object):
    """Missing associated documentation comment in .proto file."""

    def register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def informprimaryreplica(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getserverlist(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def writefile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def readfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendtoprimary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendall(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def senddeltoprime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def senddelall(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_activateserversServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'register': grpc.unary_unary_rpc_method_handler(
                    servicer.register,
                    request_deserializer=blocking__pb2.connectrequest.FromString,
                    response_serializer=blocking__pb2.connectreply.SerializeToString,
            ),
            'informprimaryreplica': grpc.unary_unary_rpc_method_handler(
                    servicer.informprimaryreplica,
                    request_deserializer=blocking__pb2.newreplica.FromString,
                    response_serializer=blocking__pb2.informstatus.SerializeToString,
            ),
            'getserverlist': grpc.unary_unary_rpc_method_handler(
                    servicer.getserverlist,
                    request_deserializer=blocking__pb2.serverlistrequest.FromString,
                    response_serializer=blocking__pb2.serverlist.SerializeToString,
            ),
            'writefile': grpc.unary_unary_rpc_method_handler(
                    servicer.writefile,
                    request_deserializer=blocking__pb2.writerequest.FromString,
                    response_serializer=blocking__pb2.filestatus.SerializeToString,
            ),
            'readfile': grpc.unary_unary_rpc_method_handler(
                    servicer.readfile,
                    request_deserializer=blocking__pb2.readrequest.FromString,
                    response_serializer=blocking__pb2.filecontent.SerializeToString,
            ),
            'sendtoprimary': grpc.unary_unary_rpc_method_handler(
                    servicer.sendtoprimary,
                    request_deserializer=blocking__pb2.writerequest.FromString,
                    response_serializer=blocking__pb2.confirm.SerializeToString,
            ),
            'sendall': grpc.unary_unary_rpc_method_handler(
                    servicer.sendall,
                    request_deserializer=blocking__pb2.writerequest.FromString,
                    response_serializer=blocking__pb2.confirm.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=blocking__pb2.deleterequest.FromString,
                    response_serializer=blocking__pb2.deletereply.SerializeToString,
            ),
            'senddeltoprime': grpc.unary_unary_rpc_method_handler(
                    servicer.senddeltoprime,
                    request_deserializer=blocking__pb2.deleterequest.FromString,
                    response_serializer=blocking__pb2.deletereply.SerializeToString,
            ),
            'senddelall': grpc.unary_unary_rpc_method_handler(
                    servicer.senddelall,
                    request_deserializer=blocking__pb2.deleterequest.FromString,
                    response_serializer=blocking__pb2.deletereply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'activateservers', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class activateservers(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/activateservers/register',
            blocking__pb2.connectrequest.SerializeToString,
            blocking__pb2.connectreply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def informprimaryreplica(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/activateservers/informprimaryreplica',
            blocking__pb2.newreplica.SerializeToString,
            blocking__pb2.informstatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getserverlist(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/activateservers/getserverlist',
            blocking__pb2.serverlistrequest.SerializeToString,
            blocking__pb2.serverlist.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def writefile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/activateservers/writefile',
            blocking__pb2.writerequest.SerializeToString,
            blocking__pb2.filestatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def readfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/activateservers/readfile',
            blocking__pb2.readrequest.SerializeToString,
            blocking__pb2.filecontent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendtoprimary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/activateservers/sendtoprimary',
            blocking__pb2.writerequest.SerializeToString,
            blocking__pb2.confirm.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendall(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/activateservers/sendall',
            blocking__pb2.writerequest.SerializeToString,
            blocking__pb2.confirm.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/activateservers/delete',
            blocking__pb2.deleterequest.SerializeToString,
            blocking__pb2.deletereply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def senddeltoprime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/activateservers/senddeltoprime',
            blocking__pb2.deleterequest.SerializeToString,
            blocking__pb2.deletereply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def senddelall(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/activateservers/senddelall',
            blocking__pb2.deleterequest.SerializeToString,
            blocking__pb2.deletereply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
