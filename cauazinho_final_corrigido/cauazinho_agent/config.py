"""
Configurações do Agente Cauãzinho
Arquivo central de configuração para APIs, tickers e constantes
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ============================================
# CONFIGURAÇÕES DE API
# ============================================

# NewsAPI (para notícias globais)
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "sua_chave_aqui")
NEWS_API_URL = "https://newsapi.org/v2"

# Você pode obter uma chave gratuita em: https://newsapi.org

# ============================================
# TICKERS DE BOLSAS GLOBAIS
# ============================================

# Índices Globais
GLOBAL_INDICES = {
    "IBOV": "^BVSP",           # Ibovespa - Brasil
    "SP500": "^GSPC",          # S&P 500 - EUA
    "DOW": "^DJI",             # Dow Jones - EUA
    "NASDAQ": "^IXIC",         # Nasdaq - EUA
    "NIKKEI": "^N225",         # Nikkei 225 - Japão
    "DAX": "^GDAXI",           # DAX - Alemanha
    "FTSE": "^FTSE",           # FTSE 100 - Reino Unido
    "SSE": "000001.SS",        # Shanghai Stock Exchange - China
}

# ============================================
# PRINCIPAIS EMPRESAS DA B3
# ============================================

EMPRESAS_B3_PRINCIPAIS = {
    # Petróleo e Gás
    "PETR4.SA": {"nome": "Petrobras", "setor": "Petróleo e Gás", "sensivel_a": ["petróleo", "dólar"]},
    
    # Mineração
    "VALE3.SA": {"nome": "Vale", "setor": "Mineração", "sensivel_a": ["minério", "china", "dólar"]},
    
    # Bancos
    "ITUB4.SA": {"nome": "Itaú Unibanco", "setor": "Financeiro", "sensivel_a": ["juros", "dólar"]},
    "BBAS3.SA": {"nome": "Banco do Brasil", "setor": "Financeiro", "sensivel_a": ["juros", "dólar"]},
    "SANB11.SA": {"nome": "Santander Brasil", "setor": "Financeiro", "sensivel_a": ["juros", "dólar"]},
    
    # Energia
    "ELET3.SA": {"nome": "Eletrobras", "setor": "Energia", "sensivel_a": ["juros", "política"]},
    "ENGI11.SA": {"nome": "Engie Brasil", "setor": "Energia", "sensivel_a": ["juros", "clima"]},
    
    # Varejo
    "MGLU3.SA": {"nome": "Magazine Luiza", "setor": "Varejo", "sensivel_a": ["juros", "consumo"]},
    "BHIA3.SA": {"nome": "Natura &Co", "setor": "Varejo", "sensivel_a": ["dólar", "consumo"]},
    
    # Infraestrutura
    "WEGE3.SA": {"nome": "WEG", "setor": "Infraestrutura", "sensivel_a": ["dólar", "crescimento"]},
    "CCRO3.SA": {"nome": "CCR", "setor": "Infraestrutura", "sensivel_a": ["juros", "política"]},
    
    # Agronegócio
    "SUZB3.SA": {"nome": "Suzano", "setor": "Agronegócio", "sensivel_a": ["china", "dólar"]},
    "JBSS3.SA": {"nome": "JBS", "setor": "Agronegócio", "sensivel_a": ["dólar", "china"]},
    
    # Telecom
    "VIVT3.SA": {"nome": "Vivo", "setor": "Telecom", "sensivel_a": ["juros", "consumo"]},
    "OIBR3.SA": {"nome": "Oi", "setor": "Telecom", "sensivel_a": ["juros", "consumo"]},
}

# ============================================
# PRINCIPAIS EMPRESAS GLOBAIS
# ============================================

EMPRESAS_GLOBAIS = {
    # Tech - EUA
    "AAPL": {"nome": "Apple", "bolsa": "NASDAQ", "sensivel_a": ["china", "dólar"]},
    "MSFT": {"nome": "Microsoft", "bolsa": "NASDAQ", "sensivel_a": ["juros", "tech"]},
    "GOOGL": {"nome": "Google", "bolsa": "NASDAQ", "sensivel_a": ["regulação", "tech"]},
    "AMZN": {"nome": "Amazon", "bolsa": "NASDAQ", "sensivel_a": ["juros", "consumo"]},
    "NVDA": {"nome": "Nvidia", "bolsa": "NASDAQ", "sensivel_a": ["tech", "china"]},
    
    # Financeiro - EUA
    "JPM": {"nome": "JPMorgan", "bolsa": "NYSE", "sensivel_a": ["juros", "economia"]},
    "BAC": {"nome": "Bank of America", "bolsa": "NYSE", "sensivel_a": ["juros", "economia"]},
    
    # Energia - EUA
    "XOM": {"nome": "ExxonMobil", "bolsa": "NYSE", "sensivel_a": ["petróleo", "geopolítica"]},
    "CVX": {"nome": "Chevron", "bolsa": "NYSE", "sensivel_a": ["petróleo", "geopolítica"]},
    
    # Luxo - Europa
    "LVMH.PA": {"nome": "LVMH", "bolsa": "Euronext", "sensivel_a": ["consumo", "china"]},
    
    # Automotivo - Europa
    "SAP.DE": {"nome": "SAP", "bolsa": "DAX", "sensivel_a": ["tech", "economia"]},
    
    # Japão
    "6758.T": {"nome": "Sony", "bolsa": "Tokyo", "sensivel_a": ["tech", "china"]},
}

# ============================================
# MOEDAS E COMMODITIES
# ============================================

MOEDAS = {
    "USDBRL=X": "USD/BRL - Dólar Americano",
    "EURUSD=X": "EUR/USD - Euro",
    "GBPUSD=X": "GBP/USD - Libra Esterlina",
    "CNYJPY=X": "CNY/JPY - Yuan Chinês",
}

COMMODITIES = {
    "CL=F": "Petróleo WTI",
    "BZ=F": "Brent",
    "GC=F": "Ouro",
    "SI=F": "Prata",
    "ZS=F": "Soja",
    "ZW=F": "Trigo",
    "^GSPC": "S&P 500",
}

# ============================================
# MAPA DE IMPACTO MACROECONÔMICO
# ============================================

MAPA_MACRO_IMPACTO = {
    "petróleo_sobe": {
        "empresas": ["PETR4.SA"],
        "impacto": "positivo",
        "força": 0.8,
        "descricao": "Petrobras se beneficia de preços altos de petróleo"
    },
    "petróleo_cai": {
        "empresas": ["PETR4.SA"],
        "impacto": "negativo",
        "força": 0.8,
        "descricao": "Petrobras sofre com queda nos preços de petróleo"
    },
    "minério_sobe": {
        "empresas": ["VALE3.SA"],
        "impacto": "positivo",
        "força": 0.75,
        "descricao": "Vale se beneficia de preços altos de minério"
    },
    "china_desacelera": {
        "empresas": ["VALE3.SA", "SUZB3.SA"],
        "impacto": "negativo",
        "força": 0.7,
        "descricao": "Empresas exportadoras sofrem com desaceleração chinesa"
    },
    "juros_eua_sobem": {
        "empresas": ["ITUB4.SA", "BBAS3.SA", "SANB11.SA"],
        "impacto": "positivo",
        "força": 0.6,
        "descricao": "Bancos se beneficiam de juros mais altos"
    },
    "dólar_sobe": {
        "empresas": ["PETR4.SA", "VALE3.SA", "SUZB3.SA", "JBSS3.SA"],
        "impacto": "positivo",
        "força": 0.65,
        "descricao": "Exportadores se beneficiam de dólar mais forte"
    },
    "inflação_alta": {
        "empresas": ["ITUB4.SA", "BBAS3.SA"],
        "impacto": "positivo",
        "força": 0.55,
        "descricao": "Bancos se beneficiam com inflação"
    },
    "guerra_geopolitica": {
        "empresas": ["PETR4.SA"],
        "impacto": "positivo",
        "força": 0.7,
        "descricao": "Conflitos geopolíticos tendem a elevar petróleo"
    },
}

# ============================================
# PALAVRAS-CHAVE PARA ANÁLISE
# ============================================

PALAVRAS_CHAVE_POSITIVAS = [
    "alta", "crescimento", "lucro", "ganho", "subida", "otimismo",
    "recuperação", "expansão", "sucesso", "aprovação", "positivo",
    "forte", "bom", "excelente", "recorde", "melhor"
]

PALAVRAS_CHAVE_NEGATIVAS = [
    "queda", "crise", "prejuízo", "perda", "recessão", "pessimismo",
    "colapso", "fracasso", "rejeição", "negativo", "fraco",
    "ruim", "pior", "desastre", "falha", "problema"
]

# ============================================
# CONFIGURAÇÕES DE ANÁLISE
# ============================================

SENTIMENTO_THRESHOLD = 0.5  # Limiar para considerar sentimento significativo
CONFIANCA_MINIMA = 0.4      # Confiança mínima para gerar recomendação
SCORE_COMPRA = 0.6          # Score mínimo para recomendar compra
SCORE_VENDA = -0.6          # Score máximo para recomendar venda

# ============================================
# FONTES DE NOTÍCIAS
# ============================================

FONTES_NOTICIAS = {
    "reuters": "https://www.reuters.com",
    "bloomberg": "https://www.bloomberg.com",
    "cnbc": "https://www.cnbc.com",
    "ft": "https://www.ft.com",
    "g1": "https://g1.globo.com/economia/",
    "valor": "https://valor.globo.com",
    "infomoney": "https://www.infomoney.com.br",
    "investing": "https://br.investing.com",
}

# ============================================
# CONFIGURAÇÕES DE LOGGING
# ============================================

LOG_LEVEL = "INFO"
LOG_FILE = "cauazinho.log"

print("✅ Configurações carregadas com sucesso!")
