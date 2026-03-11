# 🎤 SETUP DE MENSAGENS DE VOZ - CAUÃZINHO BOT

## 📱 O QUE É

O bot agora recebe **mensagens de voz** no WhatsApp e:

✅ Transcreve áudio para texto
✅ Processa o comando
✅ Responde com análise
✅ Tudo automático!

---

## 🎯 COMO FUNCIONA

### Usuário envia:
```
🎤 [Mensagem de voz]
"Oi Cauãzinho, quais ações devo comprar hoje?"
```

### Bot:
1. Recebe o áudio
2. Transcreve: "quais ações devo comprar hoje"
3. Reconhece comando: `compra`
4. Responde com recomendações

```
🟢 RECOMENDAÇÕES DE COMPRA

1. PETR4 - Petrobras
📈 Score: +0.75
💪 Confiança: 80%
```

---

## 🔑 PASSO 1: OBTER CHAVE GOOGLE SPEECH-TO-TEXT

### 1.1 Criar projeto Google Cloud
1. Vá para: https://console.cloud.google.com
2. Clique em **"Create Project"**
3. Nome: `Cauazinho`
4. Clique em **Create**

### 1.2 Ativar Speech-to-Text API
1. Vá para **APIs & Services → Library**
2. Procure por: `Speech-to-Text`
3. Clique em **Enable**

### 1.3 Criar credenciais
1. Vá para **APIs & Services → Credentials**
2. Clique em **Create Credentials**
3. Selecione **Service Account**
4. Preencha os dados
5. Clique em **Create and Continue**
6. Clique em **Create Key**
7. Selecione **JSON**
8. Clique em **Create**

Um arquivo JSON será baixado.

### 1.4 Obter chave
1. Abra o arquivo JSON
2. Copie o valor de `"private_key"`
3. Ou use `"project_id"` e `"private_key_id"`

---

## 📝 PASSO 2: CONFIGURAR .env

Abra o arquivo `.env` e adicione:

```
GOOGLE_SPEECH_API_KEY=sua_chave_google_aqui
```

Ou se usar arquivo JSON:

```
GOOGLE_SPEECH_JSON_PATH=/caminho/para/seu/arquivo.json
```

---

## 🚀 PASSO 3: INSTALAR DEPENDÊNCIAS

```bash
pip install -r requirements.txt
```

Isso vai instalar:
- `google-cloud-speech` - Transcrição de áudio
- `pydub` - Processamento de áudio

---

## 📱 PASSO 4: TESTAR

### 4.1 Rodar o bot
```bash
python whatsapp_bot.py
```

### 4.2 Enviar áudio de voz
1. Abra WhatsApp
2. Envie uma **mensagem de voz** para o bot
3. Diga algo como: "Oi Cauãzinho, resumo do mercado"

### 4.3 Resposta esperada
```
📊 RESUMO DO MERCADO DE HOJE

📰 Notícias analisadas: 45
📈 Positivas: 18 (40%)
📉 Negativas: 15 (33%)

🟢 Sinais de COMPRA: 3
🔴 Sinais de VENDA: 2
```

---

## 🎤 COMANDOS DE VOZ

Você pode dizer:

| Comando | Resultado |
|---------|-----------|
| "Oi Cauãzinho" | Menu |
| "Resumo do mercado" | Resumo |
| "Quais ações comprar?" | Recomendações de compra |
| "Quais ações vender?" | Recomendações de venda |
| "Quais são as notícias?" | Top notícias |
| "Como funciona?" | Ajuda |

---

## 🔄 COMO FUNCIONA INTERNAMENTE

### Fluxo de Processamento:

```
1. Usuário envia áudio 🎤
   ↓
2. Twilio recebe e envia URL
   ↓
3. Bot baixa o áudio
   ↓
4. Converte para WAV
   ↓
5. Envia para Google Speech-to-Text
   ↓
6. Google retorna texto transcrito
   ↓
7. Bot processa o comando
   ↓
8. Bot responde com análise
```

---

## 🛠️ TROUBLESHOOTING

### ❌ Erro: "ModuleNotFoundError: No module named 'google.cloud'"
```bash
pip install google-cloud-speech
```

### ❌ Erro: "GOOGLE_SPEECH_API_KEY not found"
- Verifique se configurou em `.env`
- Verifique se a chave está correta

### ❌ Áudio não é transcrito
- Verifique se a chave Google está ativa
- Verifique se a API está habilitada
- Verifique os logs

### ❌ Erro: "Invalid API key"
- Regenere a chave no Google Cloud
- Verifique se copiou corretamente

### ❌ Transcrição retorna vazio
- Áudio pode estar muito baixo
- Áudio pode estar corrompido
- Idioma pode estar diferente

---

## 💡 FALLBACK AUTOMÁTICO

Se a transcrição falhar, o bot:

1. Tenta reconhecer padrões de áudio
2. Se falhar, usa comando padrão: `resumo`
3. Responde com o resumo do mercado

Assim o bot **nunca fica mudo**! 🤖

---

## 🎯 EXEMPLO COMPLETO

### Conversa de voz:

```
👤 Usuário: 🎤 [Envia áudio]
            "Oi Cauãzinho, o que você recomenda hoje?"

🤖 Bot: 🎤 [Transcreve]
        "oi cauãzinho o que você recomenda hoje"
        
        [Reconhece comando: resumo]
        
        [Responde:]
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

👤 Usuário: 🎤 [Envia áudio]
            "Quais ações devo comprar?"

🤖 Bot: 🎤 [Transcreve]
        "quais ações devo comprar"
        
        [Reconhece comando: compra]
        
        [Responde:]
        🟢 RECOMENDAÇÕES DE COMPRA
        
        1. PETR4 - Petrobras
        📈 Score: +0.75
        💪 Confiança: 80%
        📌 Por quê:
           • Petrobras se beneficia de preços altos de petróleo
           • Dólar em alta favorece exportadores
```

---

## 📊 LINGUAGENS SUPORTADAS

Por padrão, o bot transcreve em **Português Brasileiro** (`pt-BR`).

Para mudar, edite `audio_transcriber.py`:

```python
"languageCode": "pt-BR",  # Português Brasil
# ou
"languageCode": "en-US",  # Inglês
# ou
"languageCode": "es-ES",  # Espanhol
```

---

## 💰 MONETIZAR COM VOZ

Agora você pode vender:

1. **Assinatura com Voz**
   - R$ 149/mês (com transcrição de voz)
   - R$ 99/mês (sem transcrição)

2. **Premium Voice**
   - R$ 299/mês
   - Análises em tempo real via voz
   - Alertas por voz

3. **B2B Voice**
   - Integrar em corretoras
   - Traders usam voz para análises

---

## ✅ CHECKLIST

- [ ] Criei projeto Google Cloud
- [ ] Ativei Speech-to-Text API
- [ ] Obtive chave JSON
- [ ] Configurei .env
- [ ] Instalei dependências
- [ ] Testei com áudio de voz
- [ ] Bot responde corretamente

---

## 🎉 PRONTO!

Seu bot agora:

✅ Recebe **mensagens de texto**
✅ Recebe **mensagens de voz**
✅ Transcreve áudio
✅ Processa comandos
✅ Responde com análises

**Você tem um BOT PROFISSIONAL DE VOZ!** 🎤🤖💰

---

## 📚 PRÓXIMAS MELHORIAS

- [ ] Responder com áudio (text-to-speech)
- [ ] Reconhecimento de voz melhorado
- [ ] Suporte a múltiplos idiomas
- [ ] Análise de tom de voz
- [ ] Histórico de conversas de voz

---

**Boa sorte!** 🚀🎤📈
