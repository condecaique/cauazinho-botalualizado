"""
Módulo de Coleta de Dados
Coleta dados de bolsas globais, moedas, commodities e índices
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import logging
from config import (
    GLOBAL_INDICES, EMPRESAS_B3_PRINCIPAIS, EMPRESAS_GLOBAIS,
    MOEDAS, COMMODITIES
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataCollector:
    """Coletor de dados de mercado financeiro"""
    
    def __init__(self):
        self.indices_data = {}
        self.stocks_b3 = {}
        self.stocks_globais = {}
        self.moedas = {}
        self.commodities = {}
        
    def coletar_indices_globais(self):
        """Coleta dados dos índices globais"""
        logger.info("📊 Coletando índices globais...")
        
        for nome, ticker in GLOBAL_INDICES.items():
            try:
                indice = yf.Ticker(ticker)
                hist = indice.history(period="1d")
                
                if not hist.empty:
                    preco_atual = hist['Close'].iloc[-1]
                    
                    # Pega dados de 30 dias atrás para calcular variação
                    hist_30d = indice.history(period="30d")
                    if len(hist_30d) > 1:
                        preco_30d_atras = hist_30d['Close'].iloc[0]
                        variacao_30d = ((preco_atual - preco_30d_atras) / preco_30d_atras) * 100
                    else:
                        variacao_30d = 0
                    
                    self.indices_data[nome] = {
                        "ticker": ticker,
                        "preco": preco_atual,
                        "variacao_30d": variacao_30d,
                        "timestamp": datetime.now()
                    }
                    logger.info(f"  ✅ {nome}: R$ {preco_atual:.2f} ({variacao_30d:+.2f}%)")
            except Exception as e:
                logger.error(f"  ❌ Erro ao coletar {nome}: {e}")
        
        return self.indices_data
    
    def coletar_empresas_b3(self):
        """Coleta dados de todas as empresas principais da B3"""
        logger.info("🇧🇷 Coletando dados da B3...")
        
        for ticker, info in EMPRESAS_B3_PRINCIPAIS.items():
            try:
                acao = yf.Ticker(ticker)
                hist = acao.history(period="1d")
                
                if not hist.empty:
                    preco_atual = hist['Close'].iloc[-1]
                    
                    # Variação de 30 dias
                    hist_30d = acao.history(period="30d")
                    if len(hist_30d) > 1:
                        preco_30d_atras = hist_30d['Close'].iloc[0]
                        variacao_30d = ((preco_atual - preco_30d_atras) / preco_30d_atras) * 100
                    else:
                        variacao_30d = 0
                    
                    self.stocks_b3[ticker] = {
                        "nome": info["nome"],
                        "setor": info["setor"],
                        "sensivel_a": info["sensivel_a"],
                        "preco": preco_atual,
                        "variacao_30d": variacao_30d,
                        "timestamp": datetime.now()
                    }
                    logger.info(f"  ✅ {info['nome']} ({ticker}): R$ {preco_atual:.2f} ({variacao_30d:+.2f}%)")
            except Exception as e:
                logger.error(f"  ❌ Erro ao coletar {ticker}: {e}")
        
        return self.stocks_b3
    
    def coletar_empresas_globais(self):
        """Coleta dados de empresas globais principais"""
        logger.info("🌍 Coletando dados de bolsas globais...")
        
        for ticker, info in EMPRESAS_GLOBAIS.items():
            try:
                acao = yf.Ticker(ticker)
                hist = acao.history(period="1d")
                
                if not hist.empty:
                    preco_atual = hist['Close'].iloc[-1]
                    
                    # Variação de 30 dias
                    hist_30d = acao.history(period="30d")
                    if len(hist_30d) > 1:
                        preco_30d_atras = hist_30d['Close'].iloc[0]
                        variacao_30d = ((preco_atual - preco_30d_atras) / preco_30d_atras) * 100
                    else:
                        variacao_30d = 0
                    
                    self.stocks_globais[ticker] = {
                        "nome": info["nome"],
                        "bolsa": info["bolsa"],
                        "sensivel_a": info["sensivel_a"],
                        "preco": preco_atual,
                        "variacao_30d": variacao_30d,
                        "timestamp": datetime.now()
                    }
                    logger.info(f"  ✅ {info['nome']} ({ticker}): ${preco_atual:.2f} ({variacao_30d:+.2f}%)")
            except Exception as e:
                logger.error(f"  ❌ Erro ao coletar {ticker}: {e}")
        
        return self.stocks_globais
    
    def coletar_moedas(self):
        """Coleta dados de moedas principais"""
        logger.info("💱 Coletando dados de moedas...")
        
        for ticker, descricao in MOEDAS.items():
            try:
                moeda = yf.Ticker(ticker)
                hist = moeda.history(period="1d")
                
                if not hist.empty:
                    preco_atual = hist['Close'].iloc[-1]
                    
                    # Variação de 30 dias
                    hist_30d = moeda.history(period="30d")
                    if len(hist_30d) > 1:
                        preco_30d_atras = hist_30d['Close'].iloc[0]
                        variacao_30d = ((preco_atual - preco_30d_atras) / preco_30d_atras) * 100
                    else:
                        variacao_30d = 0
                    
                    self.moedas[ticker] = {
                        "descricao": descricao,
                        "preco": preco_atual,
                        "variacao_30d": variacao_30d,
                        "timestamp": datetime.now()
                    }
                    logger.info(f"  ✅ {descricao}: {preco_atual:.4f} ({variacao_30d:+.2f}%)")
            except Exception as e:
                logger.error(f"  ❌ Erro ao coletar {ticker}: {e}")
        
        return self.moedas
    
    def coletar_commodities(self):
        """Coleta dados de commodities principais"""
        logger.info("⛽ Coletando dados de commodities...")
        
        for ticker, descricao in COMMODITIES.items():
            try:
                commodity = yf.Ticker(ticker)
                hist = commodity.history(period="1d")
                
                if not hist.empty:
                    preco_atual = hist['Close'].iloc[-1]
                    
                    # Variação de 30 dias
                    hist_30d = commodity.history(period="30d")
                    if len(hist_30d) > 1:
                        preco_30d_atras = hist_30d['Close'].iloc[0]
                        variacao_30d = ((preco_atual - preco_30d_atras) / preco_30d_atras) * 100
                    else:
                        variacao_30d = 0
                    
                    self.commodities[ticker] = {
                        "descricao": descricao,
                        "preco": preco_atual,
                        "variacao_30d": variacao_30d,
                        "timestamp": datetime.now()
                    }
                    logger.info(f"  ✅ {descricao}: {preco_atual:.2f} ({variacao_30d:+.2f}%)")
            except Exception as e:
                logger.error(f"  ❌ Erro ao coletar {ticker}: {e}")
        
        return self.commodities
    
    def coletar_tudo(self):
        """Coleta todos os dados de uma vez"""
        logger.info("=" * 60)
        logger.info("🤖 CAUÃZINHO - Iniciando coleta de dados do mercado")
        logger.info("=" * 60)
        
        self.coletar_indices_globais()
        self.coletar_empresas_b3()
        self.coletar_empresas_globais()
        self.coletar_moedas()
        self.coletar_commodities()
        
        logger.info("=" * 60)
        logger.info("✅ Coleta de dados concluída!")
        logger.info("=" * 60)
        
        return {
            "indices": self.indices_data,
            "b3": self.stocks_b3,
            "globais": self.stocks_globais,
            "moedas": self.moedas,
            "commodities": self.commodities
        }
    
    def gerar_resumo_mercado(self):
        """Gera um resumo do estado atual do mercado"""
        logger.info("\n📈 RESUMO DO MERCADO")
        logger.info("-" * 60)
        
        if self.indices_data:
            logger.info("\n🌍 Índices Globais:")
            for nome, dados in self.indices_data.items():
                logger.info(f"  {nome}: {dados['preco']:.2f} ({dados['variacao_30d']:+.2f}%)")
        
        if self.moedas:
            logger.info("\n💱 Moedas:")
            for ticker, dados in self.moedas.items():
                logger.info(f"  {dados['descricao']}: {dados['preco']:.4f} ({dados['variacao_30d']:+.2f}%)")
        
        if self.commodities:
            logger.info("\n⛽ Commodities:")
            for ticker, dados in self.commodities.items():
                logger.info(f"  {dados['descricao']}: {dados['preco']:.2f} ({dados['variacao_30d']:+.2f}%)")


if __name__ == "__main__":
    collector = DataCollector()
    dados = collector.coletar_tudo()
    collector.gerar_resumo_mercado()
