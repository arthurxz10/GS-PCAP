# 🚀 Mission Control AI — Missão ORION

> **FIAP • GS 2026.1 • Pensamento Computacional e Automação com Python**  
> Turma 1CCPY • Grupo 05

---

## Integrantes

 Nome | RM 
 Arthur dos Santos Bezerra | 569721 |
 Carlos Henrique Fratezi | 571792 |
 Felipe Gouveia Braga | 568956 |

---

## Sobre a Missão ORION

A **Missão ORION** é uma cápsula espacial experimental simulada desenvolvida como eixo narrativo central da Global Solution 2026.1. Este módulo — **Pensamento Computacional e Automação com Python** — implementa o núcleo de monitoramento inteligente da missão: a **Mission Control AI**.

O sistema simula 8 ciclos de operação da cápsula, desde o lançamento estável até uma crise total no Ciclo 5 (tempestade magnética intensa), passando por uma recuperação progressiva até o Ciclo 8.

---

## Estrutura do repositório

```
mission-control-ai/
├── README.md
└── mission_control.py
```

---

## Como executar

Nenhuma biblioteca externa é necessária. Basta ter Python 3 instalado.

```bash
python mission_control.py
```

A saída completa é exibida no terminal: análise ciclo a ciclo + relatório final.

---

## Estrutura de dados

### Matriz `dados_missao`

Lista de listas onde cada linha representa um ciclo e cada coluna um sensor:

```
[temperatura(°C), comunicacao(%), bateria(%), oxigenio(%), estabilidade(%)]
```

| Posição | Sensor | Unidade |
|---|---|---|
| 0 | Temperatura interna | °C |
| 1 | Comunicação com a base | % |
| 2 | Sistema de energia (bateria) | % |
| 3 | Suporte de oxigênio | % |
| 4 | Estabilidade operacional | % |

### Narrativa dos 8 ciclos

| Ciclo | Evento |
|---|---|
| 1 | Lançamento e estabilização inicial |
| 2 | Cruzeiro estável em órbita baixa |
| 3 | Início de interferência solar |
| 4 | Tempestade magnética — degradação dos sistemas |
| 5 | Pico de crise — todos os sistemas comprometidos |
| 6 | Protocolo de recuperação ativado |
| 7 | Estabilização parcial |
| 8 | Retorno a condições operacionais aceitáveis |

---

## Regras de alerta

### Temperatura (°C)

| Condição | Classificação | Pontos |
|---|---|---|
| < 18 °C | ATENÇÃO | 1 |
| 18 – 30 °C | NORMAL | 0 |
| > 30 até 35 °C | ATENÇÃO | 1 |
| > 35 °C | CRÍTICO | 2 |

### Comunicação (%)

| Condição | Classificação | Pontos |
|---|---|---|
| < 30% | CRÍTICO | 2 |
| 30 – 59% | ATENÇÃO | 1 |
| ≥ 60% | NORMAL | 0 |

### Bateria (%)

| Condição | Classificação | Pontos |
|---|---|---|
| < 20% | CRÍTICO | 2 |
| 20 – 49% | ATENÇÃO | 1 |
| ≥ 50% | NORMAL | 0 |

### Oxigênio (%)

| Condição | Classificação | Pontos |
|---|---|---|
| < 80% | CRÍTICO | 2 |
| 80 – 89% | ATENÇÃO | 1 |
| ≥ 90% | NORMAL | 0 |

### Estabilidade (%)

| Condição | Classificação | Pontos |
|---|---|---|
| < 40% | CRÍTICO | 2 |
| 40 – 69% | ATENÇÃO | 1 |
| ≥ 70% | NORMAL | 0 |

---

## Pontuação e classificação dos ciclos

| Pontuação total | Classificação |
|---|---|
| 0 – 2 | MISSÃO ESTÁVEL |
| 3 – 5 | MISSÃO EM ATENÇÃO |
| 6 – 10 | MISSÃO CRÍTICA |

Pontuação máxima por ciclo: **10 pontos** (5 sensores × 2 pontos cada).

---

## Funções implementadas

| Função | Responsabilidade |
|---|---|
| `analisar_temperatura(v)` | Classifica e pontua a temperatura |
| `analisar_comunicacao(v)` | Classifica e pontua a comunicação |
| `analisar_bateria(v)` | Classifica e pontua a bateria |
| `analisar_oxigenio(v)` | Classifica e pontua o oxigênio |
| `analisar_estabilidade(v)` | Classifica e pontua a estabilidade |
| `calcular_risco_ciclo(ciclo)` | Agrega a pontuação total de um ciclo |
| `classificar_ciclo(pontuacao)` | Converte pontuação em status da missão |
| `gerar_recomendacao(resultados)` | Gera recomendações automáticas baseadas nos alertas |
| `analisar_tendencia(riscos)` | Compara primeiro e último ciclo |
| `identificar_area_mais_afetada(...)` | Soma pontos por área ao longo de todos os ciclos |
| `exibir_ciclos(dados_missao)` | Loop principal — exibe análise de cada ciclo |
| `gerar_relatorio_final(...)` | Calcula estatísticas e exibe relatório final |
