# Abrindo o inspetor de elementos

## Iniciando o servidor

Toda vez que você for fazer algum teste utilizando o appium, é necessário iniciar o servidor antes de tudo.

Para iniciar o servidor basta digitar a seguinte linha no terminal: `appium --allow-cors`

**Antes de iniciar o servidor é necessário que o seu celular esteja conectado com o seu computador!**

## Abrindo o inspetor

Agora abra o google e abra o [inspetor](https://inspector.appiumpro.com/):
https://inspector.appiumpro.com/

1. Dentro do Inspector clique duas (2) vezes na opção para adicionar uma capacidade "capability":

![capAdd](/Images/Appium/Appium-Aula2-12.png)

2. Dentro de cada caixa digite os seguintes valores:

| Nome | Tipo | Valor |
|------|------|-------|
|platformName|text|Android|
|appium:automationName|text|uiautomator2|
