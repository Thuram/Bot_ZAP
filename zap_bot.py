from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Bom dia"
        self.grupos = ["🎮 Bora jogar 🎮"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        # <span dir="auto" title="🎮 Bora Jogar 🎮" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">

        # <div class="_2lMWa">

        # <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://www.web.whatappweb.com')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element(f"//span[@tittle='{grupo}'")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element('<div class="_2lMWa">')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(3)


bot = WhatsappBot()
bot.EnviarMensagens()
