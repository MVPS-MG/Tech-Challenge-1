# Tech Challenge 1 — Pipeline Preditivo de Churn

Pipeline de Machine Learning para prever o risco de cancelamento (churn) de
clientes de uma operadora de telecomunicações, do entendimento do problema até
uma API de inferência, usando Scikit-Learn e FastAPI.

## Contexto de negócio

Uma operadora quer reduzir a perda de clientes identificando com antecedência
quem tem maior risco de cancelar, para priorizar ações de retenção. Detalhes
completos de stakeholders, métricas de negócio e restrições estão no
[ML Canvas](docs/ml_canvas.md).

## Resultado

Modelo campeão: **Regressão Logística** (venceu Random Forest e MLP em
validação cruzada). No holdout: **F1-score ≈ 0.61** e **AUC-ROC ≈ 0.85**.
Detalhes de performance, limitações e vieses no [Model Card](docs/model_card.md).

## Estrutura do projeto

```
├── data/            # dataset (Telco Customer Churn - IBM)
├── docs/            # ML Canvas e Model Card
├── models/          # modelo campeão treinado (champion_model.joblib)
├── notebooks/       # EDA, comparação de modelos (experimentação)
├── src/
│   ├── main.py           # entrypoint FastAPI
│   ├── preprocessing.py  # limpeza de dados + pipeline de features
│   ├── train.py          # treino do modelo campeão
│   ├── routes/           # endpoints da API
│   ├── services/         # lógica de inferência
│   ├── models/           # schemas e modelos de domínio
│   └── tests/            # testes específicos da camada src
├── tests/           # testes automatizados (pytest)
└── requirements.txt
```

## Setup

Requer Python 3.11+.

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/Mac

pip install -r requirements.txt
```

## Explorar a análise e a modelagem

```bash
jupyter notebook notebooks/eda_baseline.ipynb
```

O notebook documenta, em ordem: EDA (Etapa 1), limpeza dos dados e tratamento
de vazamento de dado, definição de métricas, baseline de Regressão Logística,
e a comparação com Random Forest e MLPClassifier via validação cruzada
(Etapa 2).

## Treinar o modelo

```bash
python -m src.train
```

Treina o modelo campeão (Regressão Logística) usando o pipeline de
pré-processamento de `src/preprocessing.py` (seed fixa, `random_state=42`) e
salva em `models/champion_model.joblib`.

## Rodar a API

```bash
uvicorn src.main:app --reload
```

Endpoints:

- `GET /health` — checa se a API está no ar. Sempre responde, mesmo sem
  modelo treinado.
- `POST /predict` — recebe os dados de um cliente e retorna a propensão de
  churn. Schema completo em `http://127.0.0.1:8000/docs`.

Exemplo:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "gender": "Female", "senior_citizen": "No", "partner": "Yes",
    "dependents": "No", "tenure_months": 2, "phone_service": "Yes",
    "multiple_lines": "No", "internet_service": "Fiber optic",
    "online_security": "No", "online_backup": "No", "device_protection": "No",
    "tech_support": "No", "streaming_tv": "No", "streaming_movies": "No",
    "contract": "Month-to-month", "paperless_billing": "Yes",
    "payment_method": "Electronic check", "monthly_charges": 70.35,
    "total_charges": 140.70
  }'
```

```json
{ "churn_probability": 0.7618, "churn_prediction": true }
```

## Rodar os testes

```bash
pytest
```

Cobre a limpeza de dados (remoção de colunas com vazamento de dado) e a API
(status de `/health` e uma predição de ponta a ponta).

## Lint

```bash
black --check .
flake8 .
nbqa black --check notebooks
nbqa flake8 notebooks
```

## Reprodutibilidade

Todos os splits de treino/teste e modelos usam `random_state=42`.
