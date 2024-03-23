# API de Imagens

Este é um serviço de API RESTful construído com Flask e Flask-RESTx para recuperar imagens por categoria.

## Como Usar

Para utilizar esta API, siga estas etapas:

### 1. Clonar o Repositório

Clone este repositório em sua máquina local:

```bash
git clone https://github.com/EliasAraujoDev/projetoApiDeImages.git
cd projetoApiDeImages
```

### 2. Instalar Dependências

Instale as dependências necessárias usando `pip`:

Recomendado:
```bash
pip install -r requirements.txt
```

ou

```bash
pip install Flask Flask-RestX
```

### 3. Configurar as Pastas de Imagens

As imagens devem ser organizadas em pastas dentro do diretório `api/images`. Cada pasta representa uma categoria de imagens. Certifique-se de que as imagens estejam localizadas em pastas correspondentes às suas categorias.

Por exemplo:

```
api/
└── images/
    ├── natureza/
    │   ├── imagem1.jpg
    │   ├── imagem2.jpg
    │   └── ...
    ├── animais/
    │   ├── imagem1.jpg
    │   ├── imagem2.jpg
    │   └── ...
    └── ...
```

Obs: As categorias são automaticamente detectadas pela API com base nas pastas dentro de `images`.

### 4. Iniciar o Servidor

Execute o arquivo `app.py` para iniciar o servidor Flask:

```bash
python app.py
```

O servidor será iniciado e estará pronto para receber solicitações.

### 5. Usando a API

Existem duas principais funcionalidades disponíveis nesta API:

- **Listar imagens por categoria**: Você pode obter uma lista de URLs de imagens para uma categoria específica.
- **Obter uma imagem específica**: Você pode obter uma imagem específica por categoria e nome de imagem.

#### Exemplos de Solicitações

- **Listar imagens por categoria**:
  ```bash
  curl http://localhost:5000/images/natureza
  ```

- **Obter uma imagem específica**:
  ```bash
  curl http://localhost:5000/images/natureza/imagem1.jpg --output imagem1.jpg
  ```

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

- `app.py`: O arquivo principal que define a aplicação Flask e suas rotas.
- `requirements.txt`: Arquivo de texto contendo todas as dependências necessárias.
- `api/`: Pasta contendo o código fonte da API.
- `api/images/`: Pasta contendo as imagens categorizadas.

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir para este projeto, siga estas etapas:

1. Faça um fork do projeto.
2. Crie uma branch para sua funcionalidade (`git checkout -b feature/NovaFuncionalidade`).
3. Faça commit de suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
4. Faça push para a branch (`git push origin feature/NovaFuncionalidade`).
5. Crie um novo Pull Request.

## Contato

Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato através das redes sociais em [EliasDevMind](https://eliasdevmind.vercel.app/).

---
