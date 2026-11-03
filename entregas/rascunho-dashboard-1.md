# Rascunho do Dashboard 1

## Laboratório de distribuição e correlação

```text
┌──────────────────────── Painel lateral ────────────────────────┐
│ Variável quantitativa: [ocorrências | taxa]                   │
│ Intervalo:              [────────●────────●────────]          │
└────────────────────────────────────────────────────────────────┘

┌───────────────────────────────┬────────────────────────────────┐
│ Método: Spearman | Pearson    │                                │
│                               │ Histograma da variável         │
│ Mapa de calor 2 × 2           │ selecionada + boxplot marginal │
│ contagem × taxa               │                                │
└───────────────────────────────┴────────────────────────────────┘

┌──────────────┬──────────────┬──────────────┬───────────────────┐
│ Observações  │ Mediana      │ IQR          │ Acima do limite   │
│              │              │              │ IQR               │
└──────────────┴──────────────┴──────────────┴───────────────────┘
```

O rascunho prioriza comparação imediata entre a matriz de correlação e a forma da distribuição. A seleção de variável controla o histograma e o slider; o método alterna a correlação entre Spearman e Pearson.
