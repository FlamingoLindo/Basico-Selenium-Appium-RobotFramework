# Localizadores

---

## O que são localizadores?

Localizadores são ulizados para indentificar algum elemento em uma página.

---

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

---

## Como encontrar os localizadores

1. Abra a uma página que você quiser no seu navegador de escolha, como exemplo vamos utilizar o Google Chrome.

![Página](/Images//Selenium/Selenium-Aula3-1.png)

2. Aperte a tecla "F12" no seu teclado para a brirar as ferramenas de desenvolvedor.

![DevTools](/Images/Selenium/Selenium-Aula3-2.png)

3. Clicar no ícone de setinha no canto superior esquerdo (pode-se apertar "crtl + shift + c" para abrir essa funcionalidade):

![SelectIcon](/Images/Selenium/Selenium-Aula3-3.png)

4. Agora quando você passar o mouse por cima de algum elemento e clicar nele, esse elemento será selecionando e assim vai ser possivel observar ele no formato DOM:

![SelectedElement](/Images/Selenium/Selenium-Aula3-4.png)

5. Primeiro vamos pegar o **css selector**:

Ele fica localizado no ultimo atributo do elemento, class, ele vai ser a ultima sequência de caracteres:

![CssSelector](/Images/Selenium/Selenium-Aula3-5.png)

Nesse exemplo o seletor é: eA-DoIH.

Nota: atributos do tipo "name" e "id", também são encontrados aqui e são ótimos para a automatização!

6. Agora vamos peagar o **XPath**:

Primero vai ser necessário clicar com o botão direito no elemento selecionado, depois em "Copiar" e por ultimo em "XPath":

![XPath](/Images/Selenium/Selenium-Aula3-6.png)

O XPath então será copiado para a sua área de transferência e o seu formato será assim:

    //*[@id="offline-channel-main-content"]/div[2]/div[1]/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div/div/div/button

Como você deve ter reparado, quando fomos copiar o XPath, haviam diversas opções de copia, mas as opções que nós vamos utlizar aqui serão apenas as:

* seletor
* XPath
* full XPath

---

## Qual tipo de seletor usar?

**1. CSS Selector:**

* É geralmente mais rápido e confiável quando possível, especialmente em navegadores modernos.

* Ideal para selecionar elementos com base em classes, IDs ou atributos específicos.

* Útil para identificar elementos de forma precisa e concisa, especialmente quando a estrutura da página é estável.

**2. XPath:**

* Permite maior flexibilidade, pois pode navegar por estruturas complexas e hierarquias.

* Recomendado quando há necessidade de localizar elementos relativos, como "o segundo elemento após um título específico".

* É útil quando os elementos não têm identificadores únicos.

**3. Full XPath:**

* Utiliza o caminho completo até o elemento na árvore do DOM, indo desde o nó raiz.

* É mais suscetível a mudanças na estrutura da página, pois qualquer alteração no layout pode quebrar o seletor.

* Use-o apenas em última instância, caso os outros métodos não consigam localizar o elemento, e o layout seja estável.

Achou confuso? Não se preocupe com o tempo você pega o jeito! 