"""
CAUÃZINHO - Agente Financeiro Inteligente
Orquestra a análise completa do mercado financeiro
"""

import logging
from datetime import datetime
from data_collector import DataCollector
from news_collector import NewsCollector
from sentiment_analyzer import SentimentAnalyzer
from macro_analyzer import MacroAnalyzer
from report_generator import ReportGenerator

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CauazinhoAgent:
    """Agente Financeiro Cauãzinho - Análise Completa do Mercado"""
    
    def __init__(self):
        logger.info("🤖 Inicializando Cauãzinho...")
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
    
    def coletar_dados(self):
        """Etapa 1: Coleta de dados do mercado"""
        logger.info("\n" + "="*80)
        logger.info("ETAPA 1: COLETA DE DADOS DO MERCADO")
        logger.info("="*80)
        
        self.dados_mercado = self.data_collector.coletar_tudo()
        self.data_collector.gerar_resumo_mercado()
    
    def coletar_noticias(self):
        """Etapa 2: Coleta de notícias"""
        logger.info("\n" + "="*80)
        logger.info("ETAPA 2: COLETA DE NOTÍCIAS")
        logger.info("="*80)
        
        self.noticias = self.news_collector.coletar_tudo()
        self.news_collector.exibir_noticias(limite=5)
    
    def analisar_sentimento(self):
        """Etapa 3: Análise de sentimento"""
        logger.info("\n" + "="*80)
        logger.info("ETAPA 3: ANÁLISE DE SENTIMENTO")
        logger.info("="*80)
        
        self.noticias_analisadas = self.sentiment_analyzer.analisar_lote(self.noticias)
        self.sentiment_analyzer.gerar_relatorio_sentimento()
    
    def analisar_macro(self):
        """Etapa 4: Análise macroeconômica"""
        logger.info("\n" + "="*80)
        logger.info("ETAPA 4: ANÁLISE MACROECONÔMICA")
        logger.info("="*80)
        
        # Detecta temas
        self.temas_detectados = self.macro_analyzer.detectar_temas_noticias(
            self.noticias_analisadas
        )
        
        # Analisa impacto
        self.impactos_por_empresa = self.macro_analyzer.analisar_impacto_empresas(
            self.temas_detectados
        )
        
        # Gera relatório macro
        self.macro_analyzer.gerar_relatorio_macro()
        
        # Obtém top recomendações
        self.recomendacoes_top = self.macro_analyzer.obter_recomendacoes_top(limite=5)
    
    def gerar_relatorio(self):
        """Etapa 5: Geração de relatório executivo"""
        logger.info("\n" + "="*80)
        logger.info("ETAPA 5: GERAÇÃO DE RELATÓRIO EXECUTIVO")
        logger.info("="*80)
        
        relatorio = self.report_generator.gerar_relatorio_completo(
            self.dados_mercado,
            self.noticias_analisadas,
            self.temas_detectados,
            self.impactos_por_empresa,
            self.recomendacoes_top
        )
        
        # Exibe relatório
        self.report_generator.exibir_relatorio()
        
        # Salva relatório
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"relatorio_cauazinho_{timestamp}.txt"
        self.report_generator.salvar_relatorio(nome_arquivo)
    
    def executar(self):
        """Executa o agente completo"""
        try:
            logger.info("\n")
            logger.info("╔" + "="*78 + "╗")
            logger.info("║" + " "*78 + "║")
            logger.info("║" + "🤖 BEM-VINDO AO CAUÃZINHO - AGENTE FINANCEIRO INTELIGENTE 🤖".center(78) + "║")
            logger.info("║" + " "*78 + "║")
            logger.info("╚" + "="*78 + "╝")
            
            # Executa todas as etapas
            self.coletar_dados()
            self.coletar_noticias()
            self.analisar_sentimento()
            self.analisar_macro()
            self.gerar_relatorio()
            
            logger.info("\n" + "="*80)
            logger.info("✅ ANÁLISE CONCLUÍDA COM SUCESSO!")
            logger.info("="*80)
            
        except Exception as e:
            logger.error(f"\n❌ ERRO DURANTE EXECUÇÃO: {e}")
            import traceback
            traceback.print_exc()


def main():
    """Função principal"""
    
    # Cria e executa o agente
    agente = CauazinhoAgent()
    agente.executar()
    
    # Menu de opções
    while True:
        print("\n" + "="*80)
        print("MENU DE OPÇÕES")
        print("="*80)
        print("1. Executar análise completa novamente")
        print("2. Exibir relatório atual")
        print("3. Exibir recomendações de compra")
        print("4. Exibir recomendações de venda")
        print("5. Exibir análise de sentimento")
        print("6. Sair")
        print("="*80)
        
        opcao = input("\nEscolha uma opção (1-6): ").strip()
        
        if opcao == "1":
            print("\n🔄 Executando análise completa...")
            agente = CauazinhoAgent()
            agente.executar()
        
        elif opcao == "2":
            print("\n📄 Exibindo relatório atual...")
            agente.report_generator.exibir_relatorio()
        
        elif opcao == "3":
            print("\n🟢 RECOMENDAÇÕES DE COMPRA:")
            print("-" * 80)
            for ticker, dados in agente.recomendacoes_top.get("compras", []):
                print(f"\n{ticker}")
                print(f"  Score: {dados['score_total']:+.2f}")
                print(f"  Confiança: {dados['confianca']:.0%}")
        
        elif opcao == "4":
            print("\n🔴 RECOMENDAÇÕES DE VENDA:")
            print("-" * 80)
            for ticker, dados in agente.recomendacoes_top.get("vendas", []):
                print(f"\n{ticker}")
                print(f"  Score: {dados['score_total']:+.2f}")
                print(f"  Confiança: {dados['confianca']:.0%}")
        
        elif opcao == "5":
            print("\n🧠 ANÁLISE DE SENTIMENTO:")
            print("-" * 80)
            agente.sentiment_analyzer.gerar_relatorio_sentimento()
        
        elif opcao == "6":
            print("\n👋 Encerrando Cauãzinho. Até logo!")
            break
        
        else:
            print("\n❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
