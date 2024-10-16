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
    def __init__(self, nome, preco, quantidade=0):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self._preco = novo_preco
        else:
            print("O preço não pode ser negativo.")

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if nova_quantidade >= 0:
            self._quantidade = nova_quantidade
            print(f"A quantidade de {self.nome} foi atualizada para {self.quantidade} unidades.")
        else:
            print("A quantidade não pode ser negativa.")

    def exibir_informacoes(self):
        print(f"Produto: {self.nome}, Preço: R${self.preco:.2f}, Quantidade: {self.quantidade}")





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

    # Criação do produto
    produto = Produto(nome="Refrigerante", preco=12.50)

    # Atualiza a quantidade do produto
    Produto.quantidade = 20 

    # Exibe informações do produto
    produto.exibir_informacoes()

    # Preenche o formulário
    bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(produto.nome)
    bot.find_element('//*[@id="preco"]', By.XPATH).send_keys(str(produto.preco))
    bot.find_element('//*[@id="quantidade"]', By.XPATH).send_keys(str(produto.quantidade))

    # Envia o formulário
    bot.find_element('/html/body/form/button', By.XPATH).click()

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
