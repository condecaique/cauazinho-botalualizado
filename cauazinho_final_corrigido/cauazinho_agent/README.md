# 🤖 CAUÃZINHO - Agente Financeiro Inteligente

Um agente de análise de mercado financeiro em Python que monitora notícias globais, analisa geopolítica, decisões de empresários e manobras governamentais para gerar recomendações de compra e venda de ações.

## 🎯 Funcionalidades

✅ **Coleta de Dados em Tempo Real**
- Índices globais (Ibovespa, S&P 500, Nasdaq, DAX, etc)
- Todas as principais empresas da B3
- Empresas globais (Apple, Microsoft, Google, etc)
- Moedas (USD/BRL, EUR/USD, etc)
- Commodities (Petróleo, Ouro, Soja, etc)

✅ **Coleta de Notícias Multi-Fonte**
- RSS feeds de portais econômicos brasileiros
- NewsAPI para notícias globais
- Filtro automático de notícias relevantes
- Remoção de duplicatas

✅ **Análise de Sentimento**
- TextBlob para análise de polaridade
- Análise por palavras-chave
- Confiança de sentimento
- Classificação: Positivo, Negativo, Neutro

✅ **Análise Macroeconômica**
- Detecção automática de temas (petróleo, china, juros, etc)
- Correlação macro com empresas
- Impacto de geopolítica em setores
- Scoring de recomendações

✅ **Recomendações Inteligentes**
- Sinais de COMPRA com justificativa
- Sinais de VENDA com justificativa
- Score de confiança
- Análise de riscos

✅ **Relatórios Executivos**
- Relatório completo em texto
- Resumo executivo
- Estado do mercado
- Top notícias positivas/negativas
- Recomendações detalhadas

## 📋 Requisitos

- Python 3.8+
- pip (gerenciador de pacotes)
- Conexão com internet

## 🚀 Instalação

### 1. Clone ou baixe o projeto

```bash
cd /caminho/do/projeto/cauazinho_agent
```

### 2. Crie um ambiente virtual (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env e adicione sua chave NewsAPI
# Obtenha uma chave gratuita em: https://newsapi.org
```

## 📖 Como Usar

### Execução Básica

```bash
python main.py
```

O agente irá:
1. ✅ Coletar dados de todas as bolsas
2. ✅ Buscar notícias de múltiplas fontes
3. ✅ Analisar sentimento de cada notícia
4. ✅ Detectar temas macroeconômicos
5. ✅ Gerar recomendações de compra/venda
6. ✅ Salvar relatório em arquivo

### Menu Interativo

Após a execução, você terá acesso a um menu com opções:

```
1. Executar análise completa novamente
2. Exibir relatório atual
3. Exibir recomendações de compra
4. Exibir recomendações de venda
5. Exibir análise de sentimento
6. Sair
```

## 📁 Estrutura do Projeto

```
cauazinho_agent/
│
├── main.py                    # Arquivo principal (orquestra tudo)
├── config.py                  # Configurações (tickers, APIs, etc)
├── data_collector.py          # Coleta dados de bolsas
├── news_collector.py          # Coleta notícias
├── sentiment_analyzer.py      # Análise de sentimento
├── macro_analyzer.py          # Análise macroeconômica
├── report_generator.py        # Geração de relatórios
├── requirements.txt           # Dependências Python
├── .env.example              # Exemplo de variáveis de ambiente
└── README.md                 # Este arquivo
```

## 🔧 Configuração Avançada

### Adicionar Novas Empresas

Edite `config.py` e adicione à seção `EMPRESAS_B3_PRINCIPAIS`:

```python
"NOVO4.SA": {
    "nome": "Nova Empresa",
    "setor": "Seu Setor",
    "sensivel_a": ["tema1", "tema2"]
}
```

### Adicionar Novas Fontes de Notícias

Edite `news_collector.py` e adicione à lista `fontes_rss`:

```python
self.fontes_rss = [
    "https://seu-portal.com/rss",
    # ... outras fontes
]
```

### Customizar Análise de Sentimento

Edite `config.py` e modifique:

```python
PALAVRAS_CHAVE_POSITIVAS = [...]
PALAVRAS_CHAVE_NEGATIVAS = [...]
```

## 📊 Exemplo de Saída

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🤖 AGENTE FINANCEIRO CAUÃZINHO 🤖                        ║
║                      RELATÓRIO DE ANÁLISE DE MERCADO                         ║
║                          01/03/2026 às 14:30:45                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📋 RESUMO EXECUTIVO
────────────────────────────────────────────────────────────────────────────────

📊 Análise de Notícias:
   • Total de notícias analisadas: 45
   • Sentimento positivo: 18 (40.0%)
   • Sentimento negativo: 15 (33.3%)
   • Sentimento neutro: 12 (26.7%)

💡 Recomendações Geradas:
   • Sinais de COMPRA: 3
   • Sinais de VENDA: 2
   • Sem sinal claro: 15

🌍 Temas Macroeconômicos Detectados: 5
   • Temas ativos: petróleo, dólar, china, juros_eua, inflação

...

🟢 RECOMENDAÇÕES DE COMPRA
────────────────────────────────────────────────────────────────────────────────

🎯 PETR4 - Petrobras
   Setor: Petróleo e Gás
   Score de Impacto: +0.75
   Confiança: 80%
   Sensível a: petróleo, dólar

   📌 Justificativa:
      • Petrobras se beneficia de preços altos de petróleo
        Tema: petróleo (positivo)
        Notícia: Petróleo sobe com tensões no Oriente Médio...

...
```

