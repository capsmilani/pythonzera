# Pythonzera

Repositorio com o intuito de divulgar atividades desenvolvidas em Python

## (Web Scraping) BOT criado para compras no Aliexpress

Objetivo: BOT criado para compras em promoções no Aliexpress. Em grupos do Telegram há diversas promoções com cupons que expiram extremamente rápido, nesse contexto decidi criar este BOT para automatizar todo o processo e ficar inserindo JIT o código promocional.  

Link para manual: [Manual Selenium](https://selenium-python.readthedocs.io/index.html)

### Pré-requesitos
Para que o script funcione é necessário ter instalado a bibliote Selenium (pode ser instalado conforme comando a baixo) e também o Driver para Chrome.

Biblioteca que deve ser instalado:
> pip install selenium

Link para download do Driver: [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### Parametros

   - horario - Uma list com dois valores inteiros sendo o primeiro de 0 à 23 e o segundo de 0 à 59;
   - user - Uma string contendo o valor de usuário (podendo ser um apelido ou um e-mail);
   - password - Uma string contendo a senha para o usuário selecionado;
   - url - Uma string contendo o link para o item que deseja comprar;
   - PATH -  Uma string contendo o destino do driver baixado. Exemplo: "C:/WebDriver/bin/chromedriver.exe";
   - cupom_desconto - Uma string contendo o cupom de desconto;    
   - preco_max - Uma variavel inteira contedo qual deve ser o valor máximo a ser pago pelo item; 
