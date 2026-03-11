# 🔑 COMO CONFIGURAR A CHAVE NEWS_API_KEY

## 📍 LOCALIZAÇÃO EXATA DOS ARQUIVOS

Sua estrutura de pasta deve ser assim:

```
C:\Users\taina\OneDrive\Pictures\Documentos\projetos Python\agente_Cauãzinho\
│
├── main.py                    ← Arquivo principal
├── config.py                  ← Configurações
├── data_collector.py
├── news_collector.py
├── sentiment_analyzer.py
├── macro_analyzer.py
├── report_generator.py
├── requirements.txt
├── .env                       ← ⭐ ARQUIVO QUE VOCÊ PRECISA CRIAR
├── .env.example               ← Modelo de exemplo
└── README.md
```

---

## 🔑 PASSO 1: OBTER A CHAVE NEWS_API_KEY

### 1.1 Abra o navegador
- Vá para: **https://newsapi.org**

### 1.2 Clique em "Get API Key"
- Você verá um botão no topo da página

### 1.3 Crie uma conta (é gratuita!)
- Email
- Senha
- Confirme email

### 1.4 Copie sua chave
- Você receberá uma chave assim:
```
abc123def456ghi789jkl012mno345pqr678stu
```

**Copie essa chave!** Você vai precisar dela.

---

## 📝 PASSO 2: CRIAR O ARQUIVO .env

### 2.1 Abra o VS Code

### 2.2 Clique em "File" → "New File"

### 2.3 Copie e cole isto:
```
NEWS_API_KEY=sua_chave_aqui
LOG_LEVEL=INFO
LOG_FILE=cauazinho.log
SENTIMENTO_THRESHOLD=0.5
CONFIANCA_MINIMA=0.4
SCORE_COMPRA=0.6
SCORE_VENDA=-0.6
ATUALIZAR_A_CADA_MINUTOS=60
SALVAR_RELATORIO=true
EXIBIR_CONSOLE=true
```

### 2.4 Substitua "sua_chave_aqui" pela sua chave
```
NEWS_API_KEY=abc123def456ghi789jkl012mno345pqr678stu
```

### 2.5 Salve como ".env"

**IMPORTANTE**: O nome do arquivo deve ser exatamente `.env` (com o ponto na frente)

No VS Code:
1. Pressione **Ctrl + Shift + S** (Save As)
2. Digite: `.env`
3. Certifique-se de que está na pasta raiz do projeto
4. Clique em **Save**

---

## ✅ PASSO 3: VERIFICAR SE ESTÁ CORRETO

### 3.1 Verifique a localização
O arquivo `.env` deve estar aqui:
```
C:\Users\taina\OneDrive\Pictures\Documentos\projetos Python\agente_Cauãzinho\.env
```

### 3.2 Abra o arquivo `.env` no VS Code
- Deve conter:
```
NEWS_API_KEY=abc123def456ghi789jkl012mno345pqr678stu
LOG_LEVEL=INFO
...
```

### 3.3 Teste a instalação
No terminal do VS Code:
```bash
python main.py
```

Se funcionar, você verá:
```
✅ Configurações carregadas com sucesso!
```

---

## 🆘 PROBLEMAS COMUNS

### ❌ Erro: "ModuleNotFoundError: No module named 'yfinance'"

**Solução:**
```bash
# Certifique-se de que (venv) está ativo
# Depois reinstale:
pip install -r requirements.txt
```

### ❌ Erro: "No module named 'dotenv'"

**Solução:**
```bash
pip install python-dotenv
```

### ❌ Arquivo .env não é reconhecido

**Solução:**
- Verifique se o nome é exatamente `.env` (com ponto)
- Não é `.env.txt` ou `env.txt`
- Está na pasta raiz do projeto

### ❌ Chave NEWS_API_KEY não funciona

**Solução:**
- Verifique se copiou corretamente
- Não adicione espaços extras
- Formato correto: `NEWS_API_KEY=abc123...`

---

## 📋 CHECKLIST FINAL

- [ ] Criei conta em https://newsapi.org
- [ ] Copiei minha chave NEWS_API_KEY
- [ ] Criei arquivo `.env` na pasta raiz
- [ ] Adicionei a chave no arquivo `.env`
- [ ] Salvei o arquivo `.env`
- [ ] Rodei `pip install -r requirements.txt`
- [ ] Rodei `python main.py` com sucesso

---

## 🎉 PRONTO!

Agora o Cauãzinho está 100% configurado e pronto para rodar!

Execute:
```bash
python main.py
```

Boa sorte! 📈🤖
