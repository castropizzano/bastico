# BɅSTICOᴮᵀ

> **Knowledge. Refined.**  
> Ontologia e Léxico · Versão 1.2.0

---

## 1. Glossário de Conceitos Core

As entidades fundamentais do sistema definem o modelo de dados estável do projeto. A terminologia descrita abaixo deve ser adotada de forma idêntica no código-fonte.

* **Corpus:** O diretório ou volume delimitado de arquivos de origem que o sistema analisa. É uma entidade passiva e restrita estritamente a operações de leitura (read-only).
* **Artifact:** Qualquer arquivo individual, isolado e identificável localizado dentro de um *Corpus*. Possui propriedades inerentes como caminho, tamanho e extensão.
* **Fingerprint:** O hash criptográfico (SHA-256) gerado a partir do conteúdo binário exato de um *Artifact*, garantindo sua identificação única.
* **Metadata:** O conjunto de informações estruturadas e atributos técnicos extraídos do *Artifact*.
* **Inventory:** O artefato de saída consolidado (obrigatoriamente estruturado em formato **JSON**) que mapeia todos os *Artifacts* de um *Corpus*, vinculando suas respectivas *Fingerprints* e *Metadata*.
* **Quarentena:** O diretório físico, externo ao *Corpus*, destinado ao isolamento não-destrutivo (*soft delete*) de *Artifacts* redundantes identificados a partir do *Inventory*.
* **Referência:** Dentro de um grupo de *Artifacts* com *Fingerprint* idêntica, o item selecionado por critério determinístico (ordenação lexicográfica de path) para permanecer no *Corpus*.
* **Redundância:** Dentro de um grupo de *Artifacts* com *Fingerprint* idêntica, qualquer item que não seja a *Referência*, elegível para isolamento em *Quarentena*.

## 2. Regras de Consistência Semântica

* Um *Corpus* abriga zero ou mais *Artifacts*.
* Cada *Artifact* gera obrigatoriamente uma única *Fingerprint*.
* O módulo `ᴮᵀObserve` lê um *Corpus* para estruturar ou atualizar um *Inventory*, operando sob proibição absoluta de modificar qualquer propriedade física dos arquivos de origem.
* Um grupo de *Artifacts* que compartilham a mesma *Fingerprint* produz exatamente uma *Referência* e zero ou mais *Redundâncias*.

## 3. Diretrizes Léxicas de Desenvolvimento

Fica proibida a utilização de sinônimos arbitrários no código ou nos documentos técnicos.

| Termo Proibido | Termo Canônico Obrigatório |
| :--- | :--- |
| Arquivo / Item | Artifact |
| Pasta / Diretório | Corpus |
| Hash / Código | Fingerprint |
| Dados / Propriedades | Metadata |
| Relatório / Lista | Inventory |
| Lixeira / Backup | Quarentena |
| Original | Referência |
| Cópia / Duplicata | Redundância |

---

```text
BɅSTICOᴮᵀ // DOC_REF: docs/ONTOLOGY.md // VERSION: 1.2.0 // STATUS: STABLE
```
