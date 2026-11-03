"""Testes das regras analíticas do dashboard."""

from pathlib import Path

import pandas as pd
import pytest

from src.dashboard_utils import compute_kpis, filter_by_range, load_data


DATA_PATH = Path(__file__).parents[1] / "data" / "clean" / "dataset.csv"


def test_dataset_schema_and_public_aggregation():
    data = load_data(DATA_PATH)
    assert data.shape == (918, 4)
    assert data["country/territory"].nunique() == 102
    assert data["date"].min() == 2003
    assert data["date"].max() == 2011
    assert set(data.columns) == {
        "country/territory",
        "date",
        "sexual violence",
        "rate",
    }


def test_range_filter_excludes_values_but_preserves_missing_rows():
    data = pd.DataFrame(
        {
            "country/territory": ["A", "B", "C"],
            "date": [2003, 2003, 2003],
            "sexual violence": [10.0, 100.0, None],
            "rate": [1.0, 2.0, None],
        }
    )
    filtered = filter_by_range(data, "sexual violence", 0.0, 50.0)
    assert filtered["country/territory"].tolist() == ["A", "C"]


def test_kpis_are_computed_from_filtered_data():
    data = pd.DataFrame(
        {
            "country/territory": ["A", "A", "B"],
            "date": [2003, 2004, 2003],
            "sexual violence": [10.0, 20.0, None],
            "rate": [2.0, 4.0, None],
        }
    )
    kpis = compute_kpis(data)
    assert kpis["total_occurrences"] == 30.0
    assert kpis["median_rate"] == 3.0
    assert kpis["rate_coverage"] == pytest.approx(200 / 3)
    assert kpis["countries_with_rate"] == 1
    assert kpis["complete_pairs"] == 2
