# BɅSTICOᴮᵀ

> **Knowledge. Refined.**  
> Manifesto e Governança · Versão 1.0.0

---

## 1. Identidade Canônica

A grafia oficial, canônica e imutável do projeto é **BɅSTICOᴮᵀ**.

O sobrescrito **ᴮᵀ** constitui o selo oficial e o prefixo obrigatório de todo e qualquer módulo funcional desenvolvido sob este ecossistema (ex: `ᴮᵀObserve`). A consistência terminológica e ortográfica entre documentação, código-fonte, logs e mensagens de commit é um requisito de engenharia inegociável para a preservação do conhecimento.

## 2. Princípios de Engenharia

Para garantir que o sistema permaneça leve, simples e estritamente objetivo, toda decisão técnica deve se submeter aos seguintes pilares filosóficos:

* **Pragmatismo sobre Burocracia:** A documentação existe para clareza técnica e alinhamento conceitual. Rejeita-se a proliferação de arquivos vazios ou redundantes.
* **Baixo Acoplamento e Alta Coesão:** Cada módulo resolve um problema único e bem delimitado da jornada do conhecimento.
* **Isolamento de Efeitos Colaterais:** Módulos de leitura pura (como o `ᴮᵀObserve`) são isolados de operações de escrita ou mutação de dados.
* **Evolução Incremental:** Não projetamos arquiteturas complexas para o futuro se elas bloquearem a utilidade do sistema hoje. O foco é entregar software funcional a cada ciclo.

## 3. Atmosfera

A identidade do **BɅSTICOᴮᵀ** transmite precisão, permanência e silêncio. A estética do projeto não nasce da ornamentação visual, mas da clareza e do ritmo editorial do texto puro.

O BɅSTICOᴮᵀ não parece vir do futuro.  
Parece ter sido descoberto no futuro.

## 4. Regras de Governança e Fluxo Git

O projeto adota um fluxo Git focado em pacotes coerentes de entrega para manter a rastreabilidade das decisões:

1. **Veto a Commits Caóticos:** Não são permitidos commits isolados ou desorganizados de arquivos individuais diretamente na branch principal, exceto durante a inicialização do Cycle 000.
2. **O Ciclo de Entrega:** O desenvolvimento de qualquer funcionalidade segue rigorosamente o fluxo: Desenvolvimento em branch local $\rightarrow$ Revisão do conjunto de artefatos $\rightarrow$ Abertura de Pull Request (PR) $\rightarrow$ Merge.
3. **Casos de ADR:** Decisões que alterem profundamente as regras deste manifesto ou modifiquem a estrutura física plana do repositório exigiriam a criação de um novo registro formal na pasta `docs/adr/`.
