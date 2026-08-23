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
