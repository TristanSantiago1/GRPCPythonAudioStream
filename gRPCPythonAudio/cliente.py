import pyaudio
import grpc
import audio_pb2
import audio_pb2_grpc

def streamAudio(stub, nombre_archivo):
    repsuesta = stub.descargarAudio(audio_pb2.PeticionDescargarAudio(nombre = nombre_archivo))
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=2, rate= 48000, output= True)
    print("Reproduciendo audio: " + nombre_archivo)
    for audio_chunk in repsuesta:
        print(".", end="", flush=True)
        stream.write(audio_chunk.datos)
    print("\nRecepcion de datos correcta.")    
    print("\nReproduccion terminada.", end="\n")

def run():
    puerto = "9000"
    canal = grpc.insecure_channel("localhost:"+puerto)
    stub = audio_pb2_grpc.ServicioAudioStub(canal) 
    try:
        nombre_archivo= "anyma.wav"
        streamAudio(stub, nombre_archivo)
    except:
        pass
    finally:
        canal.close()



if __name__ == "__main__":
    run()