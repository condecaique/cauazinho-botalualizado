# 📚 Documentação Técnica - Cauãzinho

## 🏗️ Arquitetura do Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                     CAUÃZINHO AGENT                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Coleta     │  │   Análise    │  │  Geração de  │     │
│  │   de Dados   │→ │ Sentimento   │→ │  Relatório   │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│         ↓                  ↓                  ↓             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   Bolsas     │  │   Notícias   │  │   Análise    │     │
│  │   Globais    │  │   Relevantes │  │    Macro     │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 📊 Fluxo de Dados

```
1. DATA COLLECTOR
   ├─ Índices Globais (yfinance)
   ├─ Empresas B3 (yfinance)
   ├─ Empresas Globais (yfinance)
   ├─ Moedas (yfinance)
   └─ Commodities (yfinance)

2. NEWS COLLECTOR
   ├─ RSS Feeds (feedparser)
   ├─ NewsAPI (requests)
   ├─ Filtro de Relevância
   └─ Remoção de Duplicatas

3. SENTIMENT ANALYZER
   ├─ TextBlob (análise de polaridade)
   ├─ Palavras-chave (análise customizada)
   └─ Scoring de Confiança

4. MACRO ANALYZER
   ├─ Detecção de Temas
   ├─ Mapeamento de Impacto
   ├─ Correlação com Empresas
   └─ Scoring de Recomendação

5. REPORT GENERATOR
   ├─ Formatação de Relatório
   ├─ Justificativas
   └─ Exportação em Arquivo
```

## 🔧 Módulos Principais

### 1. config.py (227 linhas)

**Responsabilidade**: Centralizar todas as configurações

**Componentes**:
- `GLOBAL_INDICES`: Índices de bolsas mundiais
- `EMPRESAS_B3_PRINCIPAIS`: Tickers da B3 com metadados
- `EMPRESAS_GLOBAIS`: Tickers globais com metadados
- `MOEDAS`: Pares de moedas
- `COMMODITIES`: Commodities principais
- `MAPA_MACRO_IMPACTO`: Mapeamento de impacto macroeconômico
- `PALAVRAS_CHAVE_POSITIVAS/NEGATIVAS`: Dicionário de sentimento

**Uso**:
```python
from config import EMPRESAS_B3_PRINCIPAIS, MAPA_MACRO_IMPACTO
```

### 2. data_collector.py (240 linhas)

**Responsabilidade**: Coletar dados de mercado em tempo real

**Classe**: `DataCollector`

**Métodos Principais**:
```python
coletar_indices_globais()      # Coleta índices
coletar_empresas_b3()          # Coleta B3
coletar_empresas_globais()     # Coleta globais
coletar_moedas()               # Coleta moedas
coletar_commodities()          # Coleta commodities
coletar_tudo()                 # Executa tudo
gerar_resumo_mercado()         # Exibe resumo
```

**Retorno**:
```python
{
    "indices": {...},
    "b3": {...},
    "globais": {...},
    "moedas": {...},
    "commodities": {...}
}
```

**Estrutura de Dados**:
```python
{
    "ticker": "PETR4.SA",
    "nome": "Petrobras",
    "preco": 25.50,
    "variacao_30d": 5.2,
    "timestamp": datetime.now()
}
```

### 3. news_collector.py (217 linhas)

**Responsabilidade**: Coletar notícias de múltiplas fontes

**Classe**: `NewsCollector`

**Métodos Principais**:
```python
coletar_noticias_newsapi()     # Coleta via NewsAPI
coletar_noticias_rss()         # Coleta via RSS
filtrar_noticias_relevantes()  # Filtra por relevância
remover_duplicatas()           # Remove duplicatas
ordenar_por_data()             # Ordena cronologicamente
coletar_tudo()                 # Executa tudo
exibir_noticias()              # Exibe notícias
```

**Estrutura de Dados**:
```python
{
    "titulo": "Petrobras sobe com alta do petróleo",
    "descricao": "Ações registram ganho expressivo",
    "conteudo": "A empresa se beneficia...",
    "fonte": "G1 Economia",
    "url": "https://...",
    "data": "2026-03-01T14:30:00Z",
    "tipo": "rss" ou "newsapi"
}
```

### 4. sentiment_analyzer.py (202 linhas)

**Responsabilidade**: Analisar sentimento de notícias

**Classe**: `SentimentAnalyzer`

**Métodos Principais**:
```python
analisar_sentimento_textblob()      # TextBlob
analisar_sentimento_palavras_chave() # Palavras-chave
analisar_noticia()                   # Análise completa
analisar_lote()                      # Lote de notícias
gerar_relatorio_sentimento()         # Relatório
filtrar_por_sentimento()             # Filtro
filtrar_por_confianca()              # Filtro por confiança
```

**Retorno**:
```python
{
    "noticia": "Petrobras sobe...",
    "sentimento": "POSITIVO",
    "confianca": 0.85,
    "polaridade": 0.72,
    "subjetividade": 0.45
}
```

**Classificação**:
- `POSITIVO`: polaridade > 0.1
- `NEGATIVO`: polaridade < -0.1
- `NEUTRO`: -0.1 ≤ polaridade ≤ 0.1

### 5. macro_analyzer.py (242 linhas)

**Responsabilidade**: Análise macroeconômica e correlações

**Classe**: `MacroAnalyzer`

**Métodos Principais**:
```python
detectar_temas_noticias()       # Detecta temas
calcular_impacto_tema()         # Calcula impacto
analisar_impacto_empresas()     # Impacto em empresas
gerar_relatorio_macro()         # Relatório macro
obter_recomendacoes_top()       # Top recomendações
```

**Temas Detectados**:
- `petróleo`: Preços de petróleo
- `minério`: Preços de minério
- `china`: Economia chinesa
- `juros_eua`: Juros americanos
- `dólar`: Cotação do dólar
- `inflação`: Inflação global
- `guerra`: Conflitos geopolíticos
- `política`: Política governamental

**Scoring**:
```
Score = Σ(força_impacto × sentimento)

COMPRA:   score > 0.6
NEUTRO:   -0.6 ≤ score ≤ 0.6
VENDA:    score < -0.6
```

**Retorno**:
```python
{
    "PETR4.SA": {
        "score_total": 0.75,
        "confianca": 0.80,
        "recomendacao": "COMPRA",
        "impactos": [
            {
                "tema": "petróleo",
                "tipo": "positivo",
                "forca": 0.8,
                "descricao": "..."
            }
        ]
    }
}
```

### 6. report_generator.py (337 linhas)

**Responsabilidade**: Gerar relatórios executivos

**Classe**: `ReportGenerator`

**Métodos Principais**:
```python
gerar_relatorio_completo()      # Relatório completo
_gerar_cabecalho()              # Cabeçalho
_gerar_resumo_executivo()       # Resumo
_gerar_estado_mercado()         # Estado do mercado
_gerar_analise_sentimento()     # Análise de sentimento
_gerar_temas_macro()            # Temas macro
_gerar_recomendacoes_compra()   # Recomendações de compra
_gerar_recomendacoes_venda()    # Recomendações de venda
_gerar_riscos_oportunidades()   # Riscos e oportunidades
_gerar_rodape()                 # Rodapé
salvar_relatorio()              # Salva em arquivo
exibir_relatorio()              # Exibe no console
```

### 7. main.py (198 linhas)

**Responsabilidade**: Orquestrar todo o agente

**Classe**: `CauazinhoAgent`

**Métodos Principais**:
```python
coletar_dados()                 # Etapa 1
coletar_noticias()              # Etapa 2
analisar_sentimento()           # Etapa 3
analisar_macro()                # Etapa 4
gerar_relatorio()               # Etapa 5
executar()                      # Executa tudo
```

**Fluxo de Execução**:
```
main()
  ├─ CauazinhoAgent()
  ├─ agente.executar()
  │   ├─ coletar_dados()
  │   ├─ coletar_noticias()
  │   ├─ analisar_sentimento()
  │   ├─ analisar_macro()
  │   └─ gerar_relatorio()
  └─ Menu Interativo
```

## 🔄 Ciclo de Vida dos Dados

### 1. Entrada (Input)
```
APIs (yfinance, NewsAPI, RSS)
         ↓
    Dados Brutos
```

### 2. Processamento (Processing)
```
Dados Brutos
    ↓
Limpeza & Validação
    ↓
Análise de Sentimento
    ↓
Detecção de Temas
    ↓
Correlação Macro
    ↓
Scoring & Recomendação
```

### 3. Saída (Output)
```
Dados Processados
    ↓
Relatório Executivo
    ↓
Arquivo de Texto
```

## 📈 Algoritmo de Scoring

