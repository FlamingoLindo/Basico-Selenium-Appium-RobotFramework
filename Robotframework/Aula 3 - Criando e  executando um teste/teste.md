# Criando um teste

Dentro da pasta `Tests` crie um arquivo chamado `create_accout.robot`

Este aquivo será utilizado para criar e orgarnizar os testes:

```robot
*** Settings ***
Library    SeleniumLibrary
Library    XML
Resource   ../Keywords/keywords.robot
Resource   ../Resources/variables.robot

*** Test Cases ***
Create account
    Open the url in browser    ${page}    ${browser}
    
    Wait for and click in the log-in button

    Wait for modal to load

    Fill up the form    ${name}    ${password}    ${email}

    Wait and see the results

    [Teardown]    Close Browser
```

* `*** Settings ***` → São declaradas as bibliotecas e recursos necessários para o teste.

* `Library    SeleniumLibrary` →  Biblioteca essencial para automatizar ações em navegadores, como abrir uma página, clicar em botões, preencher formulários, entre outras interações. É importada para permitir que o teste realize ações no navegador.

* `Library    XML` → É uma biblioteca utilizada para manipulação de documentos XML. Embora não seja utilizada diretamente no exemplo fornecido, pode ser útil para manipular ou validar dados em formato XML em outros casos de teste.

* `Resource   ../Keywords/keywords.robot` → O arquivo keywords.robot contém palavras-chave personalizadas (ações específicas que o teste executa). Ele é importado para que essas palavras-chave possam ser usadas neste arquivo de teste.

* `Resource   ../Resources/variables.robot` → O arquivo variables.robot contém as variáveis usadas no teste, como URL, navegador, nome de usuário, etc. Ele é importado para fornecer esses valores no momento da execução do teste.

* `*** Test Cases ***` → Cada caso de teste consiste em uma série de palavras-chave que serão executadas.

* `Create account` → Este é o nome do caso de teste. O nome serve para identificar o teste e deve descrever de maneira clara o que está sendo testado. No caso, estamos criando uma conta, então o nome do caso de teste reflete isso.

* `Open the url in browser    ${page}    ${browser}` → Palavra-chave personalizada que abre o navegador e acessa a URL. Os valores `${page}` (URL) e `${browser}` (navegador) são variáveis que são passadas a partir do arquivo `variables.robot`.

* `Wait for and click in the log-in button` → Espera até que o botão de login esteja visível e então clica nele. Isso é útil quando a página pode levar um tempo para carregar completamente. A palavra-chave vai garantir que o botão de login esteja visível antes de tentar clicar.

* `Wait for modal to load` → Palavra-chave personalizada que aguarda o carregamento de um modal (caixa de diálogo ou janela pop-up) na página. Ela usa um comando Wait Until Element Is Visible para garantir que o modal seja carregado e visível.

* `Fill up the form    ${name}    ${password}    ${email}` → Palavra-chave personalizada que preenche um formulário com os dados do usuário. Os parâmetros `${name}`, `${password}` e `${email}` são passados como variáveis (definidas no arquivo variables.robot) e inseridos nos campos apropriados da página.

* `Wait and see the results` → Palavra-chave personalizada que espera (com o comando Sleep) por 15 segundos. Isso é útil para ver o que acontece após a execução do formulário e o login. Em muitos casos de automação, usar Sleep é uma maneira simples de garantir que os resultados sejam visíveis antes de o teste ser finalizado, mas deve ser usado com cautela, pois pode tornar os testes mais lentos.

* `[Teardown]    Close Browser` → É uma seção que define ações que devem ser realizadas após a execução do caso de teste, independentemente de o teste ter passado ou falhado. Neste caso, a palavra-chave Close Browser é chamada para fechar o navegador após o término do teste, garantindo que os recursos sejam liberados corretamente.

# Executando um teste

Para executar um teste, basta apenas clicar em `run` que aparece em cima do nome do caso de teste.

![exc](/Images/Robot/7.png)

Após a execução do testeé possivel ver que ele passou sem nenhum erro e que alguns arquis foram criados no _root_ do projeto.

![result](/Images/Robot/8.png)

Se clicar no segundo caminho **Log:** nele com `Ctrl + botão esquerdo o mouse`

![log](/Images/Robot/9.png)

O **Log** contém um registro detalhado da execução do teste, permitindo verificar o que aconteceu durante a execução. Ele fornece informações sobre:

* Passos do Teste: Cada palavra-chave que foi executada, com detalhes sobre o que aconteceu em cada uma delas (se o passo foi bem-sucedido ou se ocorreu algum erro).

* Mensagens de Erro: Se algum erro ocorrer durante o teste (por exemplo, se um elemento não for encontrado ou uma interação falhar), o log exibirá uma mensagem detalhada sobre o erro, ajudando a identificar o que deu errado.

* Captura de Tela (se configurado): Caso o teste esteja configurado para tirar capturas de tela quando um erro ocorrer, o log pode incluir essas imagens.

* Tempo de Execução: O tempo que cada parte do teste levou para ser executada, podendo ser útil para análise de desempenho.

A interface do Log normalmente exibe o histórico completo da execução e permite navegar por cada passo do teste, ajudando na depuração e na análise de falhas.

Se clicar no terceiro caminho **Report:** nele com `Ctrl + botão esquerdo o mouse`

![report](/Images/Robot/10.png)

O **Report** fornece um resumo visual e consolidado da execução do teste. Ele geralmente contém:

* Resumo do Teste: Informações gerais sobre a execução, como a quantidade de testes executados, passados, falhados e ignorados.
Status Global: Um status geral da execução (se foi bem-sucedida ou se houve falhas).

* Testes Detalhados: Detalhes sobre cada caso de teste, como o nome do teste, o tempo de execução e o status (passou ou falhou).

* Histórico de Execuções: Em alguns casos, o Report pode incluir uma comparação com execuções anteriores, permitindo avaliar se o número de falhas ou testes bem-sucedidos está mudando ao longo do tempo.

O Report é uma forma mais resumida e amigável de visualizar os resultados do teste, com ênfase na interpretação rápida dos dados, sem tantos detalhes como o Log.

**Diferença entre Log e Report:**

**Log:** É o registro detalhado de tudo o que aconteceu durante a execução, útil para depuração e entendimento profundo do fluxo de execução.

**Report:** É o resumo visual da execução, focado no status geral dos testes, ideal para ter uma visão rápida do desempenho dos testes.

Ambos são ferramentas importantes para verificar o sucesso ou falha de um teste e diagnosticar problemas, mas com diferentes níveis de detalhamento.
