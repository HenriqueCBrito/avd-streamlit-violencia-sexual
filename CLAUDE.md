# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Setup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

# Run the app
streamlit run app.py          # opens at http://localhost:8501

# Run all tests
pytest -q

# Run a single test file or test
pytest tests/test_dashboard_utils.py -q
pytest tests/test_app.py::test_app_loads_both_dashboards_without_exceptions -q
```

`requirements.txt` is the production dependency set (streamlit, pandas, numpy, plotly). `requirements-dev.txt` extends it with pytest.

## Architecture

### Data flow

```
data/clean/dataset.csv
    └── src/dashboard_utils.py :: load_data()
            └── app.py :: get_data()  (cached with @st.cache_data)
                    └── sidebar filters → filtered DataFrame
                            └── Dashboard 1 (lab_tab) + Dashboard 2 (strategy_tab)
```

The raw dataset (`data/raw/`, gitignored except `.gitkeep`) is never read by the app. Only `data/clean/dataset.csv` is committed and read at runtime — this is intentional so Streamlit Community Cloud can serve it directly from GitHub.

### Module responsibilities

- **`src/dashboard_utils.py`** — all pure analytical logic: `load_data`, `filter_by_range`, `compute_kpis`, `annual_rate_summary`, `country_rate_summary`. No Streamlit imports here.
- **`app.py`** — presentation only: page config, sidebar widgets, two `st.tabs`, Plotly charts. Calls `src.dashboard_utils` for every data transformation.

### Dataset shape

918 rows × 4 columns (`country/territory`, `date`, `sexual violence`, `rate`), covering 102 countries/territories from 2003–2011. `rate` has significant missingness; `filter_by_range` preserves `NaN` rows by design so coverage metrics remain accurate.

### Tests

- `tests/test_dashboard_utils.py` — unit tests for pure functions (schema, filter edge cases, KPI computation). Fast, no Streamlit dependency.
- `tests/test_app.py` — integration tests using `streamlit.testing.v1.AppTest`. Exercises widget keys (`selected_variable`, `range_rate`, `correlation_method`) and asserts tab count, metric count, and no exceptions after reruns.

### Visual identity

Defined in `.streamlit/config.toml`: primary purple `#5A3D7A`, terracotta accent `#C47F6A`. These constants are also hardcoded in `app.py` (`PURPLE`, `TERRACOTTA`, `NEUTRAL`, `ALERT`) for use in Plotly chart color sequences.
