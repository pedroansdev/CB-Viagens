# Resultado - Desafio CoorLab

## Backend

### Tecnologias

- Flask
- Flask-cors

Para o backend, a implementação foi simples. <br>
Utilizei o `flask` para o gerenciamento das rotas da api criada, configurando no próprio arquivo `app.py` a porta que a api deveria funcionar, no caso, a `porta 3000.` <br>
Utilizei o `flask-cors` para determinar que requisições de qualquer origem sejam aceitas, assim possibilitando a comunicação do frontend com a api no backend.

## Frontend

### Tecnologias

- Vue
- Vite
- Axios
- Tailwind CSS

Para o frontend, a implementação já precisou de mais tecnologias. <br>
Começando pelo `Vue`, ele foi o FrameWork que utilizei para a construção das interfaces do projeto, nele utilizei sua função `ref` para criação de componentes reativos. <br>
Já o `Vite`, foi a tecnologia utilizada como servidor do ambiente de desenvolvimento, que inclusive, foi no arquivo de configuração do vite (o `vite.config.js`), que eu defini a porta que ele usaria para rodar o servidor frontend, no caso, a `porta 8080`. <br>
O `Axios`, uma biblioteca JavaScript, foi a tecnologia que utilizei para fazer as `requisições` ao servidor da api, usando como link base da configuração do axios, o `localhost:3000/api`, que é a parte do link que eu usaria em todas as minhas requisições, sendo assim, no `axios.get`, eu apenas passava a cidade que eu desejava, como sp, rj ou bh. Para a configuração do link base do axios, utilizei o arquivo `.env` para que assim, caso tenham vários ambientes, como ambientes de desenvolvimento ou produção, caso necessário, só precisa mexer no arquivo `.env` e não no código em si. <br>
E por fim, o `Tailwind CSS` foi a tecnologia que optei para fazer as estilizações do site de maneira mais prática, pois com este framework css eu já tinha várias classes para utilizar, não precisando fazer tudo do zero, a única coisa que mudei foi no arquivo de configuração do tailwind, o `tailwind.config.js`, onde eu coloquei a paleta de cores do site do CB Viagens, para poder utilizá-las onde eu precisasse.
