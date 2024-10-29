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
https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""

# Import for the Desktop Bot
import os
import subprocess
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *


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

    bot = DesktopBot()
    bot.execute(r"C:\Users\matutino\Desktop\POO_em_Python\Bot_Pagamentos_Funcionarios\dist\App.exe")

    # Cadastro do primeiro funcionario

    if not bot.find("nome", matching=0.97, waiting_time=10000):
        not_found("nome")
    bot.click_relative(40, 33)
    
    bot.paste("Sabrina Frazão")

    if not bot.find("matricula", matching=0.97, waiting_time=10000):
        not_found("matricula")
    bot.click_relative(17, 32)
    
    bot.paste("12345")
    
    if not bot.find("mensal", matching=0.97, waiting_time=10000):
        not_found("mensal")
    bot.click_relative(-13, 6)
    
    if not bot.find("salario-valorHora", matching=0.97, waiting_time=10000):
        not_found("salario-valorHora")
    bot.click_relative(17, 34)
    
    bot.paste(1860)

    if not bot.find("cadastro", matching=0.97, waiting_time=10000):
        not_found("cadastro")
    bot.click()

    if not bot.find("ConfirmarCadastro", matching=0.97, waiting_time=10000):
        not_found("ConfirmarCadastro")
    bot.click()

    # Cadastro do segundo funcionario

    if not bot.find("nome", matching=0.97, waiting_time=10000):
        not_found("nome")
    bot.click_relative(40, 33)
    
    bot.paste("João Perera")

    if not bot.find("matricula", matching=0.97, waiting_time=10000):
        not_found("matricula")
    bot.click_relative(17, 32)
    
    bot.paste("678988")
    
    if not bot.find("Horista", matching=0.97, waiting_time=10000):
        not_found("Horista")
    bot.click_relative(-14, 6)
    
    if not bot.find("salario-valorHora", matching=0.97, waiting_time=10000):
        not_found("salario-valorHora")
    bot.click_relative(17, 34)
    
    bot.paste(25)

    if not bot.find("HoraTrabalho", matching=0.97, waiting_time=10000):
        not_found("HoraTrabalho")
    bot.click_relative(16, 34)

    bot.paste(40)

    if not bot.find("cadastro", matching=0.97, waiting_time=10000):
        not_found("cadastro")
    bot.click()

    if not bot.find("ConfirmarCadastro", matching=0.97, waiting_time=10000):
        not_found("ConfirmarCadastro")
    bot.click()
    

    # Cadastro do terceiro funcionario

    if not bot.find("nome", matching=0.97, waiting_time=10000):
        not_found("nome")
    bot.click_relative(40, 33)
    
    bot.paste("Paula Fernandes Rodrigues")

    if not bot.find("matricula", matching=0.97, waiting_time=10000):
        not_found("matricula")
    bot.click_relative(17, 32)
    
    bot.paste("190875")
    
    if not bot.find("comisionado", matching=0.97, waiting_time=10000):
        not_found("comisionado")
    bot.click_relative(-14, 7)
    
 
    if not bot.find("salario-valorHora", matching=0.97, waiting_time=10000):
        not_found("salario-valorHora")
    bot.click_relative(17, 34)
    
    bot.paste(1900)

    
    if not bot.find("vendas", matching=0.97, waiting_time=10000):
        not_found("vendas")
    bot.click_relative(14, 33)

    bot.paste(15)

    if not bot.find("comissao", matching=0.97, waiting_time=10000):
        not_found("comissao")
    bot.click_relative(28, 30)

    bot.paste(5)

    if not bot.find("cadastro", matching=0.97, waiting_time=10000):
        not_found("cadastro")
    bot.click()

    if not bot.find("ConfirmarCadastro", matching=0.97, waiting_time=10000):
        not_found("ConfirmarCadastro")
    bot.click()  


    if not bot.find("listarFuncionario", matching=0.97, waiting_time=10000):
        not_found("listarFuncionario")
    bot.click()

    bot.sleep(3000)

    # Editar Funcionarios

    if not bot.find("editarMensalista", matching=0.97, waiting_time=10000):
        not_found("editarMensalista")
    bot.click()

    if not bot.find("atualizarValorHora", matching=0.97, waiting_time=10000):
        not_found("atualizarValorHora")
    bot.click_relative(60, 32)

    bot.control_a()
    bot.backspace()
    bot.paste(2000)

    if not bot.find("atualizar", matching=0.97, waiting_time=10000):
        not_found("atualizar")
    bot.click()
    

   # Excluir  Funcionario
    if not bot.find("listarFuncionario", matching=0.97, waiting_time=10000):
        not_found("listarFuncionario")
    bot.click()

    if not bot.find("excluir", matching=0.97, waiting_time=10000):
       not_found("excluir")
    bot.click()

    if not bot.find("confirmarExcluir", matching=0.97, waiting_time=10000):
        not_found("confirmarExcluir")
    bot.click()

    bot.sleep(3000)
    
    if not bot.find("fecharlista", matching=0.97, waiting_time=10000):
        not_found("fecharlista")
    bot.click()

    if not bot.find("fechar", matching=0.97, waiting_time=10000):
        not_found("fechar")
    bot.click()
    

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
    