# Localizadores

## O que são localizadores?

Localizadores são ulizados para indentificar algum elemento em uma página.

## Quais são os tipos de localizadores?

| Tipo | Descrição |
|------|-----------|
|class name|Localiza elementos cujo nome de classe contém o valor de pesquisa (nomes de classes compostos não são permitidos)|
|css selector|Localiza elementos que correspondem a um seletor CSS|
|id|Localiza elementos cujo atributo ID corresponde ao valor de pesquisa|
|name|Localiza elementos cujo atributo NAME corresponde ao valor pesquisado|
|link text|Localiza elementos âncora cujo texto visível corresponde ao valor de pesquisa|
|partial link text|Localiza elementos âncora cujo texto visível contém o valor de pesquisa. Se vários elementos corresponderem, apenas o primeiro será selecionado|
|tag name|Localiza elementos cujo nome da tag corresponde ao valor de pesquisa|
|xpath|Localiza elementos que correspondem a uma expressão XPath|

Essa tabela foi retirada do site do [Selenium][0].

[0]:https://www.selenium.dev/documentation/webdriver/elements/locators/

## Como encontrar os localizadores

1. Abra a uma página que você quiser no seu navegador de escolha, como exemplo vamos utilizar o Google Chrome.
![p](Images\Selenium\Selenium-Aula3-1.png)
2. Aperte a tecla "F12" no seu teclado para a brirar as ferramenas de desenvolvedor.