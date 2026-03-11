# p⚡ Guia de Início Rápido - Cauãzinho

## 🚀 5 Minutos para Começar

### Passo 1: Instale Python (se não tiver)

Baixe em: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Verifique a instalação:

```bash
python --version
```

### Passo 2: Abra o Terminal/Prompt de Comando

Windows: `Win + R` → `cmd`Mac/Linux: Abra o Terminal

### Passo 3: Navegue até a pasta do projeto

```bash
cd C:\caminho\para\cauazinho_agent
```

### Passo 4: Instale as dependências

```bash
pip install -r requirements.txt
```

Isso pode levar 2-3 minutos.

### Passo 5: Configure a API (Opcional )

Para usar notícias globais:

1. Vá para [https://newsapi.org](https://newsapi.org)

1. Clique em "Get API Key"

1. Copie sua chave

1. Abra o arquivo `.env` e cole:

```
NEWS_API_KEY=sua_chave_aqui
```

### Passo 6: Execute o agente

```bash
python main.py
```

## ✅ Pronto!

O Cauãzinho irá:

- 📊 Coletar dados de bolsas

- 📰 Buscar notícias

- 🧠 Analisar sentimento

- 💡 Gerar recomendações

- 📄 Salvar relatório

## 📊 Interpretando os Resultados

### 🟢 COMPRA

Empresa tem boas chances de subir

- Compre se você acredita no potencial

### 🔴 VENDA

Empresa tem risco de queda

- Venda se você quer reduzir risco

### ⚪ NEUTRO

Sem sinal claro

- Aguarde mais informações

## 🎯 Próximos Passos

1. **Leia o README.md** para documentação completa

1. **Customize config.py** para adicionar suas empresas favoritas

1. **Explore as recomendações** e valide com sua estratégia

1. **Acompanhe os relatórios** gerados diariamente

## 💡 Dicas

- Execute o agente **todos os dias** para acompanhar mudanças

- **Não confie 100%** nas recomendações - sempre valide

- **Considere seu perfil de risco** antes de investir

- **Diversifique** seus investimentos

## ❓ Problemas Comuns

### "ModuleNotFoundError: No module named 'yfinance'"

```bash
pip install -r requirements.txt
```

### "NewsAPI key not configured"

- Ignore se não quiser usar notícias globais

- Ou configure em `.env`

### "Connection timeout"

- Verifique sua internet

- Tente novamente em alguns minutos

## 📚 Aprenda Mais

- [README.md](README.md) - Documentação completa

- [config.py](config.py) - Configurações e tickers

- [main.py](main.py) - Código principal

## 🎓 Conceitos Importantes

### Sentimento

- **Positivo**: Notícia favorável para o ativo

- **Negativo**: Notícia desfavorável

- **Neutro**: Sem impacto claro

### Score de Impacto

- **+1.0**: Muito positivo (forte compra)

- **0.0**: Neutro

- **-1.0**: Muito negativo (forte venda)

### Confiança

- **100%**: Muito confiável

- **50%**: Moderadamente confiável

- **0%**: Pouco confiável

## 🔒 Segurança

- ✅ Nunca compartilhe sua chave de API

- ✅ Mantenha `.env` seguro

- ✅ Use credenciais diferentes para produção

## 🚀 Agora é com você!

Execute o agente e comece a analisar o mercado:

```bash
python main.py
```

Boa sorte! 📈🤖

