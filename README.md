# Avaliação Sprint 4-5 -> Programa de Bolsas Compass UOL / AWS - ABRIL/2024

<p align="center">
 <a href="#-descrição">Descrição</a>  •
 <a href="#-funcionalidades">Funcionalidades</a>  • 
 <a href="#-como-usar-a-aplicação">Como usar</a>  • 
 <a href="#-desenvolvimento">Desenvolvimento</a>  • 
 <a href="#-execução">Execução</a>  • 
  <a href="#-arquitetura-aws">Arquitetura AWS</a>  •
 <a href="#-dificuldades">Dificuldades</a>  •
 <a href="#-autores">Autores</a> 
</p>

## 📜 Descrição

Projeto tem como objetivo classificar reservas de hotel com base na faixa de preço por quarto utilizando AWS SageMaker para treinamento de modelo, AWS RDS para armazenamento de dados, e FastAPI para exposição de uma API de predição. O projeto é containerizado utilizando Docker.

## ✅ Funcionalidades

Este projeto possui diversas funcionalidades importantes, que permitem a classificação de reservas de hotel com base em faixas de preço por quarto, utilizando um modelo de machine learning treinado no AWS SageMaker. Aqui estão as principais funcionalidades:

**1. Carregamento e Preparação dos Dados**

- Notebooks Jupyter: Utilizamos notebooks para carregar, explorar e preparar os dados. Isso inclui limpeza dos dados, criação de novas features e armazenamento dos dados processados no AWS S3 e AWS RDS.
- Interação com RDS: Conexão ao banco de dados relacional (RDS) da AWS para executar consultas SQL e manipular os dados diretamente.

**2. Treinamento do Modelo**

- AWS SageMaker: Utilizamos o AWS SageMaker para treinar um modelo de machine learning. O modelo é treinado utilizando dados armazenados no S3 e a configuração do treinamento é feita nos notebooks.
- Modelo Random Forest: Escolha do algoritmo Random Forest devido à sua robustez e alta performance em tarefas de classificação.

**3. Desenvolvimento da API**

**FastAPI**
- Desenvolvemos uma API utilizando o framework FastAPI, que oferece uma interface RESTful para realizar predições. A API é configurada para carregar o modelo treinado a partir do S3.

**4. Containerização**

- Docker: Utilização do Docker para containerizar a aplicação, garantindo que o ambiente de execução seja consistente em diferentes máquinas.

**5. Deploy na AWS**
- EC2: A aplicação pode ser implantada na AWS usando Amazon ECS, EKS ou instâncias EC2. O uso de containers Docker facilita o deploy e a escalabilidade da aplicação.
- AWS S3: O modelo treinado e os dados são armazenados no Amazon S3, permitindo fácil acesso e gerenciamento.

**Endpoint**
- /api/v1/predict: Endpoint POST que recebe um JSON com os dados da reserva e retorna a classificação (faixa de preço).
- /: Endpoint GET que retorna uma mensagem de boas-vindas.


## 🧑‍💻 Como usar a Aplicação


## 🚀 Desenvolvimento
**📂 Estrutura de pastas**

 ```
├── src
│   ├── Api
│   │   ├── Controllers                         
│   │   │   ├── home_controller.py                # Controlador para a rota principal da API, respondendo com uma mensagem de boas-vindas.
│   │   │   └── prediction_controller.py          # Controlador para a rota de predição, gerenciando a lógica de receber dados de entrada e retornar a predição.
│   │   ├── Models
│   │   │   └── prediction_model.py               # Modelo de dados utilizado na API, definindo a estrutura dos dados de entrada para a predição.
│   │   ├── Service                                
│   │   │   └── prediction_service                # Serviço para carregar o modelo treinado do S3 e realizar predições.
│   │   ├── main.py                               # Ponto de entrada da aplicação FastAPI
│   │   ├── requeriments.txt                      # Lista de dependências do Python.
│   │   └── Dockerfile                            # Configuração do Docker
│   ├── Notebooks
│   │   ├── Treinamento                             
│   │   │   └── notebooks.ipynb                   # Notebooks Jupyter para desenvolvimento e treinamento dos dados
│   │   ├── AWS
│   │   │   └── rds.ipynb                         # Notebook para interação com RDS, incluindo conexão ao banco de dados, execução de consultas SQL e carregamento dos dados.
│   │   └── requeriments.txt                      # Lista de dependências do Python.



 ```
**⚙️ Tecnologias Utilizadas**
- Python: Linguagem de programação principal.
- FastAPI: Framework para desenvolvimento da API.
- AWS SageMaker: Serviço da AWS para treinamento e deploy de modelos de machine learning.
- AWS S3: Armazenamento de dados e modelos.
- AWS RDS: Banco de dados relacional para armazenamento dos dados.
- Docker: Ferramenta de containerização.

## 💻 Execução

**Pré-requisitos** : 
- `Conta na AWS com permissões para SageMaker, S3, e RDS`
- `Docker`
- `Python 3.9 ou superior`
- `Jupyter Notebook`


## 🌐 Arquitetura AWS
A arquitetura AWS deste projeto integra vários serviços da AWS para criar uma solução de machine learning e predição. A utilização de SageMaker, S3, RDS, FastAPI, Docker e EC2 permite que a aplicação seja escalável, eficiente e fácil de gerenciar. Cada componente foi escolhido para otimizar o desempenho e a escalabilidade, garantindo que o sistema possa lidar com grandes volumes de dados e fornecer predições em tempo real.



## 🔐 Dificuldades

- Tivemos uma dificuldade relacionada ao treinamento do sagemaker, encontramos um erro ao tentar ajustar o estimador em apenas uma das maquinas locais utilizadas e que gerou um bom tempo para o entedimento do mesmo e a descoberta para a solução.


## 👤 Autores
- [Gabriel Venancio de Avelar](https://github.com/GabrielAvelarbr) | Email: 99gabrielavelar@gmail.com |
- [Layon Jose Pedrosa dos Reis](https://github.com/Layonj3000) | Email: layonjp300@gmail.com |
- [Leonardo Loureiro de Almeida](https://github.com/lloureiro2) | Email: leoloureiro44@gmail.com |

