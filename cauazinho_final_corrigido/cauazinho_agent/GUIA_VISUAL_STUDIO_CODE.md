# 🎯 GUIA COMPLETO - Rodando Cauãzinho no Visual Studio Code

## 📋 Pré-requisitos

- ✅ Python 3.8+ instalado
- ✅ Visual Studio Code instalado
- ✅ Conexão com internet

---

## 🚀 PASSO 1: Instalar Python

### Windows:
1. Acesse: https://www.python.org/downloads/
2. Clique em **"Download Python 3.11"** (ou versão mais recente)
3. Execute o instalador
4. ⚠️ **IMPORTANTE**: Marque a opção **"Add Python to PATH"**
5. Clique em **"Install Now"**

### Mac:
```bash
# Instale via Homebrew
brew install python3
```

### Linux:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Verificar Instalação:
Abra o Terminal/Prompt e digite:
```bash
python --version
```

Deve mostrar algo como: `Python 3.11.x`

---

## 🎨 PASSO 2: Instalar Visual Studio Code

1. Acesse: https://code.visualstudio.com/
2. Clique em **"Download"**
3. Escolha seu sistema operacional
4. Execute o instalador
5. Abra o VS Code

---

## 📁 PASSO 3: Abrir o Projeto no VS Code

### Opção A: Via Pasta

1. Abra o **VS Code**
2. Clique em **File** → **Open Folder**
3. Navegue até: `C:\Users\SeuUsuario\cauazinho_agent` (Windows)
   - Ou `/home/usuario/cauazinho_agent` (Linux/Mac)
4. Clique em **Select Folder**

### Opção B: Via Terminal

1. Abra o Terminal/Prompt de Comando
2. Digite:
```bash
cd C:\caminho\para\cauazinho_agent
code .
```

---

## 🔧 PASSO 4: Instalar Extensões Recomendadas

No VS Code, clique no ícone de **Extensões** (lado esquerdo):

### Extensões Essenciais:

1. **Python** (Microsoft)
   - Clique em **Install**
   - Fornece suporte completo para Python

2. **Pylance** (Microsoft)
   - Autocompletar avançado
   - Verificação de erros

3. **Python Docstring Generator** (Nils Werner)
   - Gera documentação automaticamente

4. **Better Comments** (Aaron Bond)
   - Comentários coloridos

5. **Thunder Client** ou **REST Client** (opcional)
   - Para testar APIs

---

## 🐍 PASSO 5: Configurar Ambiente Virtual

### No VS Code, abra o Terminal Integrado:

**Windows/Mac/Linux:**
1. Pressione **Ctrl + `** (backtick)
2. Ou vá em **View** → **Terminal**

### Criar Ambiente Virtual:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Você verá `(venv)` no início da linha do terminal.

---

## 📦 PASSO 6: Instalar Dependências

No terminal do VS Code (com venv ativado), digite:

```bash
pip install -r requirements.txt
```

Isso vai instalar:
- yfinance (dados de mercado)
- feedparser (RSS feeds)
- textblob (análise de sentimento)
- requests (HTTP)
- pandas (análise de dados)
- E mais...

⏳ Isso pode levar **2-5 minutos**. Aguarde!

---

## 🔑 PASSO 7: Configurar API (Opcional)

Se quiser usar **notícias globais**:

1. Acesse: https://newsapi.org
2. Clique em **"Get API Key"**
3. Crie uma conta (gratuita)
4. Copie sua chave

No VS Code:

1. Abra o arquivo `.env.example`
2. Clique em **File** → **Save As**
3. Renomeie para `.env`
4. Edite a linha:
```
NEWS_API_KEY=sua_chave_aqui
```

5. Cole sua chave
6. Salve (Ctrl + S)

---

## ▶️ PASSO 8: Executar o Cauãzinho

### Opção A: Via Terminal do VS Code

1. Abra o Terminal (Ctrl + `)
2. Certifique-se de que `(venv)` está ativo
3. Digite:
```bash
python main.py
```

### Opção B: Via Botão Play

1. Abra o arquivo `main.py`
2. Clique no botão **▶️ Play** (canto superior direito)
3. Ou pressione **F5**

### Opção C: Via Run and Debug

1. Pressione **Ctrl + Shift + D**
2. Clique em **"Run and Debug"**
3. Selecione **"Python"**

---

## 📊 PASSO 9: Acompanhar a Execução

No terminal do VS Code, você verá:

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🤖 AGENTE FINANCEIRO CAUÃZINHO 🤖                        ║
║                      RELATÓRIO DE ANÁLISE DE MERCADO                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

================================================================================
ETAPA 1: COLETA DE DADOS DO MERCADO
================================================================================

📊 Coletando índices globais...
  ✅ IBOV: 123456.78 (+2.50%)
  ✅ SP500: 5000.00 (+1.20%)
  ...

📊 Coletando dados da B3...
  ✅ Petrobras (PETR4): R$ 25.50 (+5.20%)
  ✅ Vale (VALE3): R$ 80.30 (+3.10%)
  ...
```

---

## 📄 PASSO 10: Ver o Relatório

Quando terminar, você verá:

1. **No Terminal**: Relatório completo com recomendações
2. **Em Arquivo**: Um arquivo `.txt` será criado com nome como:
   ```
   relatorio_cauazinho_20260301_143045.txt
   ```

### Para Abrir o Relatório no VS Code:

1. Clique em **File** → **Open File**
2. Selecione o arquivo `relatorio_cauazinho_*.txt`
3. Leia as recomendações

---

## 🎮 PASSO 11: Menu Interativo

Após a execução, você verá:

```
================================================================================
MENU DE OPÇÕES
================================================================================
1. Executar análise completa novamente
2. Exibir relatório atual
3. Exibir recomendações de compra
4. Exibir recomendações de venda
5. Exibir análise de sentimento
6. Sair
================================================================================

Escolha uma opção (1-6):
```

Digite um número (1-6) e pressione **Enter**.

---

## 🔍 PASSO 12: Entender os Resultados

### 🟢 COMPRA (Score > 0.6)
```
🎯 PETR4 - Petrobras
   Score de Impacto: +0.75
   Confiança: 80%
   
   📌 Justificativa:
      • Petrobras se beneficia de preços altos de petróleo
        Tema: petróleo (positivo)
        Notícia: Petróleo sobe com tensões no Oriente Médio...
```

**Significado**: Boas chances de subida. Considere comprar.

### 🔴 VENDA (Score < -0.6)
```
⚠️ VALE3 - Vale
   Score de Impacto: -0.65
   Confiança: 75%
   
   📌 Justificativa:
      • China desacelera impacta exportadores
        Tema: china (negativo)
        Notícia: Economia chinesa cresce menos que esperado...
```

**Significado**: Risco de queda. Considere vender.

### ⚪ NEUTRO (-0.6 < Score < 0.6)
**Significado**: Sem sinal claro. Aguarde mais informações.

---

## 🛠️ TROUBLESHOOTING

### ❌ Erro: "python: command not found"

**Solução:**
- Reinstale Python marcando **"Add Python to PATH"**
- Reinicie o VS Code
- Ou use `python3` em vez de `python`

### ❌ Erro: "ModuleNotFoundError: No module named 'yfinance'"

**Solução:**
```bash
# Certifique-se de que (venv) está ativo
pip install -r requirements.txt
```

### ❌ Erro: "No module named 'dotenv'"

**Solução:**
```bash
pip install python-dotenv
```

### ❌ Terminal não reconhece (venv)

**Solução:**
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### ❌ NewsAPI não funciona

**Solução:**
- Ignore se não quiser usar notícias globais
- Ou obtenha uma chave em https://newsapi.org
- Configure em `.env`

---

## ⚙️ CONFIGURAÇÕES RECOMENDADAS DO VS CODE

### Abrir Configurações:
1. Pressione **Ctrl + ,**
2. Ou vá em **File** → **Preferences** → **Settings**

### Configurações Úteis:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.python",
    "terminal.integrated.defaultProfile.windows": "Command Prompt",
    "terminal.integrated.defaultProfile.osx": "bash",
    "terminal.integrated.defaultProfile.linux": "bash"
}
```

---

## 🔄 EXECUTAR DIARIAMENTE

Para rodar o Cauãzinho todos os dias:

### Opção 1: Manual
```bash
# Abra o VS Code
# Pressione Ctrl + `
# Digite: python main.py
```

### Opção 2: Criar Tarefa Agendada (Windows)

1. Pressione **Win + R**
2. Digite: `taskschd.msc`
3. Clique em **Create Basic Task**
4. Nome: "Cauãzinho Diário"
5. Trigger: **Daily** às 14:00
6. Action: **Start a program**
7. Program: `C:\Python311\python.exe`
8. Arguments: `C:\caminho\para\main.py`

### Opção 3: Cron Job (Mac/Linux)

```bash
# Abra o editor
crontab -e

# Adicione a linha (executa diariamente às 14:00)
0 14 * * * cd /home/usuario/cauazinho_agent && python main.py >> relatorio.log 2>&1
```

---

## 📚 PRÓXIMOS PASSOS

1. ✅ Execute o agente
2. ✅ Analise as recomendações
3. ✅ Valide com sua estratégia
4. ✅ Customize `config.py` com suas empresas favoritas
5. ✅ Acompanhe os relatórios diários

---

## 🎓 DICAS IMPORTANTES

1. **Não confie 100%** nas recomendações
2. **Sempre consulte um analista** antes de investir
3. **Considere seu perfil de risco**
4. **Diversifique seus investimentos**
5. **Mercados são voláteis** - nenhum sistema prevê 100%

---

## 🆘 PRECISA DE AJUDA?

Se tiver problemas:

1. Verifique se Python está instalado: `python --version`
2. Verifique se venv está ativo: deve ter `(venv)` no terminal
3. Reinstale dependências: `pip install -r requirements.txt`
4. Limpe cache: `rm -rf __pycache__` (Mac/Linux) ou `rmdir /s __pycache__` (Windows)
5. Reinicie o VS Code

---

## 🎉 PRONTO!

Agora você tem um **agente financeiro profissional** rodando no seu computador! 

Execute `python main.py` e comece a analisar o mercado! 📈🤖

**Boa sorte nos investimentos!** 💰
