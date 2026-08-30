# Model Card — Previsão de Churn (Telco)

## Resumo

Modelo de classificação binária que estima a probabilidade de um cliente de
telecomunicações cancelar o serviço (churn), para priorizar ações de retenção.
Ver [ML Canvas](ml_canvas.md) para o contexto de negócio completo.

- **Tipo de modelo:** Regressão Logística (`sklearn.linear_model.LogisticRegression`)
- **Pipeline:** `StandardScaler`/`OneHotEncoder` + imputação (mediana/moda), via
  `src/preprocessing.py`
- **Artefato:** `models/champion_model.joblib`, gerado por `python -m src.train`
- **Servido por:** API FastAPI (`src/api/main.py`), endpoint `POST /predict`

## Dados de treino

- **Fonte:** [Telco Customer Churn — IBM (Kaggle)](https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset)
- **Volume:** 7.043 clientes, 5.634 usados no treino e 1.409 em holdout (split 80/20 estratificado, `random_state=42`)
- **Taxa de churn:** ~26,5% (desbalanceada) — idêntica no treino e no teste graças à estratificação
- **Features usadas (19):** perfil do cliente (gênero, idoso, parceiro, dependentes), tempo de contrato, serviços contratados (telefone, internet, segurança online, backup, proteção de dispositivo, suporte técnico, streaming), tipo de contrato, forma de pagamento, cobrança mensal e total
- **Features explicitamente excluídas:**
  - Geográficas (cidade, estado, país, CEP, lat/long) — alta cardinalidade, pouco poder preditivo generalizável
  - `Churn Label` — idêntica à variável-alvo, vazamento de dado direto
  - `Churn Reason` — só é preenchida após o cliente já ter cancelado, informação indisponível no momento da previsão
  - `Churn Score` e `CLTV` — scores pré-computados de origem desconhecida no dataset original, tratados como não confiáveis para reprodução

## Escolha do modelo

Comparados via validação cruzada estratificada (5 folds) sobre o conjunto de treino
(ver `notebooks/eda_baseline.ipynb`, Etapa 2):

| Modelo | F1-score (CV) | AUC-ROC (CV) |
|---|---|---|
| **Regressão Logística** | **0.62** | **0.86** |
| MLPClassifier | 0.59 | 0.85 |
| Random Forest | 0.58 | 0.84 |

A Regressão Logística venceu sem tuning de hiperparâmetros em nenhum dos três
modelos. É um resultado plausível para esse volume de dados e número de
features — modelos não-lineares tendem a precisar de mais ajuste (ou mais
dados) para superar um linear bem regularizado.

## Performance (holdout, modelo de produção)

| Métrica | Valor |
|---|---|
| F1-score (classe Churn) | 0.61 |
| AUC-ROC | 0.85 |
| Precisão (Churn) | 0.65 |
| Recall (Churn) | 0.57 |
| Acurácia geral | 0.80 |

Matriz de confusão (1.409 clientes no holdout):

|  | Previsto: Não Churn | Previsto: Churn |
|---|---|---|
| **Real: Não Churn** | 918 | 117 |
| **Real: Churn** | 160 | 214 |

**Referência:** um classificador que sempre prevê "não churn" tem F1 = 0 para a
classe de interesse e 73,5% de acurácia — a acurácia geral não é uma métrica
informativa isolada aqui, por isso F1 e AUC-ROC foram adotados como métricas
técnicas principais (ver Etapa 1 no notebook).

## Limitações

- **Recall moderado (57%)**: quase metade dos clientes que de fato cancelam não
  é sinalizada pelo modelo no limiar padrão de 0.5. Times de retenção com
  capacidade para abordar mais clientes podem reduzir o limiar de decisão para
  aumentar o recall, à custa de mais falsos positivos.
- **Sem tuning de hiperparâmetros**: a comparação entre modelos usou
  configurações padrão/simples. Random Forest e MLP poderiam superar a
  Regressão Logística com otimização de hiperparâmetros e mais dados — a
  conclusão atual vale para o cenário testado, não é definitiva.
- **Dataset estático de um único momento**: não há dados temporais/histórico de
  comportamento ao longo do tempo. Mudanças de mercado, preço ou concorrência
  não são capturadas, e o modelo deve ser retreinado periodicamente.
- **Escopo geográfico único**: os dados são de uma operadora específica (dataset
  de demonstração da IBM); o modelo não deve ser assumido como generalizável
  para outras operadoras ou mercados sem revalidação.
- **Não explica o motivo do churn**: como `Churn Reason` foi excluída (vazamento
  de dado), o modelo prevê *quem* tem risco, não *por quê* — ofertas de
  retenção direcionadas exigem análise complementar.

## Considerações de viés e uso responsável

- O modelo usa `Gender` e `Senior Citizen` como features. Nenhuma análise de
  fairness/impacto desigual entre esses grupos foi realizada nesta entrega —
  recomenda-se auditar as taxas de erro por subgrupo antes de usar o modelo
  para decisões que afetem clientes de forma diferenciada.
- O modelo deve apoiar decisões de retenção (ex.: priorização de contato), não
  substituir julgamento humano ou ser usado para negar serviços.
- Predições são probabilidades de churn, não certezas — devem ser combinadas
  com o limiar de decisão e a capacidade operacional do time de retenção
  (ver "Objetivos e operação" no [ML Canvas](ml_canvas.md)).
