# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import audio_pb2 as audio__pb2


class ServicioAudioStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.descargarAudio = channel.unary_stream(
                '/ServicioAudio/descargarAudio',
                request_serializer=audio__pb2.PeticionDescargarAudio.SerializeToString,
                response_deserializer=audio__pb2.RespuestaChunkAudio.FromString,
                )


class ServicioAudioServicer(object):
    """Missing associated documentation comment in .proto file."""

    def descargarAudio(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServicioAudioServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'descargarAudio': grpc.unary_stream_rpc_method_handler(
                    servicer.descargarAudio,
                    request_deserializer=audio__pb2.PeticionDescargarAudio.FromString,
                    response_serializer=audio__pb2.RespuestaChunkAudio.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ServicioAudio', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ServicioAudio(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def descargarAudio(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ServicioAudio/descargarAudio',
            audio__pb2.PeticionDescargarAudio.SerializeToString,
            audio__pb2.RespuestaChunkAudio.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)