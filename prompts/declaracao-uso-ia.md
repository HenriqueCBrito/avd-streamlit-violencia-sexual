## Seção 1 — Identificação

| Campo | Valor |
|---|---|
| Turma | **5A** |
| Nome Completo | **Henrique Sérgio Carneiro de Brito** |
| E-mail | hscb@cesar.school |
| Repositório | https://github.com/HenriqueCBrito/avd-streamlit-violencia-sexual |
| Data de entrega | 3/11/2026 |

---

## Seção 3 — Declaração geral

☑ **Utilizei** IA generativa, somente nas situações permitidas, e registrei todos os usos nas Seções 4 a 6.

---

## Seção 4 — Ferramentas utilizadas

| Ferramenta | Versão / plano | Em que parte da atividade |
|---|---|---|
| ChatGPT (OpenAI) | Versão paga | Esqueleto do `app.py` (Aula 21) |
| Claude Code (Anthropic) | Versão paga | Reorganização da estrutura do projeto e deploy |

---

## Seção 5 — Registro de usos (Opção B — bloco a bloco)

### Uso nº 1

| Campo | Conteúdo |
|---|---|
| **Data** | Aula 21 (outubro de 2026) |
| **Ferramenta** | ChatGPT (OpenAI), versão paga |
| **Parte da atividade** | `app.py` — esqueleto inicial |
| **Finalidade** | Gerar o esqueleto do `app.py` a partir do rascunho de layout (item permitido da Seção 2) |
| **O que foi pedido** | Geração do esqueleto do `app.py` a partir do rascunho do Dashboard 1: sidebar com seletor de variável e slider de intervalo, duas abas (Dashboard 1 e Dashboard 2), estrutura de colunas para heatmap e histograma |
| **O que foi aproveitado / modificado** | Aproveitei a estrutura geral de abas, sidebar e layout de colunas. Adaptei os nomes das variáveis, labels e constantes de cor para o dataset UN-CTS; substituí os gráficos de exemplo pelos gráficos definitivos de Plotly |
| **Como verificou que estava correto** | Rodei localmente com `streamlit run app.py` e testei os widgets na interface |
| **Link ou anexo** | — |

---

### Uso nº 2

| Campo | Conteúdo |
|---|---|
| **Data** | 3/11/2026 |
| **Ferramenta** | Claude Code (Anthropic), versão paga |
| **Parte da atividade** | Estrutura do repositório — `src/`, `data/clean/`, `.gitignore`, imports |
| **Finalidade** | Apoio técnico na organização de arquivos para seguir a estrutura do repositório de referência do curso |
| **O que foi pedido** | Mover `dashboard_utils.py` para `src/`, renomear e mover o CSV para `data/clean/dataset.csv`, atualizar todos os imports em `app.py` e nos testes, substituir o `.gitignore` pela versão do repositório de referência |
| **O que foi aproveitado / modificado** | Aceitei todos os movimentos de arquivo e atualizações de import; revisei cada mudança proposta antes de confirmar no terminal |
| **Como verificou que estava correto** | Verifiquei com `git status`, inspecionei os arquivos alterados e rodei os imports manualmente |
| **Link ou anexo** | — |

---

### Uso nº 3

| Campo | Conteúdo |
|---|---|
| **Data** | 3/11/2026 |
| **Ferramenta** | Claude Code (Anthropic), versão paga |
| **Parte da atividade** | Deploy — `requirements.txt`, README, Streamlit Community Cloud |
| **Finalidade** | Depuração e verificação do checklist de deploy (item permitido da Seção 2) |
| **O que foi pedido** | Verificar se o repositório estava pronto para deploy: `requirements.txt` completo, `data/clean/dataset.csv` versionado, caminhos relativos, nenhum segredo commitado; e atualizar a seção de estrutura do README |
| **O que foi aproveitado / modificado** | Aceitei a atualização do README e a confirmação do checklist; o push para o GitHub e a verificação final do app publicado foram feitos por mim |
| **Como verificou que estava correto** | Abri o app publicado em janela anônima e testei as duas abas e os widgets |
| **Link ou anexo** | — |

---

## Seção 6 — Trechos de código feitos com apoio de IA

| Arquivo / parte | Teve apoio de IA? | Tipo de apoio |
|---|---|---|
| `app.py` (esqueleto) | **Sim** | Esqueleto gerado com ChatGPT a partir do rascunho de layout |
| Dashboard 1 (correlação + distribuição) | **Não** | — |
| Dashboard 2 (KPIs) | **Não** | — |
| Deploy / configuração | **Sim** | Claude Code — verificação do checklist e atualização do README |
| `src/dashboard_utils.py` (`annual_rate_summary`) | **Sim** | ChatGPT/Codex — agregação anual de taxa, quartis e cobertura (marcado com `# [IA]` no código) |

---

## Seção 7 — Reflexão individual



A inteligência artificial foi usada em dois momentos distintos do projeto: na geração do esqueleto inicial do `app.py` e na reorganização da estrutura de pastas do repositório.

No primeiro caso, usei o ChatGPT para transformar o rascunho do Dashboard 1 em código Streamlit. O resultado me deu uma estrutura de abas, sidebar e colunas que funcionava como ponto de partida, mas precisei adaptar praticamente todos os detalhes: os nomes das variáveis do dataset UN-CTS, as constantes de cor, os tipos de gráfico e as funções analíticas. O esqueleto sozinho não teria gerado um dashboard coerente com a análise exploratória que fiz.

No segundo caso, usei o Claude Code para reorganizar o repositório seguindo a estrutura de referência do curso. Todas as mudanças propostas foram revisadas por mim antes de ser confirmadas — nenhum arquivo foi movido ou alterado sem eu entender o que estava acontecendo.

As métricas do Dashboard 2 foram escolhidas por mim, a partir dos resultados da EDA: identifiquei que o dataset tem cobertura incompleta para a variável `rate` e que a distribuição de `sexual violence` tem cauda longa. Por isso escolhi mediana em vez de média, inclui indicadores de cobertura e limitei o ranking de países a um mínimo de cinco anos observados. Nenhuma dessas decisões veio de sugestão de IA — a IA não foi consultada para escolher métricas nem para interpretar os dados.

O que garantiu que as escolhas fossem minhas foi o fluxo que segui: primeiro a EDA, depois a justificativa escrita por mim, e só então a implementação. A IA entrou apenas na camada técnica de código, não nas decisões analíticas.

---

## Seção 8 — Termo de responsabilidade

Preencher com nome e assinatura (manuscrita ou gov.br) no DOCX antes de exportar como PDF.

| Nome | Assinatura | Data |
|---|---|---|
| Henrique Sérgio Carneiro de Brito | _(assinar no DOCX)_ | 3/11/2026 |
