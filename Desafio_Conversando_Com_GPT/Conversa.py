import os
from openai import OpenAI
from gtts import gTTS
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play

# Inicializa o cliente com a sua chave
client = OpenAI(api_key="SUA_CHAVE_AQUI")

def capturar_voz():
    rec = sr.Recognizer()
    with sr.Microphone() as fonte:
        print("\nOuvindo... Pode falar!")
        rec.adjust_for_ambient_noise(fonte)
        audio = rec.listen(fonte)
        
    with open("input.wav", "wb") as f:
        f.write(audio.get_wav_data())
    return "input.wav"

def transcricao_whisper(caminho_audio):
    print("Transcrevendo com Whisper...")
    with open(caminho_audio, "rb") as audio_file:
        # Nova sintaxe da versão 1.0+
        transcript = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
    return transcript.text

def responder_chatgpt(texto_usuario):
    print(f"Você: {texto_usuario}")
    # Nova sintaxe da versão 1.0+
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": texto_usuario}]
    )
    return response.choices[0].message.content

def sintetizar_voz(texto_resposta):
    print(f"ChatGPT: {texto_resposta}")
    tts = gTTS(text=texto_resposta, lang='pt')
    tts.save("response.mp3")
    
    # Tenta reproduzir (precisa do FFmpeg instalado)
    audio_response = AudioSegment.from_mp3("response.mp3")
    play(audio_response)

#Fluxo Principal
try:
    arquivo_audio = capturar_voz()
    texto = transcricao_whisper(arquivo_audio)
    resposta = responder_chatgpt(texto)
    sintetizar_voz(resposta)
except Exception as e:
    print(f"Ocorreu um erro: {e}")