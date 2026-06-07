# =============================================================
# MISSION CONTROL AI — MISSÃO ORION
# FIAP • GS 2026.1 • Turma 1CCPY • Grupo 05
# =============================================================
# Integrantes:
#   Arthur dos Santos Bezerra  — RM 569721
#   Carlos Henrique Fratezi    — RM 571792
#   Felipe Gouveia Braga       — RM 568956
# =============================================================

# ------------------------------------------------------------------
# DADOS DA MISSÃO
# ------------------------------------------------------------------

NOME_MISSAO = "Missão ORION"
NOME_EQUIPE  = "Grupo 05 — 1CCPY"

# Matriz principal: cada linha é um ciclo da missão
# Colunas: [temperatura(°C), comunicacao(%), bateria(%), oxigenio(%), estabilidade(%)]
#
# Narrativa dos ciclos:
#   Ciclo 1 — Lançamento e estabilização inicial
#   Ciclo 2 — Cruzeiro estável em órbita baixa
#   Ciclo 3 — Início de interferência solar (temp sobe, comm cai)
#   Ciclo 4 — Tempestade magnética: bateria e estabilidade caem
#   Ciclo 5 — Pico de crise: todos os sistemas comprometidos
#   Ciclo 6 — Protocolo de recuperação ativado
#   Ciclo 7 — Estabilização parcial — sistemas em recomposição
#   Ciclo 8 — Retorno a condições operacionais aceitáveis

dados_missao = [
    [22, 95, 91, 97, 93],   # Ciclo 1
    [25, 88, 84, 95, 89],   # Ciclo 2
    [30, 71, 75, 92, 78],   # Ciclo 3
    [34, 48, 44, 88, 61],   # Ciclo 4
    [40, 25, 17, 76, 32],   # Ciclo 5
    [37, 38, 28, 80, 45],   # Ciclo 6
    [33, 57, 41, 84, 58],   # Ciclo 7
    [28, 74, 63, 90, 72],   # Ciclo 8
]

# Lista de áreas monitoradas (mesma ordem das colunas)
areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional",
]


# =============================================================
# FUNÇÕES DE ANÁLISE — uma por sensor
# =============================================================

def analisar_temperatura(valor):
    """
    Retorna (classificacao, descricao, pontuacao).
    Regras:
      < 18 °C        → ATENÇÃO
      18–30 °C       → NORMAL
      > 30 até 35 °C → ATENÇÃO
      > 35 °C        → CRÍTICO
    """
    if valor < 18:
        return "ATENÇÃO", "Temperatura muito baixa — risco de falha térmica", 1
    elif valor <= 30:
        return "NORMAL", "Temperatura estável", 0
    elif valor <= 35:
        return "ATENÇÃO", "Temperatura elevada", 1
    else:
        return "CRÍTICO", "Risco de superaquecimento", 2


def analisar_comunicacao(valor):
    """
    Regras:
      < 30%  → CRÍTICO
      30–59% → ATENÇÃO
      ≥ 60%  → NORMAL
    """
    if valor < 30:
        return "CRÍTICO", "Comunicação com a base em nível crítico", 2
    elif valor < 60:
        return "ATENÇÃO", "Comunicação instável", 1
    else:
        return "NORMAL", "Comunicação estável", 0


def analisar_bateria(valor):
    """
    Regras:
      < 20%  → CRÍTICO
      20–49% → ATENÇÃO
      ≥ 50%  → NORMAL
    """
    if valor < 20:
        return "CRÍTICO", "Bateria em nível crítico", 2
    elif valor < 50:
        return "ATENÇÃO", "Bateria abaixo do recomendado", 1
    else:
        return "NORMAL", "Energia estável", 0


def analisar_oxigenio(valor):
    """
    Regras:
      < 80%  → CRÍTICO
      80–89% → ATENÇÃO
      ≥ 90%  → NORMAL
    """
    if valor < 80:
        return "CRÍTICO", "Oxigênio em nível crítico", 2
    elif valor < 90:
        return "ATENÇÃO", "Oxigênio abaixo do ideal", 1
    else:
        return "NORMAL", "Oxigênio adequado", 0


def analisar_estabilidade(valor):
    """
    Regras:
      < 40%  → CRÍTICO
      40–69% → ATENÇÃO
      ≥ 70%  → NORMAL
    """
    if valor < 40:
        return "CRÍTICO", "Estabilidade operacional crítica", 2
    elif valor < 70:
        return "ATENÇÃO", "Estabilidade operacional reduzida", 1
    else:
        return "NORMAL", "Estabilidade operacional adequada", 0


# =============================================================
# FUNÇÃO: calcular risco de um ciclo
# =============================================================

def calcular_risco_ciclo(ciclo):
    """
    Recebe uma lista [temp, comm, bat, ox, estab].
    Retorna (pontuacao_total, lista_de_resultados).
    Cada resultado é (classificacao, descricao, pontos).
    """
    temp, comm, bat, ox, estab = ciclo
    resultados = [
        analisar_temperatura(temp),
        analisar_comunicacao(comm),
        analisar_bateria(bat),
        analisar_oxigenio(ox),
        analisar_estabilidade(estab),
    ]
    pontuacao = sum(r[2] for r in resultados)
    return pontuacao, resultados


# =============================================================
# FUNÇÃO: classificar ciclo
# =============================================================

def classificar_ciclo(pontuacao):
    """
    0–2  → MISSÃO ESTÁVEL
    3–5  → MISSÃO EM ATENÇÃO
    6–10 → MISSÃO CRÍTICA
    """
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


# =============================================================
# FUNÇÃO: gerar recomendação automática para um ciclo
# =============================================================

def gerar_recomendacao(resultados):
    """
    Analisa os resultados e monta recomendações baseadas nos
    itens críticos. Se tudo normal, orienta manutenção padrão.
    """
    recomendacoes = []

    classificacoes = [r[0] for r in resultados]

    if classificacoes[0] == "CRÍTICO":
        recomendacoes.append("verificar controle térmico da cápsula")
    if classificacoes[1] == "CRÍTICO":
        recomendacoes.append("tentar restabelecer contato com a base")
    if classificacoes[2] == "CRÍTICO":
        recomendacoes.append("ativar modo de economia de energia")
    if classificacoes[3] == "CRÍTICO":
        recomendacoes.append("acionar protocolo de suporte à vida")
    if classificacoes[4] == "CRÍTICO":
        recomendacoes.append("reduzir operações não essenciais")

    # Sem críticos — verificar atenções
    if not recomendacoes:
        tem_atencao = any(c == "ATENÇÃO" for c in classificacoes)
        if tem_atencao:
            recomendacoes.append("monitorar sistemas em atenção e preparar plano de contingência")
        else:
            recomendacoes.append("manter operação normal e continuar monitoramento")

    return "Recomendação: " + "; ".join(recomendacoes).capitalize() + "."


# =============================================================
# FUNÇÃO: analisar tendência da missão
# =============================================================

def analisar_tendencia(riscos):
    """
    Compara risco do primeiro e do último ciclo.
    Retorna string descritiva da tendência.
    """
    primeiro = riscos[0]
    ultimo   = riscos[-1]

    if ultimo > primeiro:
        return "A missão apresentou tendência de PIORA."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de MELHORA."
    else:
        return "A missão permaneceu ESTÁVEL em relação ao início."


# =============================================================
# FUNÇÃO: identificar área mais afetada
# =============================================================

def identificar_area_mais_afetada(dados_missao, areas_monitoradas):
    """
    Soma a pontuação de risco de cada coluna ao longo de todos
    os ciclos e retorna (nome_da_area, pontuacao, lista_pontos).
    """
    num_areas = len(areas_monitoradas)
    pontos_por_area = [0] * num_areas

    analisadores = [
        analisar_temperatura,
        analisar_comunicacao,
        analisar_bateria,
        analisar_oxigenio,
        analisar_estabilidade,
    ]

    for ciclo in dados_missao:
        for i in range(num_areas):
            _, _, pts = analisadores[i](ciclo[i])
            pontos_por_area[i] += pts

    idx_max = pontos_por_area.index(max(pontos_por_area))
    return areas_monitoradas[idx_max], pontos_por_area[idx_max], pontos_por_area


# =============================================================
# FUNÇÃO: exibir análise de cada ciclo (loop principal)
# =============================================================

def exibir_ciclos(dados_missao):
    """
    Percorre todos os ciclos, exibe análise detalhada e
    retorna lista de pontuações para uso no relatório final.
    """
    riscos = []

    for i, ciclo in enumerate(dados_missao):
        numero_ciclo = i + 1
        temp, comm, bat, ox, estab = ciclo

        pontuacao, resultados = calcular_risco_ciclo(ciclo)
        classificacao = classificar_ciclo(pontuacao)
        recomendacao  = gerar_recomendacao(resultados)

        riscos.append(pontuacao)

        print(f"\nCICLO {numero_ciclo}")
        print("-" * 60)
        print(f"  Temperatura : {temp} °C  | {resultados[0][0]:8} | {resultados[0][1]}")
        print(f"  Comunicação : {comm}%    | {resultados[1][0]:8} | {resultados[1][1]}")
        print(f"  Bateria     : {bat}%     | {resultados[2][0]:8} | {resultados[2][1]}")
        print(f"  Oxigênio    : {ox}%      | {resultados[3][0]:8} | {resultados[3][1]}")
        print(f"  Estabilidade: {estab}%   | {resultados[4][0]:8} | {resultados[4][1]}")
        print()
        print(f"  Pontuação de risco  : {pontuacao}")
        print(f"  Classificação       : {classificacao}")
        print(f"  {recomendacao}")

    return riscos


# =============================================================
# FUNÇÃO: relatório final da missão
# =============================================================

def gerar_relatorio_final(dados_missao, areas_monitoradas, riscos):
    """
    Calcula estatísticas gerais e exibe o relatório final.
    """
    num_ciclos = len(dados_missao)

    # Médias por coluna
    media_temp  = sum(c[0] for c in dados_missao) / num_ciclos
    media_comm  = sum(c[1] for c in dados_missao) / num_ciclos
    media_bat   = sum(c[2] for c in dados_missao) / num_ciclos
    media_ox    = sum(c[3] for c in dados_missao) / num_ciclos
    media_estab = sum(c[4] for c in dados_missao) / num_ciclos

    # Ciclo mais crítico
    idx_critico     = riscos.index(max(riscos))
    ciclo_critico   = idx_critico + 1
    risco_max       = riscos[idx_critico]
    risco_medio     = sum(riscos) / num_ciclos
    qtd_criticos    = sum(1 for r in riscos if r >= 6)

    # Tendência
    tendencia = analisar_tendencia(riscos)

    # Área mais afetada
    area_max, pts_max, pontos_por_area = identificar_area_mais_afetada(
        dados_missao, areas_monitoradas
    )

    # Classificação final (baseada no risco médio arredondado)
    classificacao_final = classificar_ciclo(round(risco_medio))

    # ------ Exibição ------
    print()
    print("=" * 60)
    print("  RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"  Missão  : {NOME_MISSAO}")
    print(f"  Equipe  : {NOME_EQUIPE}")
    print(f"  Ciclos analisados : {num_ciclos}")
    print()
    print(f"  Média de temperatura   : {media_temp:.2f} °C")
    print(f"  Média de comunicação   : {media_comm:.2f}%")
    print(f"  Média de bateria       : {media_bat:.2f}%")
    print(f"  Média de oxigênio      : {media_ox:.2f}%")
    print(f"  Média de estabilidade  : {media_estab:.2f}%")
    print()
    print(f"  Ciclo mais crítico     : Ciclo {ciclo_critico}")
    print(f"  Maior pontuação de risco : {risco_max}")
    print(f"  Risco médio da missão  : {risco_medio:.2f}")
    print(f"  Ciclos em estado crítico : {qtd_criticos}")
    print()
    print(f"  Tendência da missão:")
    print(f"    {tendencia}")
    print()
    print("  Pontuação acumulada por área:")
    for area, pts in zip(areas_monitoradas, pontos_por_area):
        print(f"    {area}: {pts} ponto(s)")
    print()
    print(f"  Área mais afetada      : {area_max} ({pts_max} ponto(s))")
    print()
    print(f"  Classificação final    : {classificacao_final}")
    print()
    print("  Conclusão:")
    if classificacao_final == "MISSÃO CRÍTICA":
        print("    A missão ORION enfrentou falhas severas em múltiplos sistemas.")
        print("    É necessária intervenção imediata e ativação do protocolo de emergência.")
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        print("    A missão ORION apresentou instabilidade relevante durante a operação.")
        print("    Apesar da tentativa de recuperação, sistemas ainda exigem atenção.")
        print("    A equipe deve manter o plano de contingência ativo.")
    else:
        print("    A missão ORION operou dentro dos parâmetros esperados.")
        print("    Todos os sistemas mantiveram condições aceitáveis ao longo dos ciclos.")
    print("=" * 60)


# =============================================================
# EXECUÇÃO PRINCIPAL
# =============================================================

def main():
    print()
    print("=" * 60)
    print("  MISSION CONTROL AI")
    print("=" * 60)
    print(f"  Missão  : {NOME_MISSAO}")
    print(f"  Equipe  : {NOME_EQUIPE}")
    print(f"  Ciclos  : {len(dados_missao)}")
    print("=" * 60)

    riscos = exibir_ciclos(dados_missao)
    gerar_relatorio_final(dados_missao, areas_monitoradas, riscos)


if __name__ == "__main__":
    main()