## 🔍 Interpretando as Recomendações

### COMPRA (🟢)
- Score positivo acima de 0.6
- Múltiplos temas positivos afetando a empresa
- Confiança alta (>60%)
- **Ação**: Considerar entrada na posição

### VENDA (🔴)
- Score negativo abaixo de -0.6
- Múltiplos temas negativos afetando a empresa
- Confiança alta (>60%)
- **Ação**: Considerar saída ou não entrar

### NEUTRO (⚪)
- Score entre -0.6 e 0.6
- Impactos equilibrados
- **Ação**: Aguardar mais clareza

## ⚠️ Avisos Importantes

1. **Este é um sistema educacional** - Não use como única fonte de decisão
2. **Sempre consulte um analista financeiro** antes de investir
3. **Valide as recomendações** com sua estratégia pessoal
4. **Considere seu perfil de risco** e horizonte de investimento
5. **Mercados são voláteis** - Nenhum sistema prevê 100%

## 🔐 Segurança

- Nunca compartilhe suas chaves de API
- Mantenha o arquivo `.env` seguro
- Use credenciais diferentes para produção
- Não armazene dados sensíveis no repositório

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Erro: "NewsAPI key not configured"
- Obtenha uma chave em https://newsapi.org
- Configure em `.env`

### Erro: "Connection timeout"
- Verifique sua conexão com internet
- Aumente o timeout em `data_collector.py`

### Erro: "No data available"
- Alguns tickers podem não ter dados
- Verifique se o ticker está correto no Yahoo Finance

## 📈 Próximas Melhorias

- [ ] Integração com banco de dados (PostgreSQL)
- [ ] Dashboard web em tempo real
- [ ] Machine Learning para previsão
- [ ] Backtesting automático
- [ ] Alertas por email/WhatsApp
- [ ] API REST para integração
- [ ] Análise de opções
- [ ] Análise técnica (gráficos)

## 📚 Recursos Úteis

- [Yahoo Finance](https://finance.yahoo.com) - Dados de mercado
- [NewsAPI](https://newsapi.org) - Notícias globais
- [B3 - Bolsa do Brasil](https://www.b3.com.br) - Informações da bolsa
- [Investing.com](https://br.investing.com) - Análises financeiras

## 👨‍💻 Desenvolvido por

**Cauãzinho** - Agente Financeiro Inteligente

## 📄 Licença

Este projeto é fornecido como está, para fins educacionais.

## 💬 Suporte

Para dúvidas ou sugestões, abra uma issue no repositório.

---

**Última atualização**: Março de 2026
**Versão**: 1.0.0
**Status**: ✅ Pronto para uso
