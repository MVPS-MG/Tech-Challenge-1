## 1. Definição do problema de negócio

A empresa de telecomunicações busca reduzir a perda de clientes em 15% por meio da
identificação antecipada daqueles com maior propensão ao churn.

O objetivo do projeto é desenvolver um modelo de Machine Learning capaz de
estimar o risco de cancelamento de cada cliente com base em suas características,
serviços contratados, histórico de relacionamento e informações de cobrança.

As previsões permitem ações preventivas de retenção, possibilitando que as áreas
responsáveis priorizem clientes com maior risco de cancelamento antes que o churn
ocorra.

## 2. Métrica de sucesso (KPI)

O principal KPI de negócio considerado é a taxa de churn (Churn Rate), que
representa a proporção de clientes que cancelam seus serviços em determinado
período.

Em um cenário de utilização do modelo em produção, o sucesso da iniciativa poderia
ser avaliado pela redução da taxa de churn entre os clientes identificados como de
alto risco e submetidos a ações preventivas de retenção.

## 3. Levantamento de requisitos e restrições

As seguintes questões deveriam ser discutidas com os stakeholders antes da
implementação da solução:

### Objetivos e operação

- Com que antecedência um cliente precisa ser identificado como propenso ao churn
  para que seja possível realizar uma ação de retenção?
- Com que frequência as previsões devem ser atualizadas?
- Quais ações de retenção podem ser aplicadas aos clientes classificados como
  alto risco?
- Existe uma capacidade máxima de clientes que a equipe de retenção consegue
  abordar em determinado período?

### Critérios de sucesso

- Existe um custo máximo aceitável por ação de retenção?
- O custo de não identificar um cliente que irá cancelar é maior que o custo de
  abordar um cliente que não cancelaria?

### Dados

- Quais informações estão disponíveis no momento em que a previsão precisa ser
  realizada?
- Com qual frequência os dados dos clientes são atualizados?
- Existe histórico suficiente para acompanhar mudanças no comportamento dos
  clientes ao longo do tempo?
- Qual é a qualidade e completude dos dados disponíveis?

### Restrições

- Existem restrições legais ou de privacidade para utilização de dados pessoais?
- Quais dados podem ser utilizados para tomada automatizada de decisão?
- Quais recursos computacionais e de infraestrutura estão disponíveis?
- Qual o prazo esperado para disponibilização da solução?

## 4. Dados e variáveis relevantes

Com base nas informações disponíveis no dataset, as seguintes variáveis serão inicialmente consideradas como potenciais preditores de churn:

### Perfil do cliente
- `Gender`
- `Senior Citizen`
- `Partner`
- `Dependents`

### Relacionamento com a empresa
- `Tenure Months`

### Serviços contratados
- `Phone Service`
- `Multiple Lines`
- `Internet Service`
- `Online Security`
- `Online Backup`
- `Device Protection`
- `Tech Support`
- `Streaming TV`
- `Streaming Movies`

### Contrato e faturamento
- `Contract`
- `Paperless Billing`
- `Payment Method`
- `Monthly Charge`
- `Total Charges`

### Informações geográficas
- `Country`
- `State`
- `City`
- `Zip Code`
- `Latitude`
- `Longitude`

## 5. Envolvimento dos stakeholders

Os principais stakeholders envolvidos no projeto seriam:

- Retention / Customer Success: principal consumidor das previsões e responsável
  pelas ações preventivas direcionadas aos clientes com maior risco de churn;

- Marketing / CRM: responsável por utilizar os segmentos de risco na criação de
  campanhas e ofertas personalizadas;

- Customer Support: pode contribuir com conhecimento sobre os principais problemas
  e reclamações apresentados pelos clientes;

- Data / IT: responsável pela disponibilidade, qualidade e processamento dos dados,
  além da operacionalização da solução;

- Management: responsável por acompanhar os resultados do projeto por meio de
  indicadores como churn rate, retention rate e impacto financeiro.

O envolvimento dessas áreas desde o início é necessário para validar as variáveis
utilizadas, definir os critérios de sucesso e garantir que as previsões produzidas
pelo modelo possam resultar em ações concretas de retenção.