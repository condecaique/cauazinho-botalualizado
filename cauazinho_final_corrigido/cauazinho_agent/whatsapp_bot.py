"""
CAUÃZINHO BOT - WhatsApp (Versão Final Corrigida)
Bot profissional para análise de mercado financeiro via WhatsApp
Usa Twilio para integração com WhatsApp e Groq para análise de IA
"""

from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import os
import logging
from datetime import datetime
import threading
import time
from dotenv import load_dotenv

# Importar módulos do agente
from data_collector import DataCollector
from news_collector import NewsCollector
from sentiment_analyzer import SentimentAnalyzer
from macro_analyzer import MacroAnalyzer
from config import EMPRESAS_B3_PRINCIPAIS
from audio_transcriber import AudioTranscriber, AudioPatternRecognizer
from groq_agent import GroqAgent

# Carregar variáveis de ambiente
load_dotenv()

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Inicializar Flask
app = Flask(__name__)

# Configurar Twilio
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE", "whatsapp:+14155238886")

try:
    if TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN:
        twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        logger.info("✅ Twilio configurado com sucesso!")
    else:
        logger.warning("⚠️ Twilio não configurado (SIDs ou Tokens faltando).")
        twilio_client = None
except Exception as e:
    logger.error(f"❌ Erro ao configurar Twilio: {e}")
    twilio_client = None

# Cache de análises
cache_analise = {
    "timestamp": None,
    "dados": None,
    "tempo_cache": 3600
}

class CauazinhoBot:
    def __init__(self):
        self.data_collector = DataCollector()
        self.news_collector = NewsCollector()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.macro_analyzer = MacroAnalyzer()
        self.groq_agent = GroqAgent()
        
        self.dados_mercado = {}
        self.noticias = []
        self.noticias_analisadas = []
        self.recomendacoes_top = {}

    def analisar_mercado(self):
        try:
            logger.info("🔄 Iniciando análise de mercado...")
            self.dados_mercado = self.data_collector.coletar_tudo()
            self.noticias = self.news_collector.coletar_tudo()
            self.noticias_analisadas = self.sentiment_analyzer.analisar_lote(self.noticias)
            self.macro_analyzer.analisar_impacto_empresas(
                self.macro_analyzer.detectar_temas_noticias(self.noticias_analisadas)
            )
            self.recomendacoes_top = self.macro_analyzer.obter_recomendacoes_top(limite=5)
            logger.info("✅ Análise concluída!")
            return True
        except Exception as e:
            logger.error(f"❌ Erro na análise: {e}")
            return False

    def obter_analise_ia(self, contexto="geral"):
        """Usa o Groq para gerar uma análise de IA"""
        return self.groq_agent.analisar_noticias(
            self.noticias, 
            str(self.dados_mercado), 
            contexto
        )

bot = CauazinhoBot()
audio_transcriber = AudioTranscriber()

@app.route('/webhook', methods=['POST'])
@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    try:
        incoming_msg = request.values.get('Body', '').strip().lower()
        sender = request.values.get('From', '')
        
        logger.info(f"📱 Mensagem de {sender}: {incoming_msg}")
        
        # Processar comandos
        if any(p in incoming_msg for p in ["oi", "olá", "menu", "ajuda"]):
            resposta = "🤖 *Cauãzinho v2 - Menu*\n\n" \
                       "📊 *analise* - Análise completa com IA (Groq)\n" \
                       "🟢 *compra* - Melhores ações para COMPRA\n" \
                       "🔴 *venda* - Ações para EVITAR/VENDA\n" \
                       "📰 *noticias* - Principais notícias do mundo\n" \
                       "💡 Ou pergunte algo livremente!"
        
        elif "analise" in incoming_msg or "análise" in incoming_msg:
            enviar_mensagem(sender, "⏳ *Analisando notícias e mercado com IA... Aguarde!*")
            resposta = bot.obter_analise_ia("Análise Geral de Mercado e Geopolítica")
            
        elif "compra" in incoming_msg:
            resposta = bot.obter_analise_ia("Foco em recomendações de COMPRA")
            
        elif "venda" in incoming_msg:
            resposta = bot.obter_analise_ia("Foco em recomendações de VENDA")
            
        elif "noticia" in incoming_msg:
            resposta = bot.obter_analise_ia("Resumo das principais notícias geopolíticas")
            
        else:
            # Pergunta livre usando IA
            resposta = bot.obter_analise_ia(f"Pergunta do usuário: {incoming_msg}")

        enviar_mensagem(sender, resposta)
        return jsonify({"status": "ok"}), 200
    
    except Exception as e:
        logger.error(f"❌ Erro no webhook: {e}")
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

def enviar_mensagem(numero, mensagem):
    if not twilio_client:
        return False
    try:
        twilio_client.messages.create(body=mensagem, from_=TWILIO_PHONE, to=numero)
        return True
    except Exception as e:
        logger.error(f"❌ Erro Twilio: {e}")
        return False

@app.route('/status', methods=['GET'])
@app.route('/', methods=['GET'])
def status():
    return jsonify({
        "status": "online",
        "agente": "Cauãzinho v2",
        "ia": "Groq LLaMA 3.3 70B",
        "endpoints": ["/webhook", "/status"]
    }), 200

if __name__ == '__main__':
    # Análise inicial rápida
    threading.Thread(target=bot.analisar_mercado).start()
    
    # Iniciar Flask com a porta correta para o Railway
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
