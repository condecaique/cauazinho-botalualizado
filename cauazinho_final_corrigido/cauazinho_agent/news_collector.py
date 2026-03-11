"""
Módulo de Coleta de Notícias
Coleta notícias de múltiplas fontes e APIs
"""

import requests
import feedparser
import logging
from datetime import datetime, timedelta
from config import NEWS_API_KEY, NEWS_API_URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NewsCollector:
    """Coletor de notícias de múltiplas fontes"""
    
    def __init__(self):
        self.noticias = []
        self.fontes_rss = [
            "https://g1.globo.com/rss/g1/economia/",
            "https://valor.globo.com/rss",
            "https://www.infomoney.com.br/feed/",
            "https://feeds.bloomberg.com/markets/news.rss",
            "https://feeds.cnbc.com/cnbc/world/",
            "https://feeds.reuters.com/reuters/businessNews",
        ]
    
    def coletar_noticias_newsapi(self, keywords=None):
        """Coleta notícias usando NewsAPI"""
        logger.info("📰 Coletando notícias via NewsAPI...")
        
        if not keywords:
            keywords = [
                "mercado financeiro Brasil",
                "economia Brasil",
                "bolsa de valores",
                "petróleo",
                "dólar",
                "inflação",
                "juros",
                "China economia",
                "EUA economia",
                "geopolítica",
            ]
        
        try:
            for keyword in keywords:
                url = f"{NEWS_API_URL}/everything"
                params = {
                    "q": keyword,
                    "language": "pt",
                    "sortBy": "publishedAt",
                    "pageSize": 10,
                    "apiKey": NEWS_API_KEY
                }
                
                response = requests.get(url, params=params, timeout=10)
                
                if response.status_code == 200:
                    dados = response.json()
                    
                    for artigo in dados.get("articles", []):
                        noticia = {
                            "titulo": artigo.get("title", ""),
                            "descricao": artigo.get("description", ""),
                            "conteudo": artigo.get("content", ""),
                            "fonte": artigo.get("source", {}).get("name", ""),
                            "url": artigo.get("url", ""),
                            "data": artigo.get("publishedAt", ""),
                            "imagem": artigo.get("urlToImage", ""),
                            "tipo": "newsapi",
                            "keyword": keyword
                        }
                        self.noticias.append(noticia)
                    
                    logger.info(f"  ✅ {len(dados.get('articles', []))} notícias coletadas para '{keyword}'")
                else:
                    logger.warning(f"  ⚠️ Erro na API para '{keyword}': {response.status_code}")
                    
        except Exception as e:
            logger.error(f"  ❌ Erro ao coletar notícias via NewsAPI: {e}")
        
        return self.noticias
    
    def coletar_noticias_rss(self):
        """Coleta notícias via feeds RSS"""
        logger.info("📡 Coletando notícias via RSS feeds...")
        
        for url_rss in self.fontes_rss:
            try:
                feed = feedparser.parse(url_rss)
                
                for entry in feed.entries[:15]:
                    noticia = {
                        "titulo": entry.get("title", ""),
                        "descricao": entry.get("summary", ""),
                        "conteudo": entry.get("content", [{}])[0].get("value", "") if entry.get("content") else "",
                        "fonte": feed.feed.get("title", url_rss),
                        "url": entry.get("link", ""),
                        "data": entry.get("published", ""),
                        "tipo": "rss"
                    }
                    self.noticias.append(noticia)
                
                logger.info(f"  ✅ {len(feed.entries[:15])} notícias coletadas de {feed.feed.get('title', url_rss)}")
                
            except Exception as e:
                logger.error(f"  ❌ Erro ao coletar RSS de {url_rss}: {e}")
        
        return self.noticias
    
    def filtrar_noticias_relevantes(self, palavras_chave=None):
        """Filtra notícias relevantes para mercado financeiro"""
        logger.info("🔍 Filtrando notícias relevantes...")
        
        if not palavras_chave:
            palavras_chave = [
                "bolsa", "ações", "mercado", "economia", "petróleo",
                "dólar", "inflação", "juros", "banco", "empresa",
                "lucro", "prejuízo", "crescimento", "crise", "recessão",
                "china", "eua", "geopolítica", "guerra", "sanções",
                "commodity", "exportação", "importação", "política",
                "governo", "decisão", "empresa", "setor", "indústria"
            ]
        
        noticias_relevantes = []
        
        for noticia in self.noticias:
            texto_completo = (
                noticia.get("titulo", "") + " " +
                noticia.get("descricao", "") + " " +
                noticia.get("conteudo", "")
            ).lower()
            
            # Verifica se contém palavras-chave relevantes
            if any(palavra in texto_completo for palavra in palavras_chave):
                noticias_relevantes.append(noticia)
        
        logger.info(f"  ✅ {len(noticias_relevantes)} notícias relevantes encontradas")
        
        return noticias_relevantes
    
    def remover_duplicatas(self):
        """Remove notícias duplicadas"""
        logger.info("🧹 Removendo duplicatas...")
        
        titulos_vistos = set()
        noticias_unicas = []
        
        for noticia in self.noticias:
            titulo = noticia.get("titulo", "").lower()
            
            if titulo not in titulos_vistos:
                titulos_vistos.add(titulo)
                noticias_unicas.append(noticia)
        
        self.noticias = noticias_unicas
        logger.info(f"  ✅ {len(self.noticias)} notícias únicas mantidas")
        
        return self.noticias
    
    def ordenar_por_data(self):
        """Ordena notícias por data (mais recentes primeiro)"""
        try:
            self.noticias.sort(
                key=lambda x: datetime.fromisoformat(x.get("data", "").replace("Z", "+00:00")),
                reverse=True
            )
        except:
            logger.warning("⚠️ Não foi possível ordenar por data")
        
        return self.noticias
    
    def coletar_tudo(self):
        """Coleta todas as notícias de todas as fontes"""
        logger.info("=" * 60)
        logger.info("📰 CAUÃZINHO - Coletando notícias do mercado")
        logger.info("=" * 60)
        
        # Coleta de RSS (não requer API key)
        self.coletar_noticias_rss()
        
        # Coleta de NewsAPI (se tiver API key configurada)
        if NEWS_API_KEY != "sua_chave_aqui":
            self.coletar_noticias_newsapi()
        else:
            logger.warning("⚠️ NewsAPI não configurada. Configure NEWS_API_KEY em .env")
        
        # Processamento
        self.remover_duplicatas()
        self.ordenar_por_data()
        noticias_relevantes = self.filtrar_noticias_relevantes()
        
        logger.info("=" * 60)
        logger.info(f"✅ Total de notícias coletadas: {len(self.noticias)}")
        logger.info(f"✅ Notícias relevantes: {len(noticias_relevantes)}")
        logger.info("=" * 60)
        
        return noticias_relevantes
    
    def exibir_noticias(self, limite=10):
        """Exibe as notícias mais recentes"""
        logger.info(f"\n📰 Últimas {limite} notícias relevantes:")
        logger.info("-" * 60)
        
        for i, noticia in enumerate(self.noticias[:limite], 1):
            logger.info(f"\n{i}. {noticia.get('titulo', 'Sem título')}")
            logger.info(f"   Fonte: {noticia.get('fonte', 'Desconhecida')}")
            logger.info(f"   Data: {noticia.get('data', 'Desconhecida')}")
            logger.info(f"   URL: {noticia.get('url', 'Não disponível')}")


if __name__ == "__main__":
    collector = NewsCollector()
    noticias = collector.coletar_tudo()
    collector.exibir_noticias(limite=10)
