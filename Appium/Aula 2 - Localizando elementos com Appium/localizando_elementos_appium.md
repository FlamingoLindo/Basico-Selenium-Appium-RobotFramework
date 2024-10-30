# Localizando elementos utilizando Appium

## Celular conectado pelo USB, wi-fi ou emulador?

1. **Dispositivo via cabo USB:** 
É o método mais estável, ideal para testes de UI detalhados. Como está diretamente conectado, há menos chance de latência, e ele suporta quase todas as operações do Appium sem problemas.

2. **Dispositivo via Wi-Fi:** 
Útil para testes remotos ou quando o dispositivo não pode ser conectado fisicamente. A configuração exige mais passos e depende de um bom sinal de Wi-Fi. A latência é maior, mas ainda assim é útil para algumas automações.

3. **Emulador:** 
Muito utilizado em testes de desenvolvimento e integração contínua (CI/CD). Ele permite um controle maior do ambiente, como configurações de sistema, reinicializações rápidas e criação de estados personalizados para os testes. No entanto, o desempenho pode ser inferior a dispositivos reais.

### Como conectar pelo USB

Esse é o método mais simples de todos.
Basta apenas conectar o seu celular com o seu computador com um cabo USB.
Mas para isso funcionar é preciso ativar a "Depuração USB" nas opções de desenvolvedor do seu dispositovo.

* Ativando opções de desenvolvedor:
    * Abra as configurações do seu dispositivel:
    ![configs](/Images/Appium/Appium-Aula2-1.png)

    * Pesquise por "**Número de compilação**" e abra essa opção:
    ![compNum](/Images/Appium/Appium-Aula2-2.jpg)

    * Clique três (3) vezes na opção "**Número de compilação**" para ativar as opções de desenvolvedor:
    ![treeTimes](/Images/Appium/Appium-Aula2-3.jpg)

