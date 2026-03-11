# 🤖 SETUP BOT WHATSAPP - CAUÃZINHO

## 📱 O QUE É

Um **BOT PROFISSIONAL DE WHATSAPP** que:

✅ Recebe mensagens no WhatsApp
✅ Analisa notícias de mercado financeiro
✅ Recomenda ações para COMPRAR/VENDER
✅ Explica o porquê com justificativas
✅ Funciona 24/7 na nuvem
✅ Você pode vender esse serviço! 💰

---

## 🎯 COMO FUNCIONA

### Usuário envia:
```
Oi Cauãzinho, o que você tem pra mim hoje?
```

### Bot responde:
```
📊 RESUMO DO MERCADO DE HOJE

📰 Notícias analisadas: 45
📈 Positivas: 18 (40%)
📉 Negativas: 15 (33%)

🟢 Sinais de COMPRA: 3
🔴 Sinais de VENDA: 2

🌍 Temas em destaque:
   • petróleo
   • china
   • dólar
   • juros_eua
```

---

## 🔑 PASSO 1: OBTER CREDENCIAIS TWILIO

### 1.1 Criar conta Twilio
1. Acesse: https://www.twilio.com
2. Clique em **"Sign Up"**
3. Preencha os dados
4. Confirme email

### 1.2 Ativar WhatsApp Sandbox
1. No painel Twilio, vá para **Messaging → WhatsApp**
2. Clique em **"Try it out"**
3. Clique em **"Create a WhatsApp Sandbox"**
4. Siga as instruções

### 1.3 Obter credenciais
1. Vá para **Account → API Keys & tokens**
2. Copie:
   - **Account SID**
   - **Auth Token**
3. Vá para **Messaging → WhatsApp**
4. Copie o **número WhatsApp do Sandbox**

Exemplo:
```
Account SID: ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Auth Token: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Phone: whatsapp:+1415xxxxxxxxx
```

---

## 📝 PASSO 2: CONFIGURAR ARQUIVO .env

Abra o arquivo `.env` e configure:

```
NEWS_API_KEY=316d15e2877042588239d22f7db1e04f
LOG_LEVEL=INFO
LOG_FILE=cauazinho.log
SENTIMENTO_THRESHOLD=0.5
CONFIANCA_MINIMA=0.4
SCORE_COMPRA=0.6
SCORE_VENDA=-0.6
ATUALIZAR_A_CADA_MINUTOS=60
SALVAR_RELATORIO=true
EXIBIR_CONSOLE=true

# Twilio WhatsApp - CONFIGURE AQUI
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_PHONE=whatsapp:+1415xxxxxxxxx

# Servidor
PORT=5000
FLASK_ENV=production
```

**Substitua os valores com suas credenciais Twilio!**

---

## 🚀 PASSO 3: INSTALAR DEPENDÊNCIAS

```bash
pip install -r requirements.txt
```

---

## 🌐 PASSO 4: FAZER SERVIDOR PÚBLICO

O BOT precisa de um servidor público para receber mensagens do WhatsApp.

### Opção A: Usar Ngrok (Teste Local)

1. Baixe Ngrok: https://ngrok.com/download
2. Extraia em uma pasta
3. Abra terminal e execute:

```bash
ngrok http 5000
```

Você verá:
```
Forwarding                    https://abc123def456.ngrok.io -> http://localhost:5000
```

Copie a URL: `https://abc123def456.ngrok.io`

### Opção B: Deploy na Nuvem (Produção)

Recomendado para vender o serviço:
- **Heroku** (fácil, gratuito)
- **Railway** (simples)
- **Render** (rápido)
- **AWS** (profissional)

Vou criar guia de Heroku depois.

---

## 🔗 PASSO 5: CONFIGURAR WEBHOOK NO TWILIO

### 5.1 No painel Twilio
1. Vá para **Messaging → WhatsApp → Sandbox Settings**
2. Procure por **"When a message comes in"**
3. Cole a URL:
```
https://sua_url_aqui.ngrok.io/whatsapp
```

Exemplo:
```
https://abc123def456.ngrok.io/whatsapp
```

4. Clique em **Save**

---

## 📱 PASSO 6: TESTAR O BOT

### 6.1 Iniciar o servidor
```bash
python whatsapp_bot.py
```

Você verá:
```
🚀 Iniciando Cauãzinho Bot...
📱 Aguardando mensagens do WhatsApp...
```

### 6.2 Enviar mensagem de teste
1. Abra WhatsApp
2. Envie mensagem para o número Twilio
3. Escreva: `oi`

### 6.3 Resposta esperada
```
🤖 Oi! Sou o Cauãzinho! 👋

Escreva um dos comandos:

📊 resumo - Resumo do mercado hoje
🟢 compra - Ações para COMPRAR
🔴 venda - Ações para VENDER
📰 notícias - Top notícias
❓ ajuda - Ver comandos
```

---

## 🎮 COMANDOS DISPONÍVEIS

| Comando | O que faz |
|---------|-----------|
| `oi` / `olá` | Saudação e menu |
| `resumo` | Resumo do mercado hoje |
| `compra` | Ações para COMPRAR |
| `venda` | Ações para VENDER |
| `notícias` | Top notícias positivas/negativas |
| `ajuda` | Ver todos os comandos |

---

## 📊 EXEMPLO DE CONVERSA

**Usuário:**
```
Oi Cauãzinho!
```

**Bot:**
```
🤖 Oi! Sou o Cauãzinho! 👋

Escreva um dos comandos:

📊 resumo - Resumo do mercado hoje
🟢 compra - Ações para COMPRAR
🔴 venda - Ações para VENDER
📰 notícias - Top notícias
❓ ajuda - Ver comandos
```

**Usuário:**
```
compra
```

**Bot:**
```
🟢 RECOMENDAÇÕES DE COMPRA

1. PETR4 - Petrobras
📈 Score: +0.75
💪 Confiança: 80%
📌 Por quê:
   • Petrobras se beneficia de preços altos de petróleo
   • Dólar em alta favorece exportadores

2. VALE3 - Vale
📈 Score: +0.62
💪 Confiança: 75%
📌 Por quê:
   • China aumenta importações de minério
   • Preço do minério em alta
```

---

## 💰 MONETIZAR SEU BOT

### Opções:

1. **Assinatura Mensal**
   - R$ 99/mês por acesso ao bot
   - Análises diárias
   - Recomendações personalizadas

2. **Por Análise**
   - R$ 10 por análise
   - Usuário paga conforme usa

3. **Premium**
   - R$ 199/mês
   - Análises em tempo real
   - Suporte prioritário
   - Alertas por SMS

4. **Vender para Corretoras**
   - Integrar com plataformas de trading
   - Licença por corretora

---

## 🚀 DEPLOY NA NUVEM (HEROKU)

### 1. Criar conta Heroku
- Acesse: https://www.heroku.com
- Clique em **Sign Up**

### 2. Instalar Heroku CLI
- Baixe em: https://devcenter.heroku.com/articles/heroku-cli

### 3. Fazer login
```bash
heroku login
```

### 4. Criar app
```bash
heroku create seu-app-cauazinho
```

### 5. Configurar variáveis
```bash
heroku config:set TWILIO_ACCOUNT_SID=seu_sid
heroku config:set TWILIO_AUTH_TOKEN=seu_token
heroku config:set TWILIO_PHONE=whatsapp:+seu_numero
heroku config:set NEWS_API_KEY=seu_api_key
```

### 6. Fazer deploy
```bash
git push heroku main
```

### 7. Atualizar webhook Twilio
- URL: `https://seu-app-cauazinho.herokuapp.com/whatsapp`

---

## 🛠️ TROUBLESHOOTING

### ❌ Erro: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### ❌ Erro: "Twilio não configurado"
- Verifique credenciais em `.env`
- Verifique se Account SID e Auth Token estão corretos

### ❌ Bot não responde
- Verifique se webhook está configurado
- Verifique URL do ngrok/servidor
- Verifique logs: `tail -f cauazinho.log`

### ❌ Mensagens não chegam
- Verifique número WhatsApp Twilio
- Verifique se está no Sandbox
- Verifique credenciais

---

## 📊 MONITORAR BOT

### Ver logs
```bash
tail -f cauazinho.log
```

### Health check
```bash
curl http://localhost:5000/health
```

Resposta:
```json
{
  "status": "ok",
  "timestamp": "2026-03-03T14:30:00",
  "ultima_analise": "2026-03-03T14:30:00"
}
```

---

## 📈 PRÓXIMAS MELHORIAS

- [ ] Integração com banco de dados
- [ ] Histórico de conversas
- [ ] Análise de portfólio do usuário
- [ ] Alertas automáticos
- [ ] Integração com corretoras
- [ ] Dashboard de usuários
- [ ] Cobrança automática

---

## 🎉 PRONTO!

Agora você tem um **BOT PROFISSIONAL DE WHATSAPP** que:

✅ Analisa mercado financeiro
✅ Recomenda ações
✅ Funciona 24/7
✅ Você pode vender! 💰

**Comece a ganhar dinheiro com análises de mercado!** 📈🤖💰

---

## 📞 SUPORTE

Para dúvidas:
1. Verifique os logs
2. Teste com ngrok localmente
3. Verifique credenciais Twilio
4. Reinicie o servidor

**Boa sorte!** 🚀
