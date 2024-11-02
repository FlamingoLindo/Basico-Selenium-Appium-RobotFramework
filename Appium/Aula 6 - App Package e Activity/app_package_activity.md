# Como achar appPackage e appActivity de um aplicativo? 

1. Abra o terminal e digite o seguinte comando:

```powershell
adb shell
```

2. Agora abra o aplicativo desejado.

3. Por ultimo digite esse comando:

```powershell
dumpsys window displays | grep -E 'mCurrentFocus'
```

Esse comando irá retornar texto do da seguinte maneira:

![app](/Images/Appium/Appium-Aula2-16.png)