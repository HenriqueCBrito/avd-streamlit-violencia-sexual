# Justificativa das métricas — Dashboard 2

## Público-alvo

Equipes de gestão pública que precisam acompanhar registros internacionais sem confundir volume notificado com prevalência real. O painel combina magnitude, taxa relativa e cobertura da informação para apoiar esse acompanhamento.

## Métrica 1: Ocorrências registradas

- **Variável:** `sexual violence` (contagem absoluta por país/território e ano)
- **O que mede:** soma dos registros de violência sexual no recorte filtrado.
- **Por que foi escolhida:** dimensiona a carga registrada no período e recorte selecionados, servindo como ponto de partida para qualquer análise de magnitude.
- **O que comunica ao público-alvo:** o volume total de casos notificados — não a prevalência real, mas o que os sistemas oficiais registraram. Diferenças entre países de populações diferentes não devem ser comparadas isoladamente com esse número.

## Métrica 2: Taxa mediana

- **Variável:** `rate` (taxa por 100 mil habitantes)
- **O que mede:** mediana da taxa no recorte filtrado.
- **Por que foi escolhida:** a mediana reduz a influência da cauda longa e dos valores extremos identificados na EDA, tornando o resumo mais representativo do conjunto.
- **O que comunica ao público-alvo:** um valor central de referência que permite comparar períodos e recortes sem que países com valores extremos distorçam a leitura.

## Métrica 3: Cobertura da taxa

- **Variável:** `rate` (proporção de linhas com valor disponível)
- **O que mede:** percentual de linhas com `rate` preenchida no recorte.
- **Por que foi escolhida:** informa quanto do recorte sustenta comparações relativas, evitando apresentar um resultado sem indicar sua base observacional.
- **O que comunica ao público-alvo:** o grau de confiabilidade da taxa mediana — quanto maior a cobertura, mais representativo o valor central apresentado.

## Métrica 4: Países com taxa

- **Variável:** `country/territory` filtrado por linhas com `rate` disponível
- **O que mede:** quantidade de países ou territórios com pelo menos uma taxa observada no recorte.
- **Por que foi escolhida:** mostra a abrangência geográfica efetiva, separando a cobertura por linha da cobertura por país.
- **O que comunica ao público-alvo:** quantos países têm pelo menos um ponto de dados comparável, sinalizando se o recorte cobre uma região ampla ou restrita.

## Métrica 5: Pares completos

- **Variável:** linhas com `sexual violence` e `rate` simultaneamente disponíveis
- **O que mede:** número de linhas com contagem e taxa preenchidas ao mesmo tempo.
- **Por que foi escolhida:** informa o tamanho real da amostra utilizável para análises de associação entre as duas variáveis.
- **O que comunica ao público-alvo:** quantas observações permitem cruzar volume com taxa — quanto menor esse número em relação ao total, mais cautela é necessária ao interpretar correlações.

## Regras de leitura

Os filtros da barra lateral afetam os dois dashboards. O slider remove valores observados fora do intervalo, mas mantém as linhas ausentes para que os indicadores de cobertura permaneçam calculáveis. Os números são registros oficiais agregados por país e ano; diferenças legais, institucionais e de notificação limitam comparações diretas.