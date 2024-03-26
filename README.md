### Setup environment
Instructions from Appium https://appium.io/docs/en/2.5/quickstart/

- install Java (OpenJDK) 
- install Node.JS
- install Appium https://appium.io/docs/en/2.1/quickstart/install/
- install UIAutomator2 https://github.com/appium/appium-uiautomator2-driver
- install Android Studio and Android SDK https://developer.android.com/studio
- add to global vars ANDROID_HOME and ANDROID_SDK_ROOT

    _for Ubuntu:_ \
    `$ vim ~/.bashrc` \
    _Add following lines_ \
    `export ANDROID_HOME=$HOME/Android/Sdk` \
    `export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools` \

- optionally - install Appium Inspector https://github.com/appium/appium-inspector/releases
- create file [settings.ini](settings.ini) in the project root dir with values: \
`[settings]` \
`LOGIN=<LOGIN>` \
`PASSWORD=<PASSWORD>` 



### Ajax Systems, Python developer in test for Application team
Для виконання тестового завдання Вам необхідно встановити застосунок Ajax Systems на телефон (якщо не маєте реального Android девайса, можна використати емулятор).

### Завдання
1) Написати базовий функціонал для роботи з застосунком (пошук елемента, клік по елементу і т.і.).
2) Написати тест логіну користувача в застосунок (позитивний і негативний кейси).
3) Використати параметризацію.
4) Закомітити виконане завдання на гітхаб.

### Додаткове завдання (опціонально)
1) *Реалізувати логування тесту.
2) *Реалізувати динамічне визначення udid телефона через subprocess
3) **Написати тест на перевірку елементів SideBar (випадаюче меню зліва).

### Корисні посилання
1) Застосунок - https://play.google.com/store/apps/details?id=com.ajaxsystems
2) Робота з реальним телефоном - https://developer.android.com/studio/command-line/adb
3) Налаштування емулятора - https://developer.android.com/studio/run/emulator
4) Налаштування Appium - https://appium.io/docs/en/2.0/quickstart/
5) Драйвер - http://appium.io/docs/en/2.1/quickstart/uiauto2-driver/
6) Appium Inspector - https://github.com/appium/appium-inspector

### Login credentials
login - qa.ajax.app.automation@gmail.com
password - qa_automation_password
