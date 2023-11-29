# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import client.grpc.kosts_pb2 as kosts__pb2


class KostsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetKost = channel.unary_unary(
            '/kosts.Kosts/GetKost',
            request_serializer=kosts__pb2.KostRequest.SerializeToString,
            response_deserializer=kosts__pb2.KostResponse.FromString,
        )
        self.GetKosts = channel.unary_unary(
            '/kosts.Kosts/GetKosts',
            request_serializer=kosts__pb2.KostListRequest.SerializeToString,
            response_deserializer=kosts__pb2.KostListResponse.FromString,
        )
        self.CreateKost = channel.unary_unary(
            '/kosts.Kosts/CreateKost',
            request_serializer=kosts__pb2.KostCreateRequest.SerializeToString,
            response_deserializer=kosts__pb2.KostResponse.FromString,
        )
        self.UpdateKost = channel.unary_unary(
            '/kosts.Kosts/UpdateKost',
            request_serializer=kosts__pb2.KostUpdateRequest.SerializeToString,
            response_deserializer=kosts__pb2.KostResponse.FromString,
        )
        self.DeleteKost = channel.unary_unary(
            '/kosts.Kosts/DeleteKost',
            request_serializer=kosts__pb2.KostDeleteRequest.SerializeToString,
            response_deserializer=kosts__pb2.KostDeleteResponse.FromString,
        )


class KostsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetKost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetKosts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateKost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateKost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteKost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KostsServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetKost': grpc.unary_unary_rpc_method_handler(
            servicer.GetKost,
            request_deserializer=kosts__pb2.KostRequest.FromString,
            response_serializer=kosts__pb2.KostResponse.SerializeToString,
        ),
        'GetKosts': grpc.unary_unary_rpc_method_handler(
            servicer.GetKosts,
            request_deserializer=kosts__pb2.KostListRequest.FromString,
            response_serializer=kosts__pb2.KostListResponse.SerializeToString,
        ),
        'CreateKost': grpc.unary_unary_rpc_method_handler(
            servicer.CreateKost,
            request_deserializer=kosts__pb2.KostCreateRequest.FromString,
            response_serializer=kosts__pb2.KostResponse.SerializeToString,
        ),
        'UpdateKost': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateKost,
            request_deserializer=kosts__pb2.KostUpdateRequest.FromString,
            response_serializer=kosts__pb2.KostResponse.SerializeToString,
        ),
        'DeleteKost': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteKost,
            request_deserializer=kosts__pb2.KostDeleteRequest.FromString,
            response_serializer=kosts__pb2.KostDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'kosts.Kosts', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class Kosts(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetKost(request,
                target,
                options=(),
                channel_credentials=None,
                call_credentials=None,
                insecure=False,
                compression=None,
                wait_for_ready=None,
                timeout=None,
                metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kosts.Kosts/GetKost',
                                             kosts__pb2.KostRequest.SerializeToString,
                                             kosts__pb2.KostResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetKosts(request,
                 target,
                 options=(),
                 channel_credentials=None,
                 call_credentials=None,
                 insecure=False,
                 compression=None,
                 wait_for_ready=None,
                 timeout=None,
                 metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kosts.Kosts/GetKosts',
                                             kosts__pb2.KostListRequest.SerializeToString,
                                             kosts__pb2.KostListResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateKost(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kosts.Kosts/CreateKost',
                                             kosts__pb2.KostCreateRequest.SerializeToString,
                                             kosts__pb2.KostResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateKost(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kosts.Kosts/UpdateKost',
                                             kosts__pb2.KostUpdateRequest.SerializeToString,
                                             kosts__pb2.KostResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteKost(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kosts.Kosts/DeleteKost',
                                             kosts__pb2.KostDeleteRequest.SerializeToString,
                                             kosts__pb2.KostDeleteResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
