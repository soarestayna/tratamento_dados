# Tratamento de Dados

Este repositório faz parte do meu portfólio acadêmico desenvolvido durante o
curso de **Análise de Dados – EBAC**.  
Aqui estão reunidos notebooks que exploram técnicas de **limpeza, 
padronização, correção e validação de dados**, fundamentais para garantir a 
qualidade das análises e modelos preditivos.

---

## Objetivo

Demonstrar o uso de ferramentas Python para tratar dados reais e simulados,
aplicando boas práticas de pré-processamento.  
Cada notebook documenta uma etapa do processo de tratamento, 
com foco em clareza, reprodutibilidade e aprendizado técnico.

---

## Conteúdo dos Notebooks

### 1. **Análise Exploratória Inicial**

- Leitura e inspeção do dataset
- Verificação de tipos, estrutura e valores nulos
- Identificação de problemas básicos

### 2. **Limpeza de Dados**

- Remoção de colunas e linhas irrelevantes
- Normalização de texto (maiúsculas, minúsculas, espaços)
- Conversão de tipos e tratamento de nulos
- Seleção de colunas relevantes

### 3. **Remoção de Outliers**

- Detecção com Z-score e IQR
- Aplicação de limites de faixa
- Validação de campos como endereço e nome
- Exportação dos dados limpos

### 4. **Tratamento Avançado**

- Mascaramento de dados pessoais (CPF)
- Correção de datas e cálculo de idade ajustada
- Extração de informações de campos compostos (endereço, bairro, estado)
- Validação de formatos e consistência semântica

---

## 📜 Scripts Python

Além dos notebooks interativos, este repositório inclui scripts `.py` que replicam as etapas de tratamento de dados de forma automatizada.

Esses scripts são úteis para:

- Executar o pré-processamento em ambientes fora do Jupyter
- Integrar o tratamento de dados em pipelines ou aplicações
- Reutilizar funções e lógicas de limpeza com maior eficiência

Scripts disponíveis:

- `1_tratamento_dados.py` – leitura e inspeção inicial  
- `2_limpeza_dados.py` – limpeza e padronização  
- `3_outliers.py` – detecção e remoção de outliers  
- `4_inconsistencias.py` – validação e enriquecimento dos dados  
- `estudos_lambda.py` – experimentos com funções lambda

---

## Componentes do Projeto

- `pandas` – manipulação de dados tabulares  
- `numpy` – operações numéricas e tratamento de nulos  
- `scipy.stats` – detecção estatística de outliers  
- `pathlib` – gerenciamento de caminhos de arquivos

---

## Aprendizados

- O tratamento de dados é uma etapa estratégica que afeta diretamente a 
qualidade das análises.
- Cada decisão de remover, preencher ou transformar deve considera o 
- contexto e os objetivos do projeto.
- Automatizar o pré-processamento com código limpo e documentado 
facilita a escalabilidade e a colaboração.

---

## Como usar este repositório

Todos os notebooks estão organizados por módulo e podem ser executados 
individualmente em ambiente Jupyter.  
Os arquivos `.csv` gerados estão incluídos ou podem ser
reproduzidos com os scripts disponíveis.

---

## Sobre mim

Sou estudante de Análise de Dados e este módulo faz parte da minha jornada de aprendizado técnico e prático.  
Cada notebook foi construído com dedicação e foco para transformar os 
dados em conhecimento.
