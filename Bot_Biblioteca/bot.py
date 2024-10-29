from botcity.web import WebBot, Browser, By


from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager

from Biblioteca import Livro
from Biblioteca import Autor
import Biblioteca


BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():

    maestro = BotMaestroSDK.from_sys_args()

    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()


    bot.headless = False


    bot.browser = Browser.CHROME


    bot.driver_path = ChromeDriverManager().install()

    # Opens the BotCity website.
    bot.browse("http://127.0.0.1:5500/Bot_Biblioteca/Biblioteca/index.html?")

    # Livro 1
    Livro.titulo = "Dom Casmurro"
    Autor.nome = "Machado de Assis"
    Livro.codigo =  "12345"

    bot.find_element('//*[@id="titulo"]', By.XPATH).send_keys(Livro.titulo)
    bot.sleep(2000)
    bot.find_element('//*[@id="autor"]', By.XPATH).send_keys(Autor.nome)
    bot.sleep(2000)
    bot.find_element('//*[@id="codigo"]', By.XPATH).send_keys(Livro.codigo)
    bot.sleep(2000)
    bot.find_element('/html/body/div/button[1]', By.XPATH).click()
    bot.sleep(2000)

    # Livro 2
    Livro.titulo = "O Pequeno Príncipe"
    Autor.nome = "Antoine de Saint-Exupéry"
    Livro.codigo =  "54321"

    bot.find_element('//*[@id="titulo"]', By.XPATH).send_keys(Livro.titulo)
    bot.sleep(2000)
    bot.find_element('//*[@id="autor"]', By.XPATH).send_keys(Autor.nome)
    bot.sleep(2000)
    bot.find_element('//*[@id="codigo"]', By.XPATH).send_keys(Livro.codigo)
    bot.sleep(2000)
    bot.find_element('/html/body/div/button[1]', By.XPATH).click()
    bot.sleep(2000)

    # Livro 1
    Livro.titulo = "O Poder do Hábito"
    Autor.nome = " Charles Duhigg"
    Livro.codigo =  "98765"

    bot.find_element('//*[@id="titulo"]', By.XPATH).send_keys(Livro.titulo)
    bot.sleep(2000)
    bot.find_element('//*[@id="autor"]', By.XPATH).send_keys(Autor.nome)
    bot.sleep(2000)
    bot.find_element('//*[@id="codigo"]', By.XPATH).send_keys(Livro.codigo)
    bot.sleep(2000)
    bot.find_element('/html/body/div/button[1]', By.XPATH).click()
    bot.sleep(2000)

    bot.scroll_down(3)
    bot.sleep(3000)

    # Emprestimo
    Livro.codigo =  "98765"
    Biblioteca.cliente = "Sabrina Frazão"

    bot.find_element('//*[@id="codigoEmprestimo"]', By.XPATH).send_keys(Livro.codigo)
    bot.sleep(2000)
    bot.find_element('//*[@id="cliente"]', By.XPATH).send_keys(Biblioteca.cliente)
    bot.sleep(2000)
    bot.find_element('/html/body/div/button[2]', By.XPATH).click()
    bot.sleep(3000)

    bot.scroll_down(3)
    bot.sleep(3000)

    # Devolver o Livro
    Livro.codigo =  "98765"

    bot.find_element('//*[@id="codigoDevolucao"]', By.XPATH).send_keys(Livro.codigo)
    bot.sleep(2000)
    bot.find_element('/html/body/div/button[3]', By.XPATH).click()

    bot.scroll_down(3)
    bot.sleep(3000)

   
    bot.wait(3000)

    bot.stop_browser()

 

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
