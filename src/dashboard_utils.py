"""Funções analíticas reutilizadas pelo app e pelos testes."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


EXPECTED_COLUMNS = ["country/territory", "date", "sexual violence", "rate"]


def load_data(path: str | Path) -> pd.DataFrame:
    """Carrega o CSV e valida o esquema mínimo esperado."""
    data = pd.read_csv(path, na_values=["NA", "N/A", ""])
    missing_columns = set(EXPECTED_COLUMNS) - set(data.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Colunas obrigatórias ausentes: {missing}")

    data = data[EXPECTED_COLUMNS].copy()
    data["date"] = pd.to_numeric(data["date"], errors="raise").astype(int)
    for column in ["sexual violence", "rate"]:
        data[column] = pd.to_numeric(data[column], errors="coerce")
    return data


def filter_by_range(
    data: pd.DataFrame, variable: str, lower: float, upper: float
) -> pd.DataFrame:
    """Exclui valores observados fora do intervalo e preserva ausentes."""
    if variable not in {"sexual violence", "rate"}:
        raise ValueError(f"Variável não suportada: {variable}")
    values = data[variable]
    mask = values.isna() | values.between(lower, upper, inclusive="both")
    return data.loc[mask].copy()


def compute_kpis(data: pd.DataFrame) -> dict[str, float | int]:
    """Calcula os cinco KPIs do painel estratégico."""
    rate_observed = data["rate"].notna()
    count_observed = data["sexual violence"].notna()
    complete_pairs = rate_observed & count_observed
    denominator = len(data)

    return {
        "total_occurrences": float(data["sexual violence"].sum()),
        "median_rate": float(data["rate"].median()),
        "rate_coverage": float(rate_observed.mean() * 100) if denominator else 0.0,
        "countries_with_rate": int(
            data.loc[rate_observed, "country/territory"].nunique()
        ),
        "complete_pairs": int(complete_pairs.sum()),
    }


# [IA] Codex - agregação anual de taxa, quartis e cobertura para o painel estratégico.
def annual_rate_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Resume a taxa por ano com cobertura, quartis e mediana."""
    summary = (
        data.groupby("date", as_index=False)
        .agg(
            total_rows=("country/territory", "size"),
            observed_rate=("rate", "count"),
            q1=("rate", lambda series: series.quantile(0.25)),
            median=("rate", "median"),
            q3=("rate", lambda series: series.quantile(0.75)),
        )
        .sort_values("date")
    )
    summary["missing_rate"] = summary["total_rows"] - summary["observed_rate"]
    return summary


def country_rate_summary(data: pd.DataFrame, minimum_years: int = 5) -> pd.DataFrame:
    """Retorna os dez países com maior mediana e cobertura mínima."""
    summary = (
        data.dropna(subset=["rate"])
        .groupby("country/territory", as_index=False)
        .agg(observed_years=("rate", "count"), median_rate=("rate", "median"))
    )
    return (
        summary.loc[summary["observed_years"] >= minimum_years]
        .nlargest(10, "median_rate")
        .sort_values("median_rate")
    )
