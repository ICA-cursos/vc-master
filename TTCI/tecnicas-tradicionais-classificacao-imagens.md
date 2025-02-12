# Projetos de Visão Computacional da disciplina de TTCI - Técnicas Tradicionais de Classificação de Imagens

Este repositório contém diversos projetos desenvolvidos em aula com os alunos do curso VC MASTER - ICA - PUC-Rio. Cada projeto apresenta diferentes técnicas e abordagens para soluções em Machine Learning Clássico aplicadas à Visão Computacional.

## Índice

1. [Classificação de Dígitos Manuscritos com SVM](#classificacao-de-digitos-manuscritos-com-svm)
2. [Classificação de Peças de Vestuário com KNN (Deploy com FastAPI)](#classificacao-de-pecas-de-vestuario-com-knn)
3. [Classificação de Imagens CIFAR-10 (Otimização de Hiperparâmetros com Optuna)](#classificacao-de-imagens-cifar-10)
4. [Classificação de Cães e Gatos - Desafio no Kaggle](#classificacao-de-caes-e-gatos)
5. [Análise de Eletrocardiogramas (ECG) com GAF](#analise-de-eletrocardiogramas-ecg-com-gaf)
6. [Classificação de Características Faciais (Multilabel)](#classificacao-de-caracteristicas-faciais)
7. [Detecção de Anomalias em Peças de Metal](#deteccao-de-anomalias-em-pecas-de-metal)

---

## Classificação de Dígitos Manuscritos com SVM

Este projeto utiliza **Support Vector Machines (SVM)** para classificar dígitos manuscritos de 0 a 9 com base no famoso dataset MNIST.

**Técnicas aplicadas:**

- Extração de features
- Normalização dos dados
- Treinamento e avaliação do modelo



---

## Classificação de Peças de Vestuário com KNN

Neste projeto, utilizamos o **Fashion-MNIST** e um classificador **K-Nearest Neighbors (KNN)** para categorizar diferentes peças de roupa. O modelo foi implantado via **API FastAPI** para uso em produção.

**Destaques:**

- Implementação de API para inferência em tempo real
- Normalização e transformação dos dados
- Treinamento e avaliação com validação cruzada



---

## Classificação de Imagens CIFAR-10 (Otimização de Hiperparâmetros com Optuna)

O projeto utiliza a base de dados **CIFAR-10**, contendo imagens coloridas de 10 classes diferentes, e aplica otimização de hiperparâmetros com **Optuna** para melhorar o desempenho do modelo.

**Técnicas aplicadas:**

- Treinamento de CNNs (Redes Neurais Convolucionais)
- Otimização de hiperparâmetros com Optuna
- Avaliação detalhada de métricas de desempenho



---

## Classificação de Cães e Gatos

Utilizando um dataset de imagens de cães e gatos, este projeto visa construir um modelo de classificação para distinguir entre as duas categorias.

**Abordagem:**

- Uso de HOG para extração de features
- Treinamento supervisionado
- Árvores de Decisão e Random Forest



---

## Análise de Eletrocardiogramas (ECG) com GAF

Este projeto foca na conversão de séries temporais de eletrocardiogramas (ECG) em imagens usando **Gramian Angular Field (GAF)**, permitindo classificação de batimentos normais e infarto do miocárdio.

**Técnicas aplicadas:**

- Conversão de sinais temporais para imagens
- Classificação de Infarto ou Batimentos Cardíacos Normais
- Processamento de séries temporais



---

## Classificação de Características Faciais (Multilabel)

Este projeto utiliza a base de dados **CelebA**, contendo imagens de rostos humanos anotadas com diversas características faciais (ex: óculos, barba, sorriso). O modelo foi treinado para classificação **multilabel**.

**Destaques:**

- Extração e processamento de atributos faciais
- Análise de desempenho por atributo



---

## Detecção de Anomalias em Peças de Metal

Neste projeto, aplicamos técnicas de Visão Computacional para identificar defeitos de manufatura em peças de metal, utilizando aprendizado supervisionado e métodos de detecção de anomalias.

**Abordagem:**

- Extração de features
- Detecção de anomalias por ML clássico



---

Este repositório é atualizado periodicamente com novos projetos e melhorias. Sinta-se à vontade para explorar e contribuir!


