"""
Módulo de Geração de Relatórios
Gera relatórios executivos com recomendações
"""

import logging
from datetime import datetime
from config import EMPRESAS_B3_PRINCIPAIS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ReportGenerator:
    """Gerador de relatórios executivos"""
    
    def __init__(self):
        self.relatorio = ""
    
    def gerar_relatorio_completo(self, dados_mercado, noticias_analisadas, 
                                 temas_detectados, impactos_por_empresa, 
                                 recomendacoes_top):
        """Gera relatório completo do agente Cauãzinho"""
        
        self.relatorio = ""
        
        # Cabeçalho
        self.relatorio += self._gerar_cabecalho()
        
        # Resumo executivo
        self.relatorio += self._gerar_resumo_executivo(
            noticias_analisadas, temas_detectados, impactos_por_empresa
        )
        
        # Estado do mercado
        self.relatorio += self._gerar_estado_mercado(dados_mercado)
        
        # Análise de sentimento
        self.relatorio += self._gerar_analise_sentimento(noticias_analisadas)
        
        # Temas macroeconômicos
        self.relatorio += self._gerar_temas_macro(temas_detectados)
        
        # Recomendações de compra
        self.relatorio += self._gerar_recomendacoes_compra(recomendacoes_top, impactos_por_empresa)
        
        # Recomendações de venda
        self.relatorio += self._gerar_recomendacoes_venda(recomendacoes_top, impactos_por_empresa)
        
        # Riscos e oportunidades
        self.relatorio += self._gerar_riscos_oportunidades(temas_detectados)
        
        # Rodapé
        self.relatorio += self._gerar_rodape()
        
        return self.relatorio
    
    def _gerar_cabecalho(self):
        """Gera cabeçalho do relatório"""
        data_hora = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        
        texto = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                    🤖 AGENTE FINANCEIRO CAUÃZINHO 🤖                        ║
║                                                                              ║
║                      RELATÓRIO DE ANÁLISE DE MERCADO                         ║
║                                                                              ║
║                          {data_hora}                              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

"""
        return texto
    
    def _gerar_resumo_executivo(self, noticias_analisadas, temas_detectados, impactos_por_empresa):
        """Gera resumo executivo"""
        
        # Conta sentimentos
        positivas = sum(1 for n in noticias_analisadas if n["sentimento"] == "POSITIVO")
        negativas = sum(1 for n in noticias_analisadas if n["sentimento"] == "NEGATIVO")
        neutras = sum(1 for n in noticias_analisadas if n["sentimento"] == "NEUTRO")
        total = len(noticias_analisadas)
        
        # Conta recomendações
        compras = sum(1 for d in impactos_por_empresa.values() if d["recomendacao"] == "COMPRA")
        vendas = sum(1 for d in impactos_por_empresa.values() if d["recomendacao"] == "VENDA")
        
        # Temas com mais impacto
        temas_ativos = {t: d for t, d in temas_detectados.items() if d["positivas"] + d["negativas"] > 0}
        
        texto = f"""
📋 RESUMO EXECUTIVO
{'─' * 80}

📊 Análise de Notícias:
   • Total de notícias analisadas: {total}
   • Sentimento positivo: {positivas} ({positivas/total*100:.1f}%)
   • Sentimento negativo: {negativas} ({negativas/total*100:.1f}%)
   • Sentimento neutro: {neutras} ({neutras/total*100:.1f}%)

💡 Recomendações Geradas:
   • Sinais de COMPRA: {compras}
   • Sinais de VENDA: {vendas}
   • Sem sinal claro: {len(impactos_por_empresa) - compras - vendas}

🌍 Temas Macroeconômicos Detectados: {len(temas_ativos)}
   • Temas ativos: {', '.join(temas_ativos.keys())}

"""
        return texto
    
    def _gerar_estado_mercado(self, dados_mercado):
        """Gera seção de estado do mercado"""
        
        texto = f"""
📈 ESTADO ATUAL DO MERCADO
{'─' * 80}

