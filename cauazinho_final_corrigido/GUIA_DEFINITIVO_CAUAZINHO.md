# 🤖 Cauãzinho v2 - Guia de Instalação Definitivo

Este guia contém os passos exatos para colocar o seu agente de investimentos no ar usando **Groq (IA)**, **Twilio (WhatsApp)** e **Railway (Hospedagem)**.

---

## 🚀 Passo 1: Preparar o GitHub

1.  Crie um novo repositório **Privado** no seu GitHub chamado `cauazinho-bot`.
2.  Suba todos os arquivos da pasta `cauazinho_agent` que estão no ZIP que te enviei.
3.  Certifique-se de que os nomes dos arquivos estão **EXATAMENTE** assim (em inglês):
    *   `whatsapp_bot.py`
    *   `groq_agent.py`
    *   `requirements.txt`
    *   `Procfile`
    *   `config.py`

---

## 🛠️ Passo 2: Configurar o Railway

1.  No [Railway](https://railway.app/), clique em **"New Project"** -> **"Deploy from GitHub repo"**.
2.  Selecione o seu repositório `cauazinho-bot`.
3.  Vá na aba **"Variables"** e adicione estas chaves (Copie e cole os nomes em MAIÚSCULO):

| Nome da Variável | Valor (Onde conseguir) |
| :--- | :--- |
| **`GROQ_API_KEY`** | [console.groq.com/keys](https://console.groq.com/keys) |
| **`TWILIO_ACCOUNT_SID`** | [console.twilio.com](https://console.twilio.com) |
| **`TWILIO_AUTH_TOKEN`** | [console.twilio.com](https://console.twilio.com) |
| **`TWILIO_PHONE`** | Seu número do Twilio (ex: `whatsapp:+14155238886`) |
| **`NEWS_API_KEY`** | [newsapi.org](https://newsapi.org) |
| **`GROQ_MODEL`** | `llama-3.3-70b-versatile` |

---

## 📱 Passo 3: Conectar o WhatsApp

1.  No Railway, após o deploy ficar **VERDE**, copie a URL pública (ex: `https://web-production-xxxx.up.railway.app`).
2.  Vá no painel do **Twilio** -> **Messaging** -> **Settings** -> **WhatsApp Sandbox Settings**.
3.  No campo **"WHEN A MESSAGE COMES IN"**, cole a sua URL e adicione **`/webhook`** no final.
    *   Exemplo: `https://web-production-xxxx.up.railway.app/webhook`
4.  Clique em **SAVE**.
5.  No seu WhatsApp, mande a mensagem de ativação (ex: `join talk-material`) para o número do Twilio.

---

## 🎮 Comandos do Cauãzinho

*   **`menu`**: Mostra todas as opções.
*   **`analise`**: Faz uma análise profunda de geopolítica e mercado usando a IA do Groq.
*   **`compra`**: Recomendações de compra baseadas em notícias e dados.
*   **`venda`**: Recomendações de venda/evitar.
*   **`noticias`**: Resumo das notícias globais que impactam a bolsa.
*   **Pergunta Livre**: Pergunte qualquer coisa como "O que você acha da Petrobras hoje?" e ele responderá usando IA.

---

### ⚠️ Dicas de Erros Comuns:
*   **Erro Interno?** Verifique os "Logs" no Railway. Geralmente é uma chave de API faltando.
*   **Não responde?** Verifique se a URL no Twilio termina com `/webhook`.
*   **Porta 5000?** Não se preocupe, o código já está ajustado para o Railway ignorar a 5000 e usar a porta correta automaticamente.
