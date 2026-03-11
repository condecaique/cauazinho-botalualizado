"""
CAUÃZINHO - Versão WhatsApp
Agente financeiro com interface amigável para WhatsApp
Usa emojis e formatação simples
"""

import logging
from datetime import datetime
from data_collector import DataCollector
from news_collector import NewsCollector
from sentiment_analyzer import SentimentAnalyzer
from macro_analyzer import MacroAnalyzer
from report_generator import ReportGenerator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CauazinhoWhatsApp:
    """Versão WhatsApp do Cauãzinho com emojis"""
    
    def __init__(self):
        self.data_collector = DataCollector()
        self.news_collector = NewsCollector()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.macro_analyzer = MacroAnalyzer()
        self.report_generator = ReportGenerator()
        
        self.dados_mercado = {}
        self.noticias = []
        self.noticias_analisadas = []
        self.temas_detectados = {}
        self.impactos_por_empresa = {}
        self.recomendacoes_top = {}
    
    def enviar_mensagem(self, texto):
        """Simula envio de mensagem WhatsApp"""
        print(f"\n📱 WhatsApp: {texto}\n")
    
    def executar_completo(self):
        """Executa análise completa com mensagens WhatsApp"""
        
        self.enviar_mensagem("🤖 Oi! Sou o Cauãzinho! 👋")
        self.enviar_mensagem("📊 Vou analisar o mercado para você...")
        self.enviar_mensagem("⏳ Isso pode levar 1-2 minutos. Aguarde! ⏳")
        
        try:
            # Etapa 1
            self.enviar_mensagem("📈 Etapa 1/5: Coletando dados das bolsas...")
            self.dados_mercado = self.data_collector.coletar_tudo()
            self.enviar_mensagem("✅ Dados coletados com sucesso!")
            
            # Etapa 2
            self.enviar_mensagem("📰 Etapa 2/5: Buscando notícias...")
            self.noticias = self.news_collector.coletar_tudo()
            self.enviar_mensagem(f"✅ {len(self.noticias)} notícias encontradas!")
            
            # Etapa 3
            self.enviar_mensagem("🧠 Etapa 3/5: Analisando sentimento...")
            self.noticias_analisadas = self.sentiment_analyzer.analisar_lote(self.noticias)
            self.enviar_mensagem("✅ Análise de sentimento concluída!")
            
            # Etapa 4
            self.enviar_mensagem("🌍 Etapa 4/5: Detectando temas macroeconômicos...")
            self.temas_detectados = self.macro_analyzer.detectar_temas_noticias(
                self.noticias_analisadas
            )
            self.impactos_por_empresa = self.macro_analyzer.analisar_impacto_empresas(
                self.temas_detectados
            )
            self.recomendacoes_top = self.macro_analyzer.obter_recomendacoes_top(limite=5)
            self.enviar_mensagem("✅ Análise macroeconômica concluída!")
            
            # Etapa 5
            self.enviar_mensagem("📄 Etapa 5/5: Gerando relatório...")
            relatorio = self.report_generator.gerar_relatorio_completo(
                self.dados_mercado,
                self.noticias_analisadas,
                self.temas_detectados,
                self.impactos_por_empresa,
                self.recomendacoes_top
            )
            self.enviar_mensagem("✅ Relatório gerado!")
            
            # Resumo
            self.enviar_resumo()
            
            # Recomendações
            self.enviar_recomendacoes()
            
            self.enviar_mensagem("🎉 Análise completa! Relatório salvo em arquivo.")
            
        except Exception as e:
            self.enviar_mensagem(f"❌ Erro: {e}")
            import traceback
            traceback.print_exc()
    
    def enviar_resumo(self):
        """Envia resumo executivo via WhatsApp"""
        
        positivas = sum(1 for n in self.noticias_analisadas if n["sentimento"] == "POSITIVO")
        negativas = sum(1 for n in self.noticias_analisadas if n["sentimento"] == "NEGATIVO")
        total = len(self.noticias_analisadas)
        
        compras = sum(1 for d in self.impactos_por_empresa.values() if d["recomendacao"] == "COMPRA")
        vendas = sum(1 for d in self.impactos_por_empresa.values() if d["recomendacao"] == "VENDA")
        
        self.enviar_mensagem("=" * 50)
        self.enviar_mensagem("📊 RESUMO DO MERCADO")
        self.enviar_mensagem("=" * 50)
        self.enviar_mensagem(f"\n📈 Notícias Positivas: {positivas} ({positivas/total*100:.0f}%)")
        self.enviar_mensagem(f"📉 Notícias Negativas: {negativas} ({negativas/total*100:.0f}%)")
        self.enviar_mensagem(f"\n🟢 Sinais de COMPRA: {compras}")
        self.enviar_mensagem(f"🔴 Sinais de VENDA: {vendas}")
    
    def enviar_recomendacoes(self):
        """Envia recomendações de compra e venda"""
        
        from config import EMPRESAS_B3_PRINCIPAIS
        
        # Compras
        if self.recomendacoes_top["compras"]:
            self.enviar_mensagem("\n" + "=" * 50)
            self.enviar_mensagem("🟢 RECOMENDAÇÕES DE COMPRA")
            self.enviar_mensagem("=" * 50)
            
            for ticker, dados in self.recomendacoes_top["compras"]:
                empresa = EMPRESAS_B3_PRINCIPAIS.get(ticker, {})
                self.enviar_mensagem(f"\n💰 {ticker} - {empresa.get('nome', 'Desconhecida')}")
                self.enviar_mensagem(f"   Score: {dados['score_total']:+.2f}")
                self.enviar_mensagem(f"   Confiança: {dados['confianca']:.0%}")
                
                if dados['impactos']:
                    self.enviar_mensagem(f"   Razões:")
                    for impacto in dados['impactos'][:2]:
                        self.enviar_mensagem(f"   • {impacto['descricao']}")
        
        # Vendas
        if self.recomendacoes_top["vendas"]:
            self.enviar_mensagem("\n" + "=" * 50)
            self.enviar_mensagem("🔴 RECOMENDAÇÕES DE VENDA")
            self.enviar_mensagem("=" * 50)
            
            for ticker, dados in self.recomendacoes_top["vendas"]:
                empresa = EMPRESAS_B3_PRINCIPAIS.get(ticker, {})
                self.enviar_mensagem(f"\n⚠️ {ticker} - {empresa.get('nome', 'Desconhecida')}")
                self.enviar_mensagem(f"   Score: {dados['score_total']:+.2f}")
                self.enviar_mensagem(f"   Confiança: {dados['confianca']:.0%}")
                
                if dados['impactos']:
                    self.enviar_mensagem(f"   Razões:")
                    for impacto in dados['impactos'][:2]:
                        self.enviar_mensagem(f"   • {impacto['descricao']}")
    
    def menu_interativo(self):
        """Menu interativo para WhatsApp"""
        
        while True:
            self.enviar_mensagem("\n" + "=" * 50)
            self.enviar_mensagem("📱 MENU CAUÃZINHO")
            self.enviar_mensagem("=" * 50)
            self.enviar_mensagem("1️⃣ Executar análise completa")
            self.enviar_mensagem("2️⃣ Ver recomendações de COMPRA 🟢")
            self.enviar_mensagem("3️⃣ Ver recomendações de VENDA 🔴")
            self.enviar_mensagem("4️⃣ Ver análise de sentimento 🧠")
            self.enviar_mensagem("5️⃣ Ver estado do mercado 📊")
            self.enviar_mensagem("6️⃣ Sair 👋")
            self.enviar_mensagem("=" * 50)
            
            opcao = input("\nEscolha uma opção (1-6): ").strip()
            
            if opcao == "1":
                self.executar_completo()
            
            elif opcao == "2":
                self.enviar_recomendacoes_compra()
            
            elif opcao == "3":
                self.enviar_recomendacoes_venda()
            
            elif opcao == "4":
                self.enviar_analise_sentimento()
            
            elif opcao == "5":
                self.enviar_estado_mercado()
            
            elif opcao == "6":
                self.enviar_mensagem("👋 Até logo! Boa sorte nos investimentos! 💰")
                break
            
            else:
                self.enviar_mensagem("❌ Opção inválida. Tente novamente!")
    
    def enviar_recomendacoes_compra(self):
        """Envia apenas recomendações de compra"""
        from config import EMPRESAS_B3_PRINCIPAIS
        
        if not self.recomendacoes_top.get("compras"):
            self.enviar_mensagem("⚠️ Nenhuma recomendação de compra no momento.")
            return
        
        self.enviar_mensagem("\n🟢 RECOMENDAÇÕES DE COMPRA")
        self.enviar_mensagem("=" * 50)
        
        for ticker, dados in self.recomendacoes_top["compras"]:
            empresa = EMPRESAS_B3_PRINCIPAIS.get(ticker, {})
            self.enviar_mensagem(f"\n💰 {ticker}")
            self.enviar_mensagem(f"   Nome: {empresa.get('nome', 'N/A')}")
            self.enviar_mensagem(f"   Score: {dados['score_total']:+.2f}")
            self.enviar_mensagem(f"   Confiança: {dados['confianca']:.0%}")
    
    def enviar_recomendacoes_venda(self):
        """Envia apenas recomendações de venda"""
        from config import EMPRESAS_B3_PRINCIPAIS
        
        if not self.recomendacoes_top.get("vendas"):
            self.enviar_mensagem("⚠️ Nenhuma recomendação de venda no momento.")
            return
        
        self.enviar_mensagem("\n🔴 RECOMENDAÇÕES DE VENDA")
        self.enviar_mensagem("=" * 50)
        
        for ticker, dados in self.recomendacoes_top["vendas"]:
            empresa = EMPRESAS_B3_PRINCIPAIS.get(ticker, {})
            self.enviar_mensagem(f"\n⚠️ {ticker}")
            self.enviar_mensagem(f"   Nome: {empresa.get('nome', 'N/A')}")
            self.enviar_mensagem(f"   Score: {dados['score_total']:+.2f}")
            self.enviar_mensagem(f"   Confiança: {dados['confianca']:.0%}")
    
    def enviar_analise_sentimento(self):
        """Envia análise de sentimento"""
        
        if not self.noticias_analisadas:
            self.enviar_mensagem("⚠️ Nenhuma análise realizada ainda. Execute a análise completa primeiro!")
            return
        
        positivas = sum(1 for n in self.noticias_analisadas if n["sentimento"] == "POSITIVO")
        negativas = sum(1 for n in self.noticias_analisadas if n["sentimento"] == "NEGATIVO")
        neutras = sum(1 for n in self.noticias_analisadas if n["sentimento"] == "NEUTRO")
        total = len(self.noticias_analisadas)
        
        self.enviar_mensagem("\n🧠 ANÁLISE DE SENTIMENTO")
        self.enviar_mensagem("=" * 50)
        self.enviar_mensagem(f"📈 Positivas: {positivas} ({positivas/total*100:.0f}%)")
        self.enviar_mensagem(f"📉 Negativas: {negativas} ({negativas/total*100:.0f}%)")
        self.enviar_mensagem(f"➖ Neutras: {neutras} ({neutras/total*100:.0f}%)")
    
    def enviar_estado_mercado(self):
        """Envia estado atual do mercado"""
        
        if not self.dados_mercado:
            self.enviar_mensagem("⚠️ Nenhum dado de mercado coletado ainda. Execute a análise completa!")
            return
        
        self.enviar_mensagem("\n📊 ESTADO DO MERCADO")
        self.enviar_mensagem("=" * 50)
        
        if self.dados_mercado.get("indices"):
            self.enviar_mensagem("\n🌍 Índices Globais:")
            for nome, dados in self.dados_mercado["indices"].items():
                emoji = "📈" if dados["variacao_30d"] > 0 else "📉"
                self.enviar_mensagem(f"{emoji} {nome}: {dados['variacao_30d']:+.2f}%")
        
        if self.dados_mercado.get("moedas"):
            self.enviar_mensagem("\n💱 Moedas:")
            for ticker, dados in self.dados_mercado["moedas"].items():
                emoji = "📈" if dados["variacao_30d"] > 0 else "📉"
                self.enviar_mensagem(f"{emoji} {dados['descricao']}: {dados['variacao_30d']:+.2f}%")


def main():
    """Função principal"""
    
    print("\n" + "=" * 60)
    print("🤖 BEM-VINDO AO CAUÃZINHO - VERSÃO WHATSAPP 📱".center(60))
    print("=" * 60)
    
    agente = CauazinhoWhatsApp()
    agente.menu_interativo()


if __name__ == "__main__":
    main()
