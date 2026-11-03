# Registro de uso de IA

## Ferramenta

Codex, da OpenAI.

## Uso realizado

O Codex foi utilizado como apoio para estruturar e organizar o projeto Streamlit: separar responsabilidades entre a interface e as funções analíticas, ordenar os arquivos do repositório e manter uma apresentação consistente do código.

## Trecho elaborado com apoio de IA

O único trecho de código identificado como elaborado com apoio do Codex é a função `annual_rate_summary`, no arquivo `dashboard_utils.py`.

Essa função foi escolhida por concentrar a lógica mais complexa do projeto: agrupa os registros por ano, calcula quantidade de observações, cobertura da taxa, primeiro quartil, mediana, terceiro quartil e deriva o total de taxas ausentes. O resultado abastece os gráficos de tendência e cobertura do painel estratégico.

O trecho está sinalizado no código com o comentário:

```python
# [IA] Codex - agregação anual de taxa, quartis e cobertura para o painel estratégico.
```

## Verificação

O resultado da função é coberto pelos testes automatizados do projeto e pode ser conferido na execução local da aplicação. As demais decisões analíticas, textos, interface e código foram organizados e revisados no projeto sem marcação de autoria por IA.
