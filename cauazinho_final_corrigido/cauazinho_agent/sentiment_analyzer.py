"""
Módulo de Análise de Sentimento
Analisa sentimento de notícias e impacto no mercado
"""

import logging
from textblob import TextBlob
from config import PALAVRAS_CHAVE_POSITIVAS, PALAVRAS_CHAVE_NEGATIVAS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SentimentAnalyzer:
    """Analisador de sentimento de notícias"""
    
    def __init__(self):
        self.resultados = []
    
    def analisar_sentimento_textblob(self, texto):
        """Analisa sentimento usando TextBlob"""
        try:
            blob = TextBlob(texto)
            polaridade = blob.sentiment.polarity  # -1 a 1
            subjetividade = blob.sentiment.subjectivity  # 0 a 1
            
            # Classifica o sentimento
            if polaridade > 0.1:
                sentimento = "POSITIVO"
            elif polaridade < -0.1:
                sentimento = "NEGATIVO"
            else:
                sentimento = "NEUTRO"
            
            return {
                "sentimento": sentimento,
                "polaridade": polaridade,
                "subjetividade": subjetividade,
                "confianca": abs(polaridade)
            }
        except Exception as e:
            logger.error(f"Erro ao analisar sentimento: {e}")
            return {
                "sentimento": "NEUTRO",
                "polaridade": 0,
                "subjetividade": 0,
                "confianca": 0
            }
    
    def analisar_sentimento_palavras_chave(self, texto):
        """Analisa sentimento usando palavras-chave"""
        texto_lower = texto.lower()
        
        # Conta palavras positivas e negativas
        positivas = sum(1 for palavra in PALAVRAS_CHAVE_POSITIVAS if palavra in texto_lower)
        negativas = sum(1 for palavra in PALAVRAS_CHAVE_NEGATIVAS if palavra in texto_lower)
        
        # Calcula score
        if positivas + negativas == 0:
            score = 0
            sentimento = "NEUTRO"
        else:
            score = (positivas - negativas) / (positivas + negativas)
            
            if score > 0.3:
                sentimento = "POSITIVO"
            elif score < -0.3:
                sentimento = "NEGATIVO"
            else:
                sentimento = "NEUTRO"
        
        return {
            "sentimento": sentimento,
            "score": score,
            "palavras_positivas": positivas,
            "palavras_negativas": negativas,
            "confianca": min(abs(score), 1.0)
        }
    
    def analisar_noticia(self, noticia):
        """Analisa sentimento completo de uma notícia"""
        
        texto_completo = (
            noticia.get("titulo", "") + " " +
            noticia.get("descricao", "") + " " +
            noticia.get("conteudo", "")
        )
        
        # Análise TextBlob
        analise_textblob = self.analisar_sentimento_textblob(texto_completo)
        
        # Análise por palavras-chave
        analise_palavras = self.analisar_sentimento_palavras_chave(texto_completo)
        
        # Combina as análises (média ponderada)
        sentimento_final = analise_textblob["sentimento"]
        confianca_final = (analise_textblob["confianca"] + analise_palavras["confianca"]) / 2
        
        resultado = {
            "noticia": noticia.get("titulo", ""),
            "fonte": noticia.get("fonte", ""),
            "data": noticia.get("data", ""),
            "url": noticia.get("url", ""),
            "sentimento": sentimento_final,
            "confianca": confianca_final,
            "analise_textblob": analise_textblob,
            "analise_palavras": analise_palavras,
            "texto_completo": texto_completo[:500]  # Primeiros 500 caracteres
        }
        
        self.resultados.append(resultado)
        return resultado
    
    def analisar_lote(self, noticias):
        """Analisa um lote de notícias"""
        logger.info(f"🧠 Analisando sentimento de {len(noticias)} notícias...")
        
        for noticia in noticias:
            self.analisar_noticia(noticia)
        
        logger.info(f"✅ Análise concluída: {len(self.resultados)} notícias processadas")
        
        return self.resultados
    
    def gerar_relatorio_sentimento(self):
        """Gera relatório de sentimento"""
        logger.info("\n📊 RELATÓRIO DE SENTIMENTO")
        logger.info("-" * 60)
        
        if not self.resultados:
            logger.info("Nenhuma notícia analisada")
            return
        
        # Conta sentimentos
        positivos = sum(1 for r in self.resultados if r["sentimento"] == "POSITIVO")
        negativos = sum(1 for r in self.resultados if r["sentimento"] == "NEGATIVO")
        neutros = sum(1 for r in self.resultados if r["sentimento"] == "NEUTRO")
        
        total = len(self.resultados)
        
        logger.info(f"\nTotal de notícias: {total}")
        logger.info(f"  ✅ Positivas: {positivos} ({positivos/total*100:.1f}%)")
        logger.info(f"  ❌ Negativas: {negativos} ({negativos/total*100:.1f}%)")
        logger.info(f"  ➖ Neutras: {neutros} ({neutros/total*100:.1f}%)")
        
        # Confiança média
        confianca_media = sum(r["confianca"] for r in self.resultados) / total
        logger.info(f"\nConfiança média: {confianca_media:.2%}")
        
        # Top 5 notícias mais positivas
        logger.info("\n🔝 Top 5 notícias mais POSITIVAS:")
        top_positivas = sorted(
            [r for r in self.resultados if r["sentimento"] == "POSITIVO"],
            key=lambda x: x["confianca"],
            reverse=True
        )[:5]
        
        for i, noticia in enumerate(top_positivas, 1):
            logger.info(f"  {i}. {noticia['noticia'][:60]}...")
            logger.info(f"     Confiança: {noticia['confianca']:.2%}")
        
        # Top 5 notícias mais negativas
        logger.info("\n🔻 Top 5 notícias mais NEGATIVAS:")
        top_negativas = sorted(
            [r for r in self.resultados if r["sentimento"] == "NEGATIVO"],
            key=lambda x: x["confianca"],
            reverse=True
        )[:5]
        
        for i, noticia in enumerate(top_negativas, 1):
            logger.info(f"  {i}. {noticia['noticia'][:60]}...")
            logger.info(f"     Confiança: {noticia['confianca']:.2%}")
    
    def filtrar_por_sentimento(self, sentimento):
        """Filtra notícias por sentimento"""
        return [r for r in self.resultados if r["sentimento"] == sentimento]
    
    def filtrar_por_confianca(self, minima=0.5):
        """Filtra notícias com confiança mínima"""
        return [r for r in self.resultados if r["confianca"] >= minima]


if __name__ == "__main__":
    # Teste
    analyzer = SentimentAnalyzer()
    
    noticias_teste = [
        {
            "titulo": "Petrobras sobe com alta do petróleo",
            "descricao": "Ações da Petrobras registram ganho expressivo",
            "conteudo": "A empresa se beneficia do crescimento dos preços",
            "fonte": "Teste"
        },
        {
            "titulo": "Bolsa cai com pessimismo global",
            "descricao": "Mercado reage negativamente a notícias",
            "conteudo": "Investidores vendem ações em pânico",
            "fonte": "Teste"
        }
    ]
    
    resultados = analyzer.analisar_lote(noticias_teste)
    analyzer.gerar_relatorio_sentimento()
