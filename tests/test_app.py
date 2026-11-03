"""Teste funcional do app com a API oficial de testes do Streamlit."""

from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).parents[1] / "app.py"


def test_app_loads_both_dashboards_without_exceptions():
    app = AppTest.from_file(APP_PATH, default_timeout=15).run()
    assert not app.exception
    assert len(app.tabs) == 2
    assert len(app.selectbox) == 1
    assert len(app.slider) == 1
    assert len(app.radio) == 1
    assert len(app.metric) >= 9


def test_widgets_respond_and_rerun_the_app():
    app = AppTest.from_file(APP_PATH, default_timeout=15).run()

    app.selectbox(key="selected_variable").select("rate").run()
    assert not app.exception
    assert app.selectbox(key="selected_variable").value == "rate"

    app.slider(key="range_rate").set_value((0.0, 100.0)).run()
    assert not app.exception
    assert app.slider(key="range_rate").value == (0.0, 100.0)

    app.radio(key="correlation_method").set_value("Pearson").run()
    assert not app.exception
    assert app.radio(key="correlation_method").value == "Pearson"
