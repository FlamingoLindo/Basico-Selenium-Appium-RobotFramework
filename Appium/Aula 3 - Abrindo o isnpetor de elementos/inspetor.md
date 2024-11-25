# Abrindo o inspetor de elementos

## Iniciando o servidor

Toda vez que você for fazer algum teste utilizando o appium, é necessário iniciar o servidor antes de tudo.

Para iniciar o servidor basta digitar a seguinte linha no terminal: `appium --allow-cors`

**Antes de iniciar o servidor é necessário que o seu celular esteja conectado com o seu computador!**

## Abrindo o inspetor

Agora abra o google e abra o [inspetor](https://inspector.appiumpro.com/):
<https://inspector.appiumpro.com/>

1. Dentro do Inspector clique duas (2) vezes na opção para adicionar uma capacidade "capability":

![capAdd](/Images/Appium/Appium-Aula2-12.png)

2. Dentro de cada caixa digite os seguintes valores:

| Nome | Tipo | Valor |
|------|------|-------|
|platformName|text|Android|
|appium:automationName|text|uiautomator2|

Existem diversas capacidades com diversas funções, não vamos entrar muito a fundo nelas nesse tutorial, mas essas duas são as essenciais.

Caso você queria conhecer mais sobre elas segue o link para a página da [documentação](https://appium.io/docs/en/latest/guides/caps/):
<https://appium.io/docs/en/latest/guides/caps/>

## Usando o inspetor

Após declarar as capacidades, clique em `Start Session`.

Agora você pode usar o Inspector como se ele fosse a ferramenta do google para localizar elementos.

![usando](/Images/Appium/Appium-Aula2-13.png)
