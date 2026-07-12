# Manifesto e Governança: BɅSTICOᴮᵀ

## 1. Identidade Canônica

[cite_start]A grafia oficial, canônica e imutável do projeto é **BɅSTICOᴮᵀ** [cite: 767-768].

[cite_start]O sobrescrito **ᴮᵀ** constitui o selo oficial e o prefixo obrigatório de todo e qualquer módulo funcional desenvolvido sob este ecossistema (ex: `ᴮᵀObserve`) [cite: 117-118, 209]. [cite_start]A consistência terminológica e ortográfica entre documentação, código-fonte, logs e mensagens de commit é um requisito de engenharia inegociável para a preservação do conhecimento [cite: 537-538, 615-616].

## 2. Princípios de Engenharia

Para garantir que o sistema permaneça leve, simples e estritamente objetivo, toda decisão técnica deve se submeter aos seguintes pilares filosóficos:

* [cite_start]**Pragmatismo sobre Burocracia:** A documentação existe para clareza técnica e alinhamento conceitual [cite: 535, 818-819]. Rejeita-se a proliferação de arquivos vazios ou redundantes.
* [cite_start]**Baixo Acoplamento e Alta Coesão:** Cada módulo resolve um problema único e bem delimitado da jornada do conhecimento [cite: 541-542].
* [cite_start]**Isolamento de Efeitos Colaterais:** Módulos de leitura pura (como o `ᴮᵀObserve`) são isolados de operações de escrita ou mutação de dados [cite: 37, 846-847].
* [cite_start]**Evolução Incremental:** Não projetamos arquiteturas complexas para o futuro se elas bloquearem a utilidade do sistema hoje[cite: 540, 602]. O foco é entregar software funcional a cada ciclo.

## 3. Atmosfera

A identidade do **BɅSTICOᴮᵀ** transmite precisão, permanência e silêncio. A estética do projeto não nasce da ornamentação visual, mas da clareza e do ritmo editorial do texto puro.

O BɅSTICOᴮᵀ não parece vir do futuro.  
Parece ter sido descoberto no futuro.

## 4. Regras de Governança e Fluxo Git

[cite_start]O projeto adota um fluxo Git focado em pacotes coerentes de entrega para manter a rastreabilidade das decisões [cite: 539, 761-762]:

1. **Veto a Commits Caóticos:** Não são permitidos commits isolados ou desorganizados de arquivos individuais diretamente na branch principal, exceto durante a inicialização do Cycle 000.
2. [cite_start]**O Ciclo de Entrega:** O desenvolvimento de qualquer funcionalidade segue rigorosamente o fluxo: Desenvolvimento em branch local $\rightarrow$ Revisão do conjunto de artefatos $\rightarrow$ Abertura de Pull Request (PR) $\rightarrow$ Merge [cite: 43-45, 761-762].
3. [cite_start]**Casos de ADR:** Decisões que alterem profundamente as regras deste manifesto ou modifiquem a estrutura física plana do repositório exigem a criação de um novo registro formal na pasta `docs/adr/` [cite: 567, 619-620].
