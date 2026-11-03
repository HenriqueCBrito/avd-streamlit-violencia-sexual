# Observatório UN CTS de violência sexual registrada

Aplicação Streamlit construída a partir de uma análise exploratória dos registros anuais de violência sexual da United Nations Survey of Crime Trends and Operations of Criminal Justice Systems, com 918 observações de 102 países e territórios entre 2003 e 2011.

## Aplicação publicada

[Acessar o Observatório UN-CTS no Streamlit Community Cloud](https://painel-un-cts-avd.streamlit.app)

## Validação do deploy

- [x] aplicação aberta em uma sessão separada sem autenticação;
- [x] seletor de variável, slider e método de correlação respondem;
- [x] os dois dashboards carregam pelas abas;
- [x] KPIs e gráficos são recalculados após os filtros;
- [x] não foram encontrados dados pessoais, segredos ou caminhos locais publicados.

## Dashboards

### Dashboard 1 Laboratório

- seletor de variável quantitativa e filtro de intervalo na barra lateral;
- mapa de calor com correlação de Spearman ou Pearson;
- histograma com boxplot marginal;
- resumos de mediana, intervalo interquartil e valores extremos.

### Dashboard 2 Gestão pública

- cinco KPIs de magnitude, taxa e cobertura;
- evolução anual da taxa mediana com intervalo interquartil;
- países com maiores medianas, exigindo pelo menos cinco anos observados;
- cobertura anual da taxa, separando dados disponíveis e ausentes.

## Como executar localmente

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
streamlit run app.py
```

O app abrirá em `http://localhost:8501`.

## Testes

```bash
pytest -q
```

Os testes verificam o esquema e a agregação pública dos dados, as regras dos KPIs, a resposta dos widgets e o carregamento das duas abas.

## Estrutura do repositório

```text
.
├── app.py
├── src/
│   └── dashboard_utils.py
├── data/
│   ├── clean/
│   │   └── dataset.csv
│   └── raw/             ← dado bruto, não versionado
├── notebooks/
│   └── eda_crimes_violencia_sexual_final.ipynb
├── entregas/
│   ├── justificativa-metricas.md
│   ├── rascunho-dashboard1.png
│   └── rascunho-dashboard2.png
├── prompts/
│   └── registro-prompts.md
├── tests/
├── ALTAIR-CROSSFILTER.md
├── ROTEIRO.md
├── requirements.txt
└── requirements-dev.txt
```

## Privacidade e limitações

A base contém somente agregações por país e ano. Não há nomes de pessoas, endereços, documentos, contatos ou registros individuais. Ainda assim, os resultados exigem cautela: definições legais, subnotificação, práticas de registro e cobertura institucional variam entre países e anos. O painel não mede causalidade e não deve ser usado como ranking direto de segurança.
