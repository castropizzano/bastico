# BɅSTICOᴮᵀ

> **Knowledge. Refined.**  
> Especificação Funcional · Módulo de Quarentena · Versão 1.0.0

---

## 1. Objetivo do Módulo

Este módulo consome um *Inventory* já consolidado pelo `ᴮᵀObserve` e resolve grupos de *Artifacts* que compartilham a mesma *Fingerprint*, isolando as redundâncias em um diretório de quarentena físico, sem exclusão definitiva.

## 2. Restrições de Engenharia (Inegociáveis)

* **Soft Delete Obrigatório:** é proibida a exclusão permanente de qualquer *Artifact* pela interface. A única ação destrutiva permitida é o deslocamento físico do arquivo para o diretório de quarentena.
* **Determinismo do Agrupamento:** dentro de um grupo de *Fingerprint* idêntica, os *Artifacts* devem ser ordenados de forma determinística por `path` (ordem lexicográfica) antes de qualquer rotulagem. O primeiro item da lista ordenada é rotulado como **Referência**; os demais como **Redundância**.
  * Esse rótulo **não é uma afirmação de originalidade cronológica real** — é apenas um critério estável e reproduzível de desempate, necessário para satisfazer a Idempotência exigida pelo `SPEC_OBSERVE.md` (seção 2). O módulo não infere qual arquivo foi criado primeiro.
* **Localização da Quarentena:** o diretório de quarentena é criado como **irmão** do `corpus_path` (mesmo nível hierárquico, fora do Corpus), nunca aninhado dentro dele. Isso evita que artifacts isolados sejam re-mapeados como parte do Corpus em um novo ciclo de `ᴮᵀObserve`.
* **Isolamento Granular:** falha ao mover um *Artifact* individual não deve interromper o isolamento dos demais itens do mesmo grupo. Cada movimentação é uma operação independente, com resultado (sucesso/falha) reportado item a item.
* **Idempotência da Ação:** isolar o mesmo grupo de duplicatas duas vezes não deve gerar erro nem duplicar cópias na quarentena; a segunda tentativa deve reconhecer que o item já não está mais no Corpus.

## 3. Fluxo de Execução Prática

```text
[ Entrada: Inventory.json consolidado ]
                  │
                  ▼
     1. Agrupamento por Fingerprint
                  │
                  ▼
  2. Ordenação determinística (path) dentro do grupo
                  │
                  ▼
     3. Rotulagem: Referência (1º) / Redundância (demais)
                  │
                  ▼
   4. Ação do usuário: Isolar Redundâncias (por item)
                  │
                  ▼
[ Saída: Redundâncias movidas para quarentena, Referência preservada no Corpus ]
```

## 4. Fora de Escopo (Versão 1.0.0)

* Exclusão definitiva de arquivos da quarentena (ato manual do usuário, fora da aplicação).
* Inferência de originalidade real por metadados de data de criação/modificação (candidato a versão futura, dependente de extensão do `SPEC_OBSERVE.md`).
* Desfazer (undo) automático de uma ação de isolamento.

---

```text
BɅSTICOᴮᵀ // DOC_REF: docs/SPEC_QUARANTINE.md // VERSION: 1.0.0 // STATUS: STABLE
```
