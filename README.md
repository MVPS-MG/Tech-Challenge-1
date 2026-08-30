# Tech Challenge 1

## Etapa 1 - Entendimento e Preparação

Esta etapa concentra-se em:

- formular o problema de negócio;
- explorar os dados disponíveis;
- definir métricas técnicas e de negócio;
- construir um baseline inicial com Regressão Logística.

## Estrutura do projeto

- data/: arquivos de dados brutos.
- notebooks/: notebooks de EDA e experimentação.
- src/: código produtivo (pré-processamento, treino e API), refatorado a partir dos notebooks.
- models/: modelo campeão treinado (.pkl/.joblib).
- tests/: testes automatizados (pytest).
- docs/: ML Canvas e Model Card.

## Como executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Valide o estilo de código:
   ```bash
   black --check .
   flake8 .
   nbqa black --check notebooks
   nbqa flake8 notebooks
   ```
3. Abra o notebook em notebooks/eda_baseline.ipynb.
4. Execute as células para visualizar a análise e treinar o baseline.

## Treinar o modelo e rodar a API

1. Treine o modelo (salva em `models/champion_model.joblib`):
   ```bash
   python -m src.train
   ```
2. Suba a API:
   ```bash
   uvicorn src.api.main:app --reload
   ```
3. Endpoints disponíveis:
   - `GET /health` — checa se a API está no ar.
   - `POST /predict` — recebe os dados do cliente e retorna a propensão de churn.
     Exemplo de payload em `tests/test_api.py`, ou veja `/docs` para o schema completo.
4. Rode os testes:
   ```bash
   pytest
   ```
