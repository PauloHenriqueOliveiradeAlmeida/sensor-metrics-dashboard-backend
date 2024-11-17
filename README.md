# 🚨 Sensor Metrics Dashboard

Projeto desenvolvido como atividade avaliativa para matéria de IOT, o projeto consiste em um backend que recebe dados via MQTT, processa-os e os propaga via Websocket aos clientes conectados 

## 📚 Stack usada

![Stack](https://img.shields.io/badge/fastapi-blue?logo=fastapi&logoColor=white&style=for-the-badge) ![Stack](https://img.shields.io/badge/redis-red?logo=redis&logoColor=white&style=for-the-badge)


## 🦾 Funcionalidades

- Recebe dados via MQTT
- Processa os dados, gerando:
  - Desvio padrão
  - Correlação entre demais dados
- Salva os dados em um banco em memória (Redis)


## 🔧 Configuração do projeto
### 🐋 Com Docker Compose
execute o seguinte comando:
```ini
docker-compose up --build
```

### 😥 Sem Docker Compose
#### 📁 Ajustar variáveis de ambiente

Crie um arquivo `.env` na pasta ```api/``` e adicione as variáveis necessárias (há um `.env.example` de demonstração):

```ini
REDIS_HOST=string
REDIS_PORT=integer
REDIS_DB=integer

MQTT_BROKER=string
MQTT_PORT=integer
```

### 🏞️ Criação de um ambiente virtual
Crie um novo ambiente virtual:
```ini
python -m venv .venv

source .venv/bin/activate
```

### 📦 Instalação dos pacotes
Execute a instalação das dependências necessárias:
```ini
pip install --no-cache-dir -r requirements.txt
```

### 🚀 Executando o projeto
Execute o comando de inicialização:
```ini
fastapí run --host 0.0.0.0 --port 8000
```


## 🏃 Testando
Para testar, será necessário utilizar algum cliente como Postman, ou, instalar o frontend e os sensores do projeto:

Frontend: https://github.com/PauloHenriqueOliveiradeAlmeida/sensor-metrics-dashboard-web

Sensores: https://github.com/PauloHenriqueOliveiradeAlmeida/sensor-metrics-sensors
