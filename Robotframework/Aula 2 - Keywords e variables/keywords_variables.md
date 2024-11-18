# Variables

Dentro da pasta `Resources` crie um arquivo chamado `variables.robot`

Dentro desse aquirvo será declarado todas as váriaves que serão utilizadas nos testes automatizados:

```robot
*** Variables ***
${page}       https://www.twitch.tv/flamingo_lindo
${browser}    FireFox
${name}       Usuario_Robo
${email}      emailrobot@gmail.com
${password}   !Aa12345678
```

* `*** Variables ***` → É utilziado para declarar a seção de váriaveis no arquivo.

* `${page}` → É o nome da váriavel.

* `https://www.twitch.tv/flamingo_lindo` → É o valor dessa váriavel.

##### Importante

No robotframework é necessário sempre dar uma quantidade necessária de espaço entre um objeto e o seu valor ou parâmetro. 
Esse espaço é igual a apertar uma vez na tecla `tab` ou quatro vezes na tecla `espaço`.

---

# Keywords

Dentro da pasta `Keywords` crie um arquivo chamado `keywords.robot`

Dentro desse aquirvo será criado as _palavras chaves_ que serão as ações que o teste irá realizar:

```robot
*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open the url in browser
    [Arguments]    ${page}    ${browser}
    Open browser    ${page}    ${browser}

Wait for and click in the log-in button
    Wait Until Element Is Visible    css=.ceAbGI
    Click Element    xpath=//*[@id="twilight-sticky-footer-root"]/div/article/div/div/div/div/div/div/div/div[3]/button/div/div

Wait for modal to load
    Wait Until Element Is Visible    css=.jAEPQo

Fill up the form
    [Arguments]    ${name}    ${password}    ${email}
    Input Text    id=signup-username    ${name}
    Input Password    id=password-input    ${password}
    
    Click Element    xpath=/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/div[2]/div[1]/div/select
    Click Element    xpath=/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/div[2]/div[1]/div/select/option[16]

    Click Element    xpath=/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/div[2]/div[2]/div/select
    Click Element    xpath=/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/div[2]/div[2]/div/select/option[3]

    Click Element    xpath=/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/div[2]/div[3]/div/select
    Click Element    xpath=/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/div[2]/div[3]/div/select/option[23]

    Click Element    xpath=/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[4]/div[1]/div/div[1]/button/div/div

    Input Text    id=email-input    ${email}

    Wait Until Element Is Visible   css=.hsDHTp
    Click Button    css=.hsDHTp

Wait and see the results
    Sleep    15s
```

* `*** Settings ***` → É usada para importar bibliotecas, recursos e variáveis necessárias para o funcionamento dos testes.

* `Library    SeleniumLibrary` → Importa a biblioteca SeleniumLibrary, que permite automatizar interações com navegadores, como clicar em elementos e preencher campos.

* `*** Keywords ***` → Define as palavras-chave personalizadas que serão usadas nos casos de teste. Cada palavra-chave é como uma função que agrupa uma série de comandos relacionados.

* `Open the url in browser` → Nome da palavra-chave. Indica que o navegador será aberto e redirecionado para uma URL específica.

* `[Arguments]` → Declara os argumentos que a palavra-chave aceitará, neste caso, `${page}` (URL) e `${browser}` (navegador).

* `Open browser    ${page}    ${browser}` → Usa o comando da SeleniumLibrary para abrir um navegador e acessar a URL especificada.

* `Wait Until Element Is Visible    css=.ceAbGI` → Aguarda até que um elemento específico esteja visível na página antes de prosseguir com a execução do teste.

* `Click Element` → Clica em um elemento na página identificado pelo seletor especificado.

* `Input Text    id=email-input    ${email}` → Insere um texto em um campo de entrada e o texto a ser inserido (valor definido em variáveis).

* `Sleep    15s` → Pausa a execução do teste por um período especificado (15 segundos neste caso).