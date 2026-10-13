
# SCIC — Sistema de Comunicação Interplanetária da Colônia

**Aurora Siger · Projeto Integrador 2026**

O **SCIC (Sistema de Comunicação Interplanetária da Colônia)** é um projeto integrador desenvolvido para simular, monitorar e otimizar a gestão operacional de comunicações e telemetria da colônia espacial Aurora Siger.

Em um ambiente espacial isolado, os enlaces de transmissão enfrentam latências variáveis, limitações energéticas e riscos de falhas críticas. Para enfrentar esses desafios, o sistema utiliza análise estatística, modelagem preditiva e estruturas de dados avançadas para auxiliar no monitoramento e na tomada de decisões operacionais.

##  Funcionalidades Principais

-  **Gestão de Dados Operacionais:** processamento e análise de dados utilizando Pandas e NumPy.
-  **Cálculos Elétricos:** cálculo da potência elétrica a partir da tensão e da corrente.
-  **Análise de Erros Numéricos:** cálculo dos erros absoluto e relativo entre as latências observadas e previstas.
-  **Modelo Preditivo:** utilização de regressão linear com Scikit-Learn para estimar latências e avaliar previsões.
-  **Métricas de Avaliação:** análise do modelo por meio de MAE, MSE, RMSE e R².
-  **Fila de Prioridades (Min-Heap):** organização de alertas conforme seus níveis de prioridade.
-  **Busca por Prefixos (Trie):** pesquisa de registros por nomes de módulos e códigos de dispositivos.
-  **Interface via Terminal (CLI):** menu interativo para acessar as funcionalidades do sistema.

##  Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

##  Estrutura do Repositório

```text
SCIC/
├── Código-Fonte Principal.py
├── Relatório.pdf
├── dados_aurora_siger.csv
├── README.md
└── LICENSE
```

##  Requisitos

Antes de executar o projeto, certifique-se de possuir:

- Python 3.8 ou superior;
- pip para instalação das dependências;
- Git para clonar o repositório.

##  Instalação

**1. Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

**2. Acesse a pasta do projeto:**

```bash
cd seu-repositorio
```

**3. Instale as dependências:**

```bash
pip install numpy pandas scikit-learn
```

**4. Verifique os arquivos:**

Certifique-se de que o arquivo `dados_aurora_siger.csv` esteja no local esperado pelo código-fonte.

##  Como Executar

Execute o programa pelo terminal:

```bash
python "Código-Fonte Principal.py"
```

Após iniciar a aplicação, utilize o menu interativo e selecione uma das opções disponíveis, de 1 a 6.

##  Estrutura da Base de Dados

O arquivo `dados_aurora_siger.csv` contém dados simulados de telemetria utilizados nas análises do sistema.

| Coluna | Descrição |
|---|---|
| `nome_modulo` | Nome ou identificador do módulo |
| `tipo_modulo` | Categoria funcional do módulo |
| `latencia_observada_ms` | Latência observada em milissegundos |
| `latencia_prevista_ms` | Latência prevista em milissegundos |
| `tensao_v` | Tensão elétrica em volts |
| `corrente_a` | Corrente elétrica em ampères |
| `status_operacional` | Estado operacional do módulo |
| `nivel_prioridade` | Nível numérico de prioridade do alerta |
| `mensagem_alerta` | Descrição do alerta ou incidente |
| `codigo_dispositivo` | Identificador do dispositivo ou sensor |

##  Cálculos e Métricas

**Potência elétrica:**

P = V × I

**Erro absoluto:**

E_abs = |latência observada − latência prevista|

**Erro relativo:**

E_rel = E_abs / |latência observada|

O erro relativo deve ser tratado separadamente quando a latência observada for igual a zero.

O modelo preditivo utiliza as seguintes métricas de avaliação:

- **MAE:** erro absoluto médio.
- **MSE:** erro quadrático médio.
- **RMSE:** raiz do erro quadrático médio.
- **R²:** coeficiente de determinação.

##  Sustentabilidade e Responsabilidade Humana

O SCIC foi desenvolvido considerando a eficiência energética, a segurança operacional e a responsabilidade humana.

- **Eficiência energética:** análise do consumo elétrico para auxiliar na identificação de oportunidades de otimização.
- **Monitoramento:** identificação de possíveis falhas e situações críticas.
- **Priorização:** organização de alertas conforme a urgência dos incidentes.
- **Decisão humana:** utilização dos resultados como apoio à tomada de decisão, preservando a responsabilidade humana.

##  Objetivo do Projeto

Desenvolver um protótipo capaz de organizar dados operacionais, analisar indicadores de comunicação e consumo elétrico, avaliar previsões de latência e priorizar alertas utilizando estruturas de dados e técnicas de aprendizado de máquina.

##  Licença

Este projeto utiliza a licença MIT, desde que o arquivo `LICENSE` correspondente esteja incluído no repositório.

Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.

---

**Desenvolvido como parte do Projeto Integrador Aurora Siger — 2026.** 🚀
