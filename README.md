# Projeto em Python/Django totalmente encapsulado em dev container

Este projeto é a aula 1 de Caio Sampaio PyStack Week 7.0 realizado em Julho de 2023.

A ideia é usar esse template para criar novos projetos Python em containers. A ênfase aqui é desenvolvimento em container e não produção. No entanto, com pequenas configurações esse projeto pode ser usado para ambientes de produção. Vale o exercício para casa.

## Requisitos

### Docker

Para rodar esse projeto é preciso ter o Docker instalado em seu computador. Para MacOS e Linux é só instalar o Docker. Para Windows, só a partir do Windows 10. Instale o WSL e o sabor de Linux que mais lhe agrada. Em seguida instale o Docker Desktop

### VSCode

Embora não seja requisito, facilita muito usar o VSCode para rodar o dev container. Para maiores informações veja (esse excelente tutorial)[https://code.visualstudio.com/docs/devcontainers/containers]

### Github

Obviamente, é preciso clonar o repo no computador local e abrir o diretório com o VSCode.

## Como usar

- Certifique-se que o Docker está ativado.
- Abra o VSCode na pasta/diretório/folder que contém o repositório em sua máquina.
- O VSCode perguntará se é para abrir o projeto no dev container. Responda que sim e aguarde ele montar o - ambiente. A primeira vez pode demorar um pouquinho.
- Prefira abrir o terminal DENTRO do VSCode. Assim você certifica-se que está dentro do ambiente virtual criado para desenvolvimento. Se abrir o terminal fora do VSCode ainda é possível acessar o ambiente virtual mas não é tão direto. Vide o tutorial mencionado acima.

## Vantagens de desenvolver em Docker

A principal vantagem é que o ambiente de desenvolvimento pode ser configurado com muito mais rigor, evitando conflitos e incompatibilidades na hora de desenvolver. É como se para cada novo projeto fosse utilizado um computador recém configurado portanto o isolamento do ambiente facilita o diagnóstico de eventuais conflitos.

Existem outras vantagens, por exemplo, o ambiente de desenvolvimento pode ser levado para qualquer computador rapidamente. Todas as configurações do ambiente (softwares e libs que devem ser pre-instaladas) ficam sob controle do gerenciador de versões, Github. Assim, compartilha-se o ambiente rapidamente entre vários membros da equipe.





