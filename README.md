# <center> Coleta de Preço de Ações na Bolsa de Valores via Yahoo Finance </center>

<div style="text-align: center;">
    <img src = "https://lh3.googleusercontent.com/pw/AP1GczMxJVr2aLXf4duL70EG377ygdTF9JRJUVSBGaiOZW6nmLqCXIE-_NgRTORgmrLRIYvsZeM89poqgiJt9dh9OljgaTGh2LCMJRLQRE0nsGW6LXwAsu70IdxQiE2J4L_vZ_8yMUFdZLXyxqU4CMyp76zJ=w748-h601-s-no-gm?authuser=0" alt = "Exemplo da página da aplicação" />
</div>

Este projeto tem por finalidade disponibilizar uma aplicação *`python`* na web via [`streamlit`](https://streamlit.io/) e [`yfinance`](https://finance.yahoo.com/) que informa o valor da ação desejada e os dividendos pagos.
Atualmente a imagem do docker está hospedada em um servidor do [Render](https://render.com/) com a conta github conectada - isso facilita pois quaisquer alterações que sejam feitas no repositório, o Render irá atualizar no arquivo da aplicação.

A aplicação está hospedada neste link: [https://coleta-preco-acoes.onrender.com/](https://coleta-preco-acoes.onrender.com/)

O projeto foi desenvolvido na versão do `python 3.12.5` - vide arquivo `.python-version`. Para replicar este projeto será necessário: 

<<<<<<< HEAD
1. Instalar algumas bibliotecas e configurar o ambiente virtual para execução e desenvolvimentos - utilizando algum terminal, como o CMD ou Git Bash: 

```
Instalando Bibliotecas


# pyenv - dependendo do sistema operacional (Mac/Linux/Windows) o processo será diferente. O modo a seguir serve para instalação no Windows via PowerShell:

Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"


# pipx
pip install pipx


# poetry
pipx install poetry
```

```
Configurando ambiente virtual

pipx ensure path
poetry config virtualenvs.in-project true
poetry new coleta-preco-acoes
pyenv local 3.12.5
poetry env use 3.12.5
```

2. Clonar o repositório na máquina de destino pelo comando: 
=======
1. Clonar o repositório no diretório de destino da máquina pelo comando: 
>>>>>>> 7d1aeb0dac1c7734b151d478c35aadd4b88dd775
```
# Clonando via SSH
git clone git@github.com:renanmarxx/Coleta-Preco-Acoes.git
```

3. Construir a imagem docker do projeto e instalando suas dependências:
```
# Construindo imagem docker do projeto
docker build -t nome-da-imagem-desejado
```

4. Executar a imagem criada no passo anterior em um container local ou hospedar em algum servidor/máquina como EC2 da AWS:
```
# Executar a imagem em um container local
docker run -d -p 8501:8501 --name nome-do-container-desejado nome-da-imagem-criada
```
