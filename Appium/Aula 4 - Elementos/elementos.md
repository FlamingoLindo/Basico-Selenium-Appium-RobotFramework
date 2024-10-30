# Localizando elementos e quais utilizar

## Localizando

Para selecionar um elemento no seu dispositivo, basta passar o mouse em cima de algum elemento no *preview* do seu dispositivo.

![select](/Images/Appium/Appium-Aula2-14.png)

## Localizadores

Os localizadores são encontrados no lado direto da página, após selecionar um elemento:

![selectors](/Images/Appium/Appium-Aula2-15.png)

Basta clicar com o botão esquerdo sobre o seletor que ele será automaticamente copiado para a sua área de transferência.

## Quais são os tipos de localizadores

| Nome                 | Descrição                                                                                                                                                                                                                                              | Classificação de Velocidade | Exemplo                                                                                                                      |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| id                   | Esta estratégia é mapeada para o localizador `By.res` nativo do UiAutomator (correspondência exata do nome do recurso do elemento). O prefixo do identificador do pacote é adicionado automaticamente, se não definido, e é igual ao identificador do aplicativo em teste. | ⭐⭐⭐⭐⭐                        | 'com.mycompany:id/resourceId'                                                                                                |
| accessibilityId      | Esta estratégia é mapeada para o localizador `By.desc` nativo do UiAutomator (correspondência exata da descrição do conteúdo do elemento). Em aplicativos desenvolvidos com o framework ReactNative, este atributo reflete o valor da propriedade `accessibilityLabel`. | ⭐⭐⭐⭐⭐                        | 'minha descrição'                                                                                                            |
| className            | Esta estratégia é mapeada para o localizador `By.clazz` nativo do UiAutomator (correspondência exata da classe do elemento).                                                                                                                          | ⭐⭐⭐⭐⭐                        | 'android.view.View'                                                                                                          |
| -android uiautomator | Esta estratégia é mapeada para o localizador `UiSelector` do UiAutomator nativo. É possível realizar algumas operações avançadas, como rolar, com esse tipo de localizador. Confira o Guia de Tipos de Localizador UiAutomator. | ⭐⭐⭐⭐                         | new UiScrollable(new UiSelector().resourceId("android:id/list")).scrollIntoView(new UiSelector().text("Radio Group")) |
| xpath                | Para a estratégia de localização de elementos `Xpath`, o driver usa a mesma árvore XML gerada pela API `page source`. Somente o Xpath 1.0 é suportado para versões do appium-uiautomator2-server abaixo de 4.25.0. Todas as versões a partir da 4.25.0 suportam Xpath 1.0 e 2.0. | ⭐⭐⭐                          | By.xpath("//android.view.View[@text='Regular' and @checkable='true']")                                                        |
