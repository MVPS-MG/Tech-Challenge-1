# src/

Código produtivo do projeto (não experimental — experimentação fica em `notebooks/`).

Layout previsto para a Etapa 3:

- `preprocessing.py` — funções de limpeza, imputação e encoding usadas tanto no
  treino quanto na API (refatoradas a partir do `notebooks/eda_baseline.ipynb`).
- `train.py` — treino dos modelos (baseline, árvore/ensemble, MLP) e seleção do
  modelo campeão, salvando o resultado em `models/`.
- `api/` — aplicação FastAPI com os endpoints `/health` e `/predict`.

Cada módulo deve ser importável sem efeitos colaterais (sem código solto no
nível do módulo), para permitir testes unitários com `pytest`.
