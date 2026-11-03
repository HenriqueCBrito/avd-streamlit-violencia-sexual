"""Aplicação Streamlit para explorar a base UN-CTS de violência sexual."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from src.dashboard_utils import (
    annual_rate_summary,
    compute_kpis,
    country_rate_summary,
    filter_by_range,
    load_data,
)


st.set_page_config(
    page_title="Observatório UN-CTS",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA_PATH = Path(__file__).parent / "data" / "clean" / "dataset.csv"
VARIABLE_LABELS = {
    "sexual violence": "Ocorrências registradas",
    "rate": "Taxa por 100 mil habitantes",
}
PURPLE = "#5A3D7A"
TERRACOTTA = "#C47F6A"
NEUTRAL = "#B8B8B8"
ALERT = "#A53F3F"

st.markdown(
    """
    <style>
    .block-container {padding-top: 2rem; padding-bottom: 3rem;}
    [data-testid="stMetric"] {
        background: rgba(90, 61, 122, 0.06);
        border: 1px solid rgba(90, 61, 122, 0.18);
        border-radius: 0.8rem;
        padding: 0.85rem;
    }
    [data-testid="stSidebar"] {border-right: 1px solid rgba(90, 61, 122, 0.15);}
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def get_data() -> pd.DataFrame:
    return load_data(DATA_PATH)


def format_integer(value: float) -> str:
    return f"{value:,.0f}".replace(",", ".")


def format_decimal(value: float) -> str:
    if pd.isna(value):
        return "Sem dados"
    return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


data = get_data()

st.title("Observatório de violência sexual registrada")
st.write(
    "Análise exploratória dos registros anuais da UN-CTS para 102 países e "
    "territórios entre 2003 e 2011. Os dados refletem registros oficiais e "
    "não medem diretamente a prevalência real do fenômeno."
)


with st.sidebar:
    st.header("Painel de análise")
    selected_variable = st.selectbox(
        "Variável quantitativa",
        options=list(VARIABLE_LABELS),
        format_func=VARIABLE_LABELS.get,
        key="selected_variable",
        help="Define o histograma e o intervalo usado nos dois dashboards.",
    )

    observed_values = data[selected_variable].dropna()
    minimum = float(observed_values.min())
    maximum = float(observed_values.max())
    step = 1.0 if selected_variable == "sexual violence" else 0.1
    selected_range = st.slider(
        f"Intervalo de {VARIABLE_LABELS[selected_variable].lower()}",
        min_value=minimum,
        max_value=maximum,
        value=(minimum, maximum),
        step=step,
        key=f"range_{selected_variable}",
        help=(
            "Valores observados fora do intervalo são removidos. Linhas ausentes "
            "permanecem para que a cobertura dos dados possa ser medida."
        ),
    )

    filtered = filter_by_range(
        data, selected_variable, selected_range[0], selected_range[1]
    )
    included_observations = filtered[selected_variable].notna().sum()
    st.caption(
        f"{included_observations} valores observados incluídos; "
        f"{len(data) - len(filtered)} linhas excluídas pelo intervalo."
    )
    st.divider()
    st.caption("Fonte: UN Survey of Crime Trends and Operations of Criminal Justice Systems.")


laboratory_tab, strategy_tab = st.tabs(
    ["Dashboard 1 · Laboratório", "Dashboard 2 · Gestão pública"]
)


with laboratory_tab:
    st.header("Laboratório de distribuição e correlação")
    st.caption(
        "Explore a forma da distribuição e compare a associação entre contagem "
        "e taxa. Valores ausentes são descartados apenas no cálculo que os exige."
    )

    left, right = st.columns([1, 1], gap="large")

    with left:
        method_label = st.radio(
            "Método da correlação",
            options=["Spearman", "Pearson"],
            horizontal=True,
            key="correlation_method",
            help="Spearman é mais resistente à assimetria e aos valores extremos.",
        )
        method = method_label.lower()
        corr = filtered[["sexual violence", "rate"]].corr(method=method)
        corr_labels = [VARIABLE_LABELS[column] for column in corr.columns]
        heatmap = go.Figure(
            data=go.Heatmap(
                z=corr.values,
                x=corr_labels,
                y=corr_labels,
                zmin=-1,
                zmax=1,
                colorscale=[
                    [0.0, "#2E6F9E"],
                    [0.5, "#F6F3F8"],
                    [1.0, PURPLE],
                ],
                text=np.round(corr.values, 2),
                texttemplate="%{text:.2f}",
                hovertemplate="%{y} × %{x}<br>Correlação: %{z:.3f}<extra></extra>",
                colorbar_title="Coeficiente",
            )
        )
        heatmap.update_layout(
            title=f"Mapa de calor · correlação de {method_label}",
            height=430,
            margin=dict(l=20, r=20, t=70, b=20),
        )
        st.plotly_chart(heatmap, width="stretch", config={"displayModeBar": False})

    with right:
        histogram_data = filtered.dropna(subset=[selected_variable]).copy()
        bins = max(10, min(40, int(np.sqrt(len(histogram_data)) * 2)))
        histogram = px.histogram(
            histogram_data,
            x=selected_variable,
            nbins=bins,
            marginal="box",
            color_discrete_sequence=[PURPLE],
            labels={selected_variable: VARIABLE_LABELS[selected_variable]},
            title=f"Distribuição de {VARIABLE_LABELS[selected_variable].lower()}",
        )
        histogram.update_layout(
            height=430,
            bargap=0.04,
            yaxis_title="Número de observações",
            margin=dict(l=20, r=20, t=70, b=20),
        )
        st.plotly_chart(
            histogram, width="stretch", config={"displayModeBar": False}
        )

    distribution = filtered[selected_variable].dropna()
    q1, median, q3 = distribution.quantile([0.25, 0.5, 0.75])
    upper_iqr = q3 + 1.5 * (q3 - q1)
    summary_columns = st.columns(4)
    summary_columns[0].metric("Observações", format_integer(len(distribution)))
    summary_columns[1].metric("Mediana", format_decimal(median))
    summary_columns[2].metric("Intervalo interquartil", format_decimal(q3 - q1))
    summary_columns[3].metric(
        "Acima do limite IQR", format_integer((distribution > upper_iqr).sum())
    )

    with st.expander("Como interpretar este laboratório"):
        st.write(
            "As duas variáveis têm cauda longa à direita. A correlação resume "
            "associação, não causalidade. Pearson enfatiza relações lineares; "
            "Spearman avalia uma relação monotônica por postos e é mais adequada "
            "como leitura principal para estes dados assimétricos."
        )


