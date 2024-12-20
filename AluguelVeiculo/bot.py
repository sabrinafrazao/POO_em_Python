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
from VeiculoAlugar import VeiculoAlugar
from Carro import Carro
from Moto import Moto

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


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
    bot.browse("http://127.0.0.1:5500/AluguelVeiculo/index.html")

    # Implement here your logic...
    VeiculoAlugar.nome = "Honda civic"
    VeiculoAlugar.ano = 2020
    VeiculoAlugar.valor_diario = 200
    VeiculoAlugar.dias = 10
    Carro.tipo_combustivel = "Gasolina"

    bot.find_element('//*[@id="nomeVeiculo"]', By.XPATH).send_keys(VeiculoAlugar.nome)
    bot.find_element('//*[@id="anoVeiculo"]', By.XPATH).send_keys(VeiculoAlugar.ano)
    bot.find_element('//*[@id="valorDiario"]', By.XPATH).send_keys(VeiculoAlugar.valor_diario)
    bot.find_element('//*[@id="dias"]', By.XPATH).send_keys(VeiculoAlugar.dias)
    bot.find_element('//*[@id="formVeiculo"]/div[1]/div[1]/label', By.XPATH).click()
    bot.find_element('//*[@id="combustivel"]', By.XPATH).send_keys(Carro.tipo_combustivel)
    bot.find_element('//*[@id="formVeiculo"]/button', By.XPATH).click()
    bot.sleep(5)


    
    
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
