import os
import logging
from groq import Groq

logger = logging.getLogger(__name__)

class GroqAgent:
    def __init__(self):
        # Pega a chave diretamente do ambiente
        self.api_key = os.environ.get("GROQ_API_KEY")
        self.model = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")
        
        if not self.api_key:
            logger.error("❌ GROQ_API_KEY não encontrada!")
            # Não levantamos erro aqui para não quebrar o bot se a chave não estiver configurada,
            # mas as análises de IA não funcionarão.
            self.client = None
        else:
            try:
                self.client = Groq(api_key=self.api_key)
                logger.info(f"✅ Groq inicializado com sucesso (Modelo: {self.model})")
            except Exception as e:
                logger.error(f"❌ Erro ao iniciar Groq: {e}")
                self.client = None

    def analisar_noticias(self, noticias, dados_mercado, contexto="geral"):
        """Analisa notícias e dados de mercado usando Groq LLM"""
        if not self.client:
            return "⚠️ IA (Groq) não configurada. Use as análises técnicas padrão."

        try:
            # Limitar a quantidade de notícias para não estourar o limite de tokens
            noticias_texto = ""
            for n in noticias[:10]:
                noticias_texto += f"- {n.get('titulo', '')}: {n.get('descricao', '')[:200]}\n"

            prompt = f"""
            Você é o Cauãzinho, um analista de investimentos sênior especialista em geopolítica e mercado financeiro.
            
            CONTEXTO: {contexto}
            
            DADOS DE MERCADO ATUAIS:
            {dados_mercado}
            
            NOTÍCIAS RECENTES:
            {noticias_texto}
            
            SUA TAREFA:
            1. Analise como os eventos geopolíticos e políticos globais afetam as empresas da bolsa (B3 e Globais).
            2. Dê recomendações claras de COMPRA, VENDA ou MANUTENÇÃO para os ativos mais impactados.
            3. Explique o PORQUÊ técnico de cada decisão baseando-se nos fatos.
            4. Use um tom profissional, direto e amigável.
            
            Responda em Português do Brasil, formatando com negritos e emojis para leitura fácil no WhatsApp.
            """

            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Você é o Cauãzinho, o melhor assistente financeiro do mundo."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            
            return completion.choices[0].message.content
        except Exception as e:
            logger.error(f"❌ Erro na análise do Groq: {e}")
            return f"⚠️ Desculpe, tive um problema técnico na análise de IA: {str(e)}"