with strategy_tab:
    st.header("Painel estratégico para gestão pública")
    st.caption(
        "Indicadores para acompanhar magnitude registrada, comparabilidade e "
        "qualidade da cobertura. O painel não deve ser usado como ranking de segurança."
    )

    kpis = compute_kpis(filtered)
    metric_columns = st.columns(5)
    metric_columns[0].metric(
        "Ocorrências registradas", format_integer(kpis["total_occurrences"])
    )
    metric_columns[1].metric("Taxa mediana", format_decimal(kpis["median_rate"]))
    metric_columns[2].metric(
        "Cobertura da taxa", f"{format_decimal(kpis['rate_coverage'])}%"
    )
    metric_columns[3].metric(
        "Países com taxa", format_integer(kpis["countries_with_rate"])
    )
    metric_columns[4].metric(
        "Pares completos", format_integer(kpis["complete_pairs"])
    )

    annual = annual_rate_summary(filtered)
    trend = go.Figure()
    trend.add_trace(
        go.Scatter(
            x=annual["date"],
            y=annual["q3"],
            line=dict(width=0),
            hoverinfo="skip",
            showlegend=False,
            name="3º quartil",
        )
    )
    trend.add_trace(
        go.Scatter(
            x=annual["date"],
            y=annual["q1"],
            fill="tonexty",
            fillcolor="rgba(196,127,106,0.22)",
            line=dict(width=0),
            hoverinfo="skip",
            name="Intervalo interquartil",
        )
    )
    trend.add_trace(
        go.Scatter(
            x=annual["date"],
            y=annual["median"],
            mode="lines+markers",
            line=dict(color=PURPLE, width=3),
            marker=dict(size=8),
            name="Mediana",
            customdata=annual[["observed_rate"]],
            hovertemplate=(
                "Ano: %{x}<br>Taxa mediana: %{y:.2f}<br>"
                "Taxas observadas: %{customdata[0]}<extra></extra>"
            ),
        )
    )
    trend.update_layout(
        title="Evolução anual da taxa mediana e intervalo interquartil",
        xaxis_title="Ano",
        yaxis_title="Taxa por 100 mil habitantes",
        height=450,
        hovermode="x unified",
        margin=dict(l=20, r=20, t=70, b=20),
    )
    st.plotly_chart(trend, width="stretch", config={"displayModeBar": False})

    chart_left, chart_right = st.columns(2, gap="large")

    with chart_left:
        countries = country_rate_summary(filtered)
        if countries.empty:
            st.warning(
                "O intervalo selecionado não deixou países com cinco anos de taxa observada."
            )
        else:
            country_chart = px.bar(
                countries,
                x="median_rate",
                y="country/territory",
                orientation="h",
                color_discrete_sequence=[TERRACOTTA],
                labels={
                    "median_rate": "Taxa mediana",
                    "country/territory": "",
                },
                title="10 maiores taxas medianas · mínimo de 5 anos",
                custom_data=["observed_years"],
            )
            country_chart.update_traces(
                hovertemplate=(
                    "%{y}<br>Taxa mediana: %{x:.2f}<br>"
                    "Anos observados: %{customdata[0]}<extra></extra>"
                )
            )
            country_chart.update_layout(
                height=500, margin=dict(l=20, r=20, t=70, b=20)
            )
            st.plotly_chart(
                country_chart,
                width="stretch",
                config={"displayModeBar": False},
            )

    with chart_right:
        coverage_chart = go.Figure(
            data=[
                go.Bar(
                    x=annual["date"],
                    y=annual["observed_rate"],
                    name="Taxa disponível",
                    marker_color=PURPLE,
                ),
                go.Bar(
                    x=annual["date"],
                    y=annual["missing_rate"],
                    name="Taxa ausente",
                    marker_color=NEUTRAL,
                ),
            ]
        )
        coverage_chart.update_layout(
            barmode="stack",
            title="Cobertura da taxa por ano",
            xaxis_title="Ano",
            yaxis_title="Número de países/territórios",
            height=500,
            legend_title="Situação",
            margin=dict(l=20, r=20, t=70, b=20),
        )
        st.plotly_chart(
            coverage_chart, width="stretch", config={"displayModeBar": False}
        )

    st.info(
        "As diferenças entre países e anos podem refletir prevalência, definições "
        "legais, subnotificação, práticas de registro e cobertura institucional. "
        "Decisões públicas devem combinar estes indicadores com fontes locais."
    )

st.divider()
st.caption(
    "Base agregada por país e ano, sem dados pessoais. Período 2003–2011. "
    "Projeto acadêmico baseado na EDA UN-CTS."
)
