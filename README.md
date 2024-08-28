# <center> Coleta de Preço de Ações na Bolsa de Valores via Yahoo Finance </center>

<div style="text-align: center;">
    <img src = "https://lh3.googleusercontent.com/pw/AP1GczMxJVr2aLXf4duL70EG377ygdTF9JRJUVSBGaiOZW6nmLqCXIE-_NgRTORgmrLRIYvsZeM89poqgiJt9dh9OljgaTGh2LCMJRLQRE0nsGW6LXwAsu70IdxQiE2J4L_vZ_8yMUFdZLXyxqU4CMyp76zJ=w748-h601-s-no-gm?authuser=0" alt = "Exemplo da página da aplicação" />
</div>

Este projeto tem por finalidade disponibilizar uma aplicação na web via [`streamlit`](https://streamlit.io/) e [`yfinance`](https://finance.yahoo.com/) que informa o valor da ação desejada e os dividendos pagos.
Atualmente a imagem do docker está hospedada em um servidor do [Render](render.com) com a conta github conectada - isso facilita pois quaisquer alterações que sejam feitas no repositório, o Render irá atualizar no arquivo da aplicação.

Para replicar este projeto será necessário: 

1. Clonar o repositório na máquina de destino pelo comando: 
```
# Clonando via SSH
git clone git@github.com:renanmarxx/Coleta-Preco-Acoes.git
```

2. Construir a imagem docker do projeto e instalando suas dependências:
```
# Construindo imagem docker do projeto
docker build -t nome-da-imagem-desejado
```

3. Executar a imagem criada no passo anterior em um container local ou hospedar em algum servidor/máquina como EC2 da AWS:
```
# Executar a imagem em um container local
docker run -d -p 8501:8501 --name nome-do-container-desejado nome-da-imagem-criada
```