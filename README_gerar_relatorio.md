# Gerador de Relatório Anual - Comissão de Infraestrutura

## Descrição

Script Python que gera automaticamente relatórios anuais da Comissão de Serviços de Infraestrutura (CI) em formato Word (.docx).

O script lê dados da planilha consolidada de votações e cria um documento formatado com tabelas extraídas da aba "Resumo Anual".

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python:
  - `python-docx`
  - `openpyxl`

## Instalação das Dependências

```bash
pip3 install python-docx openpyxl
```

## Uso

### Execução Interativa

Execute o script e digite o ano quando solicitado:

```bash
python3 gerar_relatorio_ci.py
```

O script irá solicitar:
```
Digite o ano do relatório que deseja gerar: 2025
```

### Arquivos Necessários

O script requer os seguintes arquivos na mesma pasta:

1. `relatorio_ci_ano.docx` - Template do relatório
2. `votacoes_ci_consolidadas_[ANO].xlsx` - Planilha com os dados consolidados do ano
   - **Nota:** Se a planilha não existir, o script executará automaticamente `consolidar_votacoes_ci.py` para gerá-la

### Arquivo de Saída

O script gera um arquivo com o nome:
```
relatorio_ci_[ANO].docx
```

Exemplo: `relatorio_ci_2025.docx`

## Funcionalidades

- ✅ Solicita o ano ao usuário
- ✅ Valida se o arquivo Excel do ano existe
- ✅ **Executa automaticamente a consolidação de dados** se a planilha não existir
  - Chama `consolidar_votacoes_ci.py` de forma transparente
  - Aguarda a conclusão da consolidação antes de prosseguir
- ✅ Extrai todas as tabelas da aba "Resumo Anual"
- ✅ Substitui placeholders `{ano}` e `{data atual no formato DD/MM/YYYY}`
- ✅ Formata tabelas com:
  - **Título mesclado** em cada tabela (ex: "REUNIÕES REALIZADAS")
  - **Subtítulos** (cabeçalhos de coluna) em negrito e centralizados
  - **Células de dados** alinhadas à esquerda
  - Sombreamento cinza nos títulos e cabeçalhos
  - Bordas em todas as células
  - Larguras de coluna ajustadas
- ✅ Mantém as notas de rodapé do template
- ✅ Gera tabela customizada de **"EMENDAS AO ORÇAMENTO"** com linhas PLOA e PLDO

## Estrutura das Tabelas

As tabelas são extraídas da aba "Resumo Anual" da planilha Excel e incluem:

1. Reuniões Realizadas
2. Audiências Públicas
3. Sabatinas
4. Projetos Apreciados
5. Requerimentos Apreciados
6. Outras Matérias Apreciadas
7. Emendas ao Orçamento

## Exemplo de Uso

```bash
$ python3 gerar_relatorio_ci.py
============================================================
Gerador de Relatório Anual - Comissão de Infraestrutura
============================================================

Digite o ano do relatório que deseja gerar: 2025

Gerando relatório para o ano 2025...
Lendo dados de: votacoes_ci_consolidadas_2025.xlsx
✓ 7 tabelas extraídas da planilha
✓ Relatório gerado com sucesso: relatorio_ci_2025.docx

============================================================
Processo concluído!
============================================================
```

## Consolidação Automática

Se a planilha `votacoes_ci_consolidadas_[ANO].xlsx` não existir, o script:

1. Detecta automaticamente a ausência do arquivo
2. Informa ao usuário que executará a consolidação
3. Chama o script `consolidar_votacoes_ci.py`
4. Aguarda a conclusão da consolidação
5. Verifica se a planilha foi criada com sucesso
6. Prossegue com a geração do relatório

**Exemplo de saída:**
```
Arquivo de dados não encontrado: votacoes_ci_consolidadas_2025.xlsx
Será necessário executar a consolidação de dados primeiro.

======================================================================
EXECUTANDO CONSOLIDAÇÃO DE DADOS PARA O ANO 2025
======================================================================
...
```

## Tratamento de Erros

O script valida:
- Se o ano inserido é válido (entre 2000 e 2100)
- Se o arquivo Excel do ano existe (ou executa consolidação)
- Se a aba "Resumo Anual" existe na planilha
- Se o template existe
- Se o script de consolidação existe (quando necessário)

## Autor

Script desenvolvido para automatizar a geração de relatórios da CI.
