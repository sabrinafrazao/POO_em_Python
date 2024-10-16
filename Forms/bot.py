"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/web/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

class FormBase:
    def __init__(self, nomeCompleto, usuario, senha, email, nascimento, sexo):
        self._nomeCompleto = nomeCompleto
        self._usuario = usuario
        self._senha = senha
        self._email = email
        self._nascimento = nascimento
        self._sexo = sexo

    @property
    def nomeCompleto(self):
        return self._nomeCompleto

    @nomeCompleto.setter
    def nomeCompleto(self, value):
        self._nomeCompleto = value

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, value):
        self._usuario = value

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, value):
        self._senha = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, value):
        self._nascimento = value

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, value):
        self._sexo = value



class FormContato(FormBase):
    def __init__(self, nomeCompleto, email, contato):
        super().__init__(nomeCompleto, None, None, email, None, None)
        self._contato = contato

    @property
    def contato(self):
        return self._contato

    @contato.setter
    def contato(self, value):
        self._contato = value


class FormLogin(FormBase):
    def __init__(self, usuario, senha):
        super().__init__(None, usuario, senha, None, None, None)

        @property
        def usuario(self):
            return self._usuario

        @usuario.setter
        def usuario(self, valor):
            self._usuario = valor

        @property
        def senha(self):
            return self._senha

        @senha.setter
        def senha(self, valor):
            self._senha = valor

  


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME

    # Uncomment to set the WebDriver path
    bot.driver_path = ChromeDriverManager().install()

    # Opens the BotCity website.
    bot.browse("http://127.0.0.1:5500/Forms/form_cadastro.html")

    # Implement here your logic...

    FormBase.nomeCompleto = "Sabrina da Silva Frazão"
    FormBase.usuario = "sabrina"
    FormBase.senha = "ifam@zl"
    FormBase.email = "sabrina@gmail.com"
    FormBase.nascimento = "11/08/2002"
    FormBase.sexo = "Feminino"

    bot.find_element('//*[@id="nome"]', By.XPATH ).send_keys(FormBase.nomeCompleto)
    bot.find_element('//*[@id="nomedeusuario"]', By.XPATH ).send_keys(FormBase.usuario)
    bot.find_element('//*[@id="senha"]', By.XPATH ).send_keys(FormBase.senha)
    bot.find_element('//*[@id="email"]', By.XPATH ).send_keys(FormBase.email)
    bot.find_element('//*[@id="datanascimento"]', By.XPATH ).send_keys(FormBase.nascimento)
    bot.find_element('//*[@id="sexo"]', By.XPATH ).send_keys(FormBase.sexo)

    bot.find_element( '//*[@id="formularioCadastro"]/button', By.XPATH).click()


    FormLogin.usuario = "sabrina"
    FormLogin.senha = "ifam@zl"

    bot.find_element('//*[@id="username"] ', By.XPATH ).send_keys(FormLogin.usuario)
    bot.find_element(' //*[@id="password"]', By.XPATH ).send_keys(FormLogin.senha)

    bot.find_element( '//*[@id="formularioLogin"]/button', By.XPATH).click()

    print("Dados do Formulário de Cadastro:")
    print(f"Nome Completo: {FormBase.nomeCompleto}")
    print(f"Usuário: {FormBase.usuario}")
    print(f"Email: {FormBase.email}")
    print(f"Data de Nascimento: {FormBase.nascimento}")
    print(f"Sexo: {FormBase.sexo}")
    print("\n")

    FormContato.nomeCompleto = "Sabrina da Silva Frazão"
    FormContato.email = "sabrina@gmail.com"
    FormContato.contato = "986389490s"

    bot.find_element('//*[@id="nome"]', By.XPATH ).send_keys(FormContato.nomeCompleto)
    bot.find_element('//*[@id="email"]', By.XPATH ).send_keys(FormContato.email)
    bot.find_element('//*[@id="telefone"]', By.XPATH ).send_keys(FormContato.contato)


    bot.find_element( '//*[@id="formularioContato"]/button', By.XPATH).click()

    print("Dados do Formulário de Contato:")
    print(f"Nome Completo: {FormContato.nomeCompleto}")
    print(f"Email: {FormContato.email}")
    print(f"Contato: {FormContato.contato}")

   


 
    

    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
