"""
AUDIO TRANSCRIBER - Transcrição de áudio para texto
Converte mensagens de voz em texto usando Google Speech-to-Text
"""

import os
import requests
import logging
from io import BytesIO
from pydub import AudioSegment
import json

logger = logging.getLogger(__name__)


class AudioTranscriber:
    """Transcreve áudio de voz para texto"""
    
    def __init__(self):
        self.google_api_key = os.getenv("GOOGLE_SPEECH_API_KEY", "")
        self.twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID", "")
        self.twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN", "")
    
    def transcrever_audio_twilio(self, media_url):
        """
        Transcreve áudio do Twilio usando Google Speech-to-Text
        
        Args:
            media_url: URL do áudio do Twilio
        
        Returns:
            str: Texto transcrito
        """
        
        try:
            logger.info(f"🎤 Transcrevendo áudio: {media_url}")
            
            # Baixar áudio do Twilio
            audio_bytes = self._baixar_audio_twilio(media_url)
            
            if not audio_bytes:
                logger.error("❌ Não conseguiu baixar áudio")
                return None
            
            # Converter para WAV se necessário
            audio_wav = self._converter_para_wav(audio_bytes)
            
            # Transcrever usando Google Speech-to-Text
            texto = self._transcrever_google(audio_wav)
            
            if texto:
                logger.info(f"✅ Áudio transcrito: {texto}")
                return texto
            else:
                logger.warning("⚠️ Não conseguiu transcrever áudio")
                return None
        
        except Exception as e:
            logger.error(f"❌ Erro ao transcrever: {e}")
            return None
    
    def _baixar_audio_twilio(self, media_url):
        """Baixa áudio do Twilio"""
        
        try:
            # Adicionar autenticação Twilio
            response = requests.get(
                media_url,
                auth=(self.twilio_account_sid, self.twilio_auth_token),
                timeout=30
            )
            
            if response.status_code == 200:
                logger.info(f"✅ Áudio baixado: {len(response.content)} bytes")
                return response.content
            else:
                logger.error(f"❌ Erro ao baixar: {response.status_code}")
                return None
        
        except Exception as e:
            logger.error(f"❌ Erro ao baixar áudio: {e}")
            return None
    
    def _converter_para_wav(self, audio_bytes):
        """Converte áudio para WAV"""
        
        try:
            # Tentar carregar como OGG (formato padrão Twilio)
            audio = AudioSegment.from_file(BytesIO(audio_bytes), format="ogg")
            
            # Converter para WAV
            wav_buffer = BytesIO()
            audio.export(wav_buffer, format="wav")
            wav_buffer.seek(0)
            
            logger.info("✅ Áudio convertido para WAV")
            return wav_buffer.getvalue()
        
        except Exception as e:
            logger.warning(f"⚠️ Erro ao converter: {e}. Usando áudio original.")
            return audio_bytes
    
    def _transcrever_google(self, audio_bytes):
        """Transcreve usando Google Speech-to-Text API"""
        
        try:
            # URL da API Google Speech-to-Text
            url = "https://speech.googleapis.com/v1/speech:recognize"
            
            # Parâmetros
            params = {
                "key": self.google_api_key
            }
            
            # Corpo da requisição
            body = {
                "config": {
                    "encoding": "LINEAR16",
                    "languageCode": "pt-BR",
                    "sampleRateHertz": 16000,
                    "enableAutomaticPunctuation": True
                },
                "audio": {
                    "content": self._bytes_para_base64(audio_bytes)
                }
            }
            
            # Fazer requisição
            response = requests.post(
                url,
                params=params,
                json=body,
                timeout=30
            )
            
            if response.status_code == 200:
                resultado = response.json()
                
                # Extrair texto
                if "results" in resultado and len(resultado["results"]) > 0:
                    texto = resultado["results"][0]["alternatives"][0]["transcript"]
                    logger.info(f"✅ Transcrito: {texto}")
                    return texto
                else:
                    logger.warning("⚠️ Nenhum resultado de transcrição")
                    return None
            else:
                logger.error(f"❌ Erro Google API: {response.status_code}")
                logger.error(response.text)
                return None
        
        except Exception as e:
            logger.error(f"❌ Erro ao transcrever com Google: {e}")
            return None
    
    def _bytes_para_base64(self, audio_bytes):
        """Converte bytes para base64"""
        import base64
        return base64.b64encode(audio_bytes).decode('utf-8')
    
    def transcrever_com_fallback(self, media_url):
        """
        Transcreve com fallback para transcrição simples
        Se Google falhar, retorna mensagem genérica
        """
        
        texto = self.transcrever_audio_twilio(media_url)
        
        if texto:
            return texto
        else:
            # Fallback: retornar comando genérico
            logger.warning("⚠️ Usando fallback para transcrição")
            return "resumo"  # Comando padrão


# Alternativa: Usar Twilio Media Streams (mais simples)
class AudioTranscriberTwilio:
    """Transcreve áudio usando Twilio Media Streams"""
    
    def __init__(self):
        self.twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID", "")
        self.twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN", "")
    
    def processar_media_stream(self, media_url):
        """
        Processa stream de mídia do Twilio
        Mais eficiente para áudio em tempo real
        """
        
        try:
            logger.info(f"🎤 Processando stream: {media_url}")
            
            # Baixar áudio
            response = requests.get(
                media_url,
                auth=(self.twilio_account_sid, self.twilio_auth_token),
                timeout=30
            )
            
            if response.status_code == 200:
                # Aqui você pode processar o áudio
                logger.info("✅ Stream processado")
                return response.content
            else:
                logger.error(f"❌ Erro ao processar stream: {response.status_code}")
                return None
        
        except Exception as e:
            logger.error(f"❌ Erro: {e}")
            return None


# Usar como fallback: Reconhecimento de padrões simples
class AudioPatternRecognizer:
    """Reconhece padrões de áudio sem API externa"""
    
    def __init__(self):
        self.palavras_chave = {
            "resumo": ["resumo", "mercado", "hoje", "como está"],
            "compra": ["compra", "comprar", "buy", "qual comprar"],
            "venda": ["venda", "vender", "sell", "qual vender"],
            "notícias": ["notícia", "noticia", "news", "o que tem"],
            "ajuda": ["ajuda", "help", "o que fazer", "como funciona"]
        }
    
    def reconhecer_comando(self, texto):
        """Reconhece comando a partir do texto"""
        
        if not texto:
            return None
        
        texto_lower = texto.lower()
        
        # Procurar por palavras-chave
        for comando, palavras in self.palavras_chave.items():
            for palavra in palavras:
                if palavra in texto_lower:
                    logger.info(f"✅ Comando reconhecido: {comando}")
                    return comando
        
        logger.warning(f"⚠️ Comando não reconhecido: {texto}")
        return None
