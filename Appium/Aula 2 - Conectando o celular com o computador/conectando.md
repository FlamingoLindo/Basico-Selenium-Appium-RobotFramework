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

* Ativando a depuração USB:

  * Pesquise por "**Depuração USB**":
    ![USBsearch](/Images/Appium/Appium-Aula2-5.jpg)

    * Ative a opção "**Depuração USB**":
    ![USB](/Images/Appium/Appium-Aula2-4.jpg)

* Agora conecte o seu dispositivel com o computador e permita a depuração:

![allowDep](/Images/Appium/Appium-Aula2-7.jpg)

* Abra um terminal e digite "**abd devices**":

![adb](/Images/Appium/Appium-Aula2-6.png)

Pronto agora seu dispositivo está conectado e pronto para ser utilizado para testes.

### Como conectar por Wi-fi

* Abra o terminal e digite a seguinte linha de comando "**adb tcpip 5555**":

![tcpip](/Images/Appium/Appium-Aula2-8.png)

* Abra as configurações do seu dispositivo e pesquise por "**Endereço IP**":

![ipSearch](/Images/Appium/Appium-Aula2-10.jpg)

* Então copie o seu IP (sequência de números na segunda linha):

![ip](/Images/Appium/Appium-Aula2-11.jpg)

* Agora, no terminal digite:

```powershell
adb connect <ip>
```

* Por ultimo, abra o terminal e digite "**adb devices**" para verificar se o dispositivo conectou ou não.
