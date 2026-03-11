"""
Módulo de Análise Macroeconômica
Analisa correlações macro e impacto em empresas
"""

import logging
from config import MAPA_MACRO_IMPACTO, EMPRESAS_B3_PRINCIPAIS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MacroAnalyzer:
    """Analisador de correlações macroeconômicas"""
    
    def __init__(self, dados_mercado=None):
        self.dados_mercado = dados_mercado or {}
        self.analises = []
        self.impactos_por_empresa = {}
    
    def detectar_temas_noticias(self, noticias_analisadas):
        """Detecta temas macroeconômicos nas notícias"""
        logger.info("🔍 Detectando temas macroeconômicos...")
        
        temas_detectados = {
            "petróleo": {"positivas": 0, "negativas": 0, "noticias": []},
            "minério": {"positivas": 0, "negativas": 0, "noticias": []},
            "china": {"positivas": 0, "negativas": 0, "noticias": []},
            "juros_eua": {"positivas": 0, "negativas": 0, "noticias": []},
            "dólar": {"positivas": 0, "negativas": 0, "noticias": []},
            "inflação": {"positivas": 0, "negativas": 0, "noticias": []},
            "guerra": {"positivas": 0, "negativas": 0, "noticias": []},
            "política": {"positivas": 0, "negativas": 0, "noticias": []},
        }
        
        palavras_tema = {
            "petróleo": ["petróleo", "barril", "wti", "brent", "opep"],
            "minério": ["minério", "ferro", "minério de ferro", "vale"],
            "china": ["china", "chinês", "asiático", "oriente"],
            "juros_eua": ["fed", "juros", "taxa", "banco central eua"],
            "dólar": ["dólar", "usdbrl", "câmbio", "moeda"],
            "inflação": ["inflação", "ipc", "cpi", "preços"],
            "guerra": ["guerra", "conflito", "tensão", "sanção"],
            "política": ["governo", "política", "eleição", "decreto"],
        }
        
        for noticia in noticias_analisadas:
            texto = (
                noticia.get("noticia", "") + " " +
                noticia.get("texto_completo", "")
            ).lower()
            
            for tema, palavras in palavras_tema.items():
                if any(palavra in texto for palavra in palavras):
                    if noticia["sentimento"] == "POSITIVO":
                        temas_detectados[tema]["positivas"] += 1
                    elif noticia["sentimento"] == "NEGATIVO":
                        temas_detectados[tema]["negativas"] += 1
                    
                    temas_detectados[tema]["noticias"].append(noticia["noticia"][:60])
        
        logger.info("✅ Temas detectados:")
        for tema, dados in temas_detectados.items():
            total = dados["positivas"] + dados["negativas"]
            if total > 0:
                logger.info(f"  {tema}: +{dados['positivas']} -{dados['negativas']} (total: {total})")
        
        return temas_detectados
    
    def calcular_impacto_tema(self, tema, sentimento_positivo=True):
        """Calcula impacto de um tema em empresas"""
        
        # Mapeia tema para chave no MAPA_MACRO_IMPACTO
        chave_impacto = None
        
        if tema == "petróleo":
            chave_impacto = "petróleo_sobe" if sentimento_positivo else "petróleo_cai"
        elif tema == "minério":
            chave_impacto = "minério_sobe" if sentimento_positivo else "minério_cai"
        elif tema == "china":
            chave_impacto = "china_desacelera" if not sentimento_positivo else None
        elif tema == "juros_eua":
            chave_impacto = "juros_eua_sobem" if sentimento_positivo else None
        elif tema == "dólar":
            chave_impacto = "dólar_sobe" if sentimento_positivo else None
        elif tema == "inflação":
            chave_impacto = "inflação_alta" if sentimento_positivo else None
        elif tema == "guerra":
            chave_impacto = "guerra_geopolitica" if sentimento_positivo else None
        
        if chave_impacto and chave_impacto in MAPA_MACRO_IMPACTO:
            return MAPA_MACRO_IMPACTO[chave_impacto]
        
        return None
    
    def analisar_impacto_empresas(self, temas_detectados):
        """Analisa impacto dos temas em cada empresa"""
        logger.info("\n💼 Analisando impacto em empresas...")
        
        # Inicializa scores
        for ticker in EMPRESAS_B3_PRINCIPAIS.keys():
            self.impactos_por_empresa[ticker] = {
                "score_total": 0,
                "impactos": [],
                "confianca": 0,
                "recomendacao": "NEUTRO"
            }
        
        # Processa cada tema
        for tema, dados in temas_detectados.items():
            if dados["positivas"] + dados["negativas"] == 0:
                continue
            
            # Determina se tema é positivo ou negativo
            sentimento_positivo = dados["positivas"] > dados["negativas"]
            
            # Calcula impacto
            impacto = self.calcular_impacto_tema(tema, sentimento_positivo)
            
            if impacto:
                # Aplica impacto às empresas sensíveis
                for ticker in impacto["empresas"]:
                    if ticker in self.impactos_por_empresa:
                        # Calcula força do impacto
                        forca = impacto["força"]
                        
                        if impacto["impacto"] == "positivo":
                            score = forca
                        else:
                            score = -forca
                        
                        # Adiciona ao score total
                        self.impactos_por_empresa[ticker]["score_total"] += score
                        self.impactos_por_empresa[ticker]["impactos"].append({
                            "tema": tema,
                            "tipo": impacto["impacto"],
                            "forca": forca,
                            "descricao": impacto["descricao"],
                            "noticias": dados["noticias"][:3]
                        })
        
        # Calcula confiança e recomendação
        for ticker, dados in self.impactos_por_empresa.items():
            if dados["impactos"]:
                # Confiança baseada no número de impactos
                dados["confianca"] = min(len(dados["impactos"]) * 0.2, 1.0)
                
                # Recomendação baseada no score
                if dados["score_total"] > 0.5:
                    dados["recomendacao"] = "COMPRA"
                elif dados["score_total"] < -0.5:
                    dados["recomendacao"] = "VENDA"
                else:
                    dados["recomendacao"] = "NEUTRO"
        
        logger.info("✅ Análise de impacto concluída")
        
        return self.impactos_por_empresa
    
    def gerar_relatorio_macro(self):
        """Gera relatório de análise macroeconômica"""
        logger.info("\n" + "=" * 60)
        logger.info("📊 RELATÓRIO DE ANÁLISE MACROECONÔMICA")
        logger.info("=" * 60)
        
        # Empresas com recomendação de COMPRA
        logger.info("\n🟢 RECOMENDAÇÕES DE COMPRA:")
        compras = [
            (ticker, dados) for ticker, dados in self.impactos_por_empresa.items()
            if dados["recomendacao"] == "COMPRA"
        ]
        
        for ticker, dados in sorted(compras, key=lambda x: x[1]["score_total"], reverse=True):
            empresa = EMPRESAS_B3_PRINCIPAIS.get(ticker, {})
            logger.info(f"\n  {ticker} - {empresa.get('nome', 'Desconhecida')}")
            logger.info(f"    Score: {dados['score_total']:+.2f}")
            logger.info(f"    Confiança: {dados['confianca']:.0%}")
            logger.info(f"    Impactos identificados: {len(dados['impactos'])}")
            
            for impacto in dados['impactos'][:3]:
                logger.info(f"      • {impacto['tema']}: {impacto['descricao']}")
        
        # Empresas com recomendação de VENDA
        logger.info("\n🔴 RECOMENDAÇÕES DE VENDA:")
        vendas = [
            (ticker, dados) for ticker, dados in self.impactos_por_empresa.items()
            if dados["recomendacao"] == "VENDA"
        ]
        
        for ticker, dados in sorted(vendas, key=lambda x: x[1]["score_total"]):
            empresa = EMPRESAS_B3_PRINCIPAIS.get(ticker, {})
            logger.info(f"\n  {ticker} - {empresa.get('nome', 'Desconhecida')}")
            logger.info(f"    Score: {dados['score_total']:+.2f}")
            logger.info(f"    Confiança: {dados['confianca']:.0%}")
            logger.info(f"    Impactos identificados: {len(dados['impactos'])}")
            
            for impacto in dados['impactos'][:3]:
                logger.info(f"      • {impacto['tema']}: {impacto['descricao']}")
        
        # Empresas neutras
        neutras = [
            (ticker, dados) for ticker, dados in self.impactos_por_empresa.items()
            if dados["recomendacao"] == "NEUTRO"
        ]
        
        if neutras:
            logger.info(f"\n⚪ RECOMENDAÇÕES NEUTRAS: {len(neutras)} empresas")
    
    def obter_recomendacoes_top(self, limite=5):
        """Retorna as top recomendações de compra e venda"""
        
        compras = sorted(
            [(t, d) for t, d in self.impactos_por_empresa.items() if d["recomendacao"] == "COMPRA"],
            key=lambda x: x[1]["score_total"],
            reverse=True
        )[:limite]
        
        vendas = sorted(
            [(t, d) for t, d in self.impactos_por_empresa.items() if d["recomendacao"] == "VENDA"],
            key=lambda x: x[1]["score_total"]
        )[:limite]
        
        return {
            "compras": compras,
            "vendas": vendas
        }


if __name__ == "__main__":
    analyzer = MacroAnalyzer()
    
    # Teste com dados simulados
    noticias_teste = [
        {
            "noticia": "Petróleo sobe com tensões geopolíticas",
            "texto_completo": "Conflito no Oriente Médio eleva preços",
            "sentimento": "POSITIVO"
        }
    ]
    
    temas = analyzer.detectar_temas_noticias(noticias_teste)
    impactos = analyzer.analisar_impacto_empresas(temas)
    analyzer.gerar_relatorio_macro()