🌍 Índices Globais:
"""
        
        if dados_mercado.get("indices"):
            for nome, dados in dados_mercado["indices"].items():
                variacao = dados["variacao_30d"]
                emoji = "📈" if variacao > 0 else "📉" if variacao < 0 else "➡️"
                texto += f"   {emoji} {nome}: {dados['preco']:.2f} ({variacao:+.2f}%)\n"
        
        texto += f"\n💱 Moedas Principais:\n"
        
        if dados_mercado.get("moedas"):
            for ticker, dados in dados_mercado["moedas"].items():
                variacao = dados["variacao_30d"]
                emoji = "📈" if variacao > 0 else "📉" if variacao < 0 else "➡️"
                descricao = dados["descricao"]
                texto += f"   {emoji} {descricao}: {dados['preco']:.4f} ({variacao:+.2f}%)\n"
        
        texto += f"\n⛽ Commodities Principais:\n"
        
        if dados_mercado.get("commodities"):
            for ticker, dados in dados_mercado["commodities"].items():
                variacao = dados["variacao_30d"]
                emoji = "📈" if variacao > 0 else "📉" if variacao < 0 else "➡️"
                descricao = dados["descricao"]
                texto += f"   {emoji} {descricao}: {dados['preco']:.2f} ({variacao:+.2f}%)\n"
        
        texto += "\n"
        return texto
    
    def _gerar_analise_sentimento(self, noticias_analisadas):
        """Gera análise de sentimento"""
        
        # Top notícias positivas
        top_positivas = sorted(
            [n for n in noticias_analisadas if n["sentimento"] == "POSITIVO"],
            key=lambda x: x["confianca"],
            reverse=True
        )[:3]
        
        # Top notícias negativas
        top_negativas = sorted(
            [n for n in noticias_analisadas if n["sentimento"] == "NEGATIVO"],
            key=lambda x: x["confianca"],
            reverse=True
        )[:3]
        
        texto = f"""
🧠 ANÁLISE DE SENTIMENTO
{'─' * 80}

✅ Top 3 Notícias POSITIVAS:
"""
        
        for i, noticia in enumerate(top_positivas, 1):
            texto += f"\n   {i}. {noticia['noticia'][:70]}\n"
            texto += f"      Fonte: {noticia['fonte']}\n"
            texto += f"      Confiança: {noticia['confianca']:.0%}\n"
        
        texto += f"\n❌ Top 3 Notícias NEGATIVAS:\n"
        
        for i, noticia in enumerate(top_negativas, 1):
            texto += f"\n   {i}. {noticia['noticia'][:70]}\n"
            texto += f"      Fonte: {noticia['fonte']}\n"
            texto += f"      Confiança: {noticia['confianca']:.0%}\n"
        
        texto += "\n"
        return texto
    
    def _gerar_temas_macro(self, temas_detectados):
        """Gera análise de temas macroeconômicos"""
        
        texto = f"""
🌍 TEMAS MACROECONÔMICOS
{'─' * 80}

"""
        
        for tema, dados in temas_detectados.items():
            total = dados["positivas"] + dados["negativas"]
            if total > 0:
                sentimento = "POSITIVO" if dados["positivas"] > dados["negativas"] else "NEGATIVO"
                emoji = "📈" if sentimento == "POSITIVO" else "📉"
                
                texto += f"{emoji} {tema.upper()}\n"
                texto += f"   Notícias positivas: {dados['positivas']}\n"
                texto += f"   Notícias negativas: {dados['negativas']}\n"
                
                if dados["noticias"]:
                    texto += f"   Principais notícias:\n"
                    for noticia in dados["noticias"][:2]:
                        texto += f"      • {noticia[:60]}...\n"
                texto += "\n"
        
        return texto
    
    def _gerar_recomendacoes_compra(self, recomendacoes_top, impactos_por_empresa):
        """Gera recomendações de compra"""
        
        texto = f"""
🟢 RECOMENDAÇÕES DE COMPRA
{'─' * 80}