### Passo 1: Análise de Sentimento
```python
polaridade = TextBlob(texto).sentiment.polarity
# Resultado: -1 a 1
```

### Passo 2: Detecção de Tema
```python
if "petróleo" in texto.lower():
    tema = "petróleo"
```

### Passo 3: Impacto do Tema
```python
impacto = MAPA_MACRO_IMPACTO[tema]
# Resultado: força, tipo (positivo/negativo), empresas afetadas
```

### Passo 4: Cálculo de Score
```python
score = 0
for impacto in impactos_por_tema:
    if impacto["tipo"] == "positivo":
        score += impacto["força"]
    else:
        score -= impacto["força"]
```

### Passo 5: Recomendação
```python
if score > 0.6:
    recomendacao = "COMPRA"
elif score < -0.6:
    recomendacao = "VENDA"
else:
    recomendacao = "NEUTRO"
```

## 🔐 Tratamento de Erros

### Try-Except em Cada Módulo
```python
try:
    # Operação
except Exception as e:
    logger.error(f"Erro: {e}")
    # Continua com dados parciais
```

### Logging em Múltiplos Níveis
```python
logger.info()      # Informações gerais
logger.warning()   # Avisos
logger.error()     # Erros
```

## 🚀 Performance

### Otimizações Implementadas
1. **Cache de Dados**: Reutiliza dados coletados
2. **Batch Processing**: Processa múltiplas notícias
3. **Timeout**: Evita travamentos
4. **Logging Eficiente**: Não sobrecarrega I/O

### Tempo de Execução Esperado
- Coleta de Dados: ~30-60 segundos
- Coleta de Notícias: ~20-40 segundos
- Análise de Sentimento: ~10-20 segundos
- Análise Macro: ~5-10 segundos
- Geração de Relatório: ~2-5 segundos
- **Total**: ~1-2 minutos

## 🧪 Testes

### Teste Manual
```bash
python main.py
```

### Teste de Módulo Individual
```python
from data_collector import DataCollector
collector = DataCollector()
dados = collector.coletar_indices_globais()
print(dados)
```

## 📦 Dependências

| Pacote | Versão | Uso |
|--------|--------|-----|
| requests | 2.31.0 | HTTP requests |
| beautifulsoup4 | 4.12.2 | Web scraping |
| pandas | 2.1.3 | Análise de dados |
| yfinance | 0.2.32 | Dados de mercado |
| feedparser | 6.0.10 | RSS feeds |
| transformers | 4.35.2 | NLP (opcional) |
| torch | 2.1.1 | Deep Learning (opcional) |
| textblob | 0.17.1 | Análise de sentimento |
| python-dotenv | 1.0.0 | Variáveis de ambiente |
| newsapi | 0.1.2 | NewsAPI |

## 🔄 Extensibilidade

### Adicionar Novo Tema
1. Edite `config.py`
2. Adicione em `MAPA_MACRO_IMPACTO`
3. Adicione palavras-chave em `news_collector.py`

### Adicionar Nova Fonte de Notícias
1. Edite `news_collector.py`
2. Implemente novo método `coletar_noticias_[fonte]()`
3. Chame em `coletar_tudo()`

### Customizar Análise de Sentimento
1. Edite `sentiment_analyzer.py`
2. Implemente novo método de análise
3. Combine com análise existente

## 📊 Estrutura de Banco de Dados (Futuro)

```sql
CREATE TABLE noticias (
    id INT PRIMARY KEY,
    titulo VARCHAR(255),
    descricao TEXT,
    fonte VARCHAR(100),
    data DATETIME,
    sentimento VARCHAR(20),
    confianca FLOAT
);

CREATE TABLE empresas (
    ticker VARCHAR(10) PRIMARY KEY,
    nome VARCHAR(100),
    setor VARCHAR(50),
    preco FLOAT,
    variacao_30d FLOAT
);

CREATE TABLE recomendacoes (
    id INT PRIMARY KEY,
    ticker VARCHAR(10),
    tipo VARCHAR(10),
    score FLOAT,
    confianca FLOAT,
    data DATETIME
);
```

## 🎯 Roadmap

- [ ] v1.1: Banco de dados
- [ ] v1.2: Dashboard web
- [ ] v1.3: Machine Learning
- [ ] v1.4: Backtesting
- [ ] v1.5: Alertas em tempo real
- [ ] v2.0: API REST

---

**Última atualização**: Março de 2026
**Versão**: 1.0.0
