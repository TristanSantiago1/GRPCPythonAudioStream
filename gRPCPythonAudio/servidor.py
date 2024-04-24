from concurrent import futures
import audio_pb2_grpc
import audio_pb2

import grpc


class ServicioAudioStream(audio_pb2_grpc.ServicioAudio):
    def descargarAudio(self, peticion, contexto):
        print("\n\nEviando archivo : {0}".format(peticion.nombre))
        chunk = 1024
        with open("recursos/{0}".format(peticion.nombre),"rb") as contenido :
            while chunk_bytes := contenido.read(chunk):
                yield audio_pb2.RespuestaChunkAudio(datos = chunk_bytes)
                print(".", end="", flush= True)


def servidor():
    servicio = ServicioAudioStream()
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    puerto = "9000"
    audio_pb2_grpc.add_ServicioAudioServicer_to_server(servicio, servidor)
    servidor.add_insecure_port("[::]:"+puerto)
    servidor.start()
    print("Servidor GRPC en ejecucioón en el puerto :" + puerto)
    try:
        servidor.wait_for_termination()
    except KeyboardInterrupt:
        pass
    finally:
        servidor.stop(0)
        

if __name__ == "__main__":
    servidor()

