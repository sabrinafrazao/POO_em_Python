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
from xml.etree.ElementPath import xpath_tokenizer
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

class Produto:

    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        self._qtd = 0  

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    @property
    def qtd(self):
        return self._qtd

    @qtd.setter
    def atualizar(self, nova_qtd):
        if nova_qtd >= 0:
            self._qtd = nova_qtd
            print(f"A quantidade de {self.nome} foi atualizada para {self._qtd} unidades.")
        else:
            print("A quantidade não pode ser negativa.")

    def exibir(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade em estoque: {self.qtd}")


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
    bot.browse("http://127.0.0.1:5500/fomulario_produto/forms.html")

    Produto.nome = "Refrigerante"
    Produto.preco = 12
    Produto.qtd = 10
    bot.find_element('//*[@id="nome"]', By.XPATH ).send_keys(Produto.nome)
    bot.find_element('//*[@id="preco"]', By.XPATH ).send_keys(Produto.preco)
    bot.find_element('//*[@id="qtd"]', By.XPATH ).send_keys(Produto.qtd)


        # Clicar no botão de enviar
    bot.find('//*[@id="submit"]', By.XPATH).click() 

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