"""
        
        if recomendacoes_top["compras"]:
            for ticker, dados in recomendacoes_top["compras"]:
                empresa = EMPRESAS_B3_PRINCIPAIS.get(ticker, {})
                
                texto += f"\n🎯 {ticker} - {empresa.get('nome', 'Desconhecida')}\n"
                texto += f"   Setor: {empresa.get('setor', 'N/A')}\n"
                texto += f"   Score de Impacto: {dados['score_total']:+.2f}\n"
                texto += f"   Confiança: {dados['confianca']:.0%}\n"
                texto += f"   Sensível a: {', '.join(empresa.get('sensivel_a', []))}\n"
                
                texto += f"\n   📌 Justificativa:\n"
                for impacto in dados['impactos'][:3]:
                    texto += f"      • {impacto['descricao']}\n"
                    texto += f"        Tema: {impacto['tema']} ({impacto['tipo']})\n"
                    if impacto['noticias']:
                        texto += f"        Notícia: {impacto['noticias'][0][:50]}...\n"
        else:
            texto += "   Nenhuma recomendação de compra no momento.\n"
        
        texto += "\n"
        return texto
    
    def _gerar_recomendacoes_venda(self, recomendacoes_top, impactos_por_empresa):
        """Gera recomendações de venda"""
        
        texto = f"""
🔴 RECOMENDAÇÕES DE VENDA
{'─' * 80}

"""
        
        if recomendacoes_top["vendas"]:
            for ticker, dados in recomendacoes_top["vendas"]:
                empresa = EMPRESAS_B3_PRINCIPAIS.get(ticker, {})
                
                texto += f"\n⚠️ {ticker} - {empresa.get('nome', 'Desconhecida')}\n"
                texto += f"   Setor: {empresa.get('setor', 'N/A')}\n"
                texto += f"   Score de Impacto: {dados['score_total']:+.2f}\n"
                texto += f"   Confiança: {dados['confianca']:.0%}\n"
                texto += f"   Sensível a: {', '.join(empresa.get('sensivel_a', []))}\n"
                
                texto += f"\n   📌 Justificativa:\n"
                for impacto in dados['impactos'][:3]:
                    texto += f"      • {impacto['descricao']}\n"
                    texto += f"        Tema: {impacto['tema']} ({impacto['tipo']})\n"
                    if impacto['noticias']:
                        texto += f"        Notícia: {impacto['noticias'][0][:50]}...\n"
        else:
            texto += "   Nenhuma recomendação de venda no momento.\n"
        
        texto += "\n"
        return texto
    
    def _gerar_riscos_oportunidades(self, temas_detectados):
        """Gera análise de riscos e oportunidades"""
        
        texto = f"""
⚡ RISCOS E OPORTUNIDADES
{'─' * 80}

🎯 Principais Oportunidades:
   • Acompanhar temas com sentimento positivo para identificar entradas
   • Monitorar commodities em alta para setores exportadores
   • Avaliar impacto de decisões governamentais

⚠️ Principais Riscos:
   • Volatilidade causada por notícias geopolíticas
   • Exposição a moeda estrangeira (dólar)
   • Dependência de commodities para empresas exportadoras

"""
        return texto
    
    def _gerar_rodape(self):
        """Gera rodapé do relatório"""
        
        texto = f"""
{'─' * 80}

📌 NOTAS IMPORTANTES:
   • Este relatório é gerado automaticamente e deve ser validado por um analista
   • As recomendações são baseadas em análise de sentimento e correlações macro
   • Sempre considere seu perfil de risco e horizonte de investimento
   • Consulte um consultor financeiro antes de tomar decisões de investimento

⚖️ AVISO LEGAL:
   As informações contidas neste relatório são fornecidas apenas para fins
   educacionais e informativos. Não constituem recomendação de investimento.
   O usuário assume total responsabilidade por suas decisões de investimento.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    Relatório gerado por Cauãzinho                           ║
║                    Agente Financeiro Inteligente                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return texto
    
    def salvar_relatorio(self, nome_arquivo="relatorio_cauazinho.txt"):
        """Salva o relatório em arquivo"""
        try:
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                f.write(self.relatorio)
            logger.info(f"✅ Relatório salvo em: {nome_arquivo}")
        except Exception as e:
            logger.error(f"❌ Erro ao salvar relatório: {e}")
    
    def exibir_relatorio(self):
        """Exibe o relatório no console"""
        print(self.relatorio)


if __name__ == "__main__":
    generator = ReportGenerator()
    # Teste será feito no main.py
