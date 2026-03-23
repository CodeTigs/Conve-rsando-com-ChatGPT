# 🎙️ Voice Conversational AI - Whisper & ChatGPT

Este projeto consiste em um sistema de conversação por voz inteligente que utiliza as tecnologias de ponta da **OpenAI** para transformar fala em texto, processar a inteligência da resposta e converter o retorno em áudio natural.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**: Linguagem base do projeto.
* **OpenAI Whisper**: Reconhecimento Automático de Fala (ASR) robusto e multilíngue.
* **GPT-4o/3.5-Turbo**: Modelo de linguagem para geração de respostas contextuais.
* **gTTS (Google Text-to-Speech)**: Biblioteca para síntese de voz.
* **FFmpeg**: Framework multimídia para processamento de áudio.
* **SpeechRecognition**: Captura de áudio via microfone.

---

## 🛠️ Como Funciona?

O fluxo de dados segue a seguinte arquitetura:
1.  **Captura:** O script ouve o microfone do usuário e salva um arquivo `.wav`.
2.  **Transcrição:** O **Whisper** processa o áudio e converte em texto (STT).
3.  **Processamento:** O texto é enviado para a API do **ChatGPT**, que gera uma resposta inteligente.
4.  **Síntese:** A resposta é convertida em áudio pelo **gTTS** (TTS).
5.  **Reprodução:** O sistema utiliza o `pydub` para tocar a resposta para o usuário.

---

## 🔧 Pré-requisitos e Instalação

### 1. Dependências do Sistema
É necessário ter o **FFmpeg** instalado e configurado no seu `PATH` do sistema.

### 2. Bibliotecas Python
```bash
pip install openai gtts pydub SpeechRecognition
