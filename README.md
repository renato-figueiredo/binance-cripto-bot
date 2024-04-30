```markdown
# Bot de Verificação de Criptomoedas

## Tecnologias Usadas

Este projeto utiliza Python, juntamente com várias bibliotecas, incluindo `pandas`, `pandas_ta`, `binance-python` e `pyTelegramBotAPI`.

## Sobre o Projeto

Este projeto é um bot de verificação automática de criptomoedas. Ele verifica todas as criptomoedas na Binance que são negociadas com USDT e envia notificações para o Telegram quando certas condições são atendidas. As condições são baseadas no Índice de Força Relativa (RSI) e no Índice de Fluxo de Dinheiro (MFI) das criptomoedas.
```

## Iniciando o Projeto

Para iniciar o projeto, primeiro você precisa criar um ambiente virtual Python. Você pode fazer isso usando o seguinte comando no terminal:

```bash
python -m venv venv
```

Depois de criar o ambiente virtual, você precisa ativá-lo. No Windows, você pode fazer isso com o seguinte comando:

```bash
venv\Scripts\activate
```

No Linux ou macOS, você pode usar o seguinte comando:

```bash
source venv/bin/activate
```

## Instalando as Bibliotecas

Depois de ativar o ambiente virtual, você pode instalar as bibliotecas necessárias usando o arquivo `references.txt`. Você pode fazer isso com o seguinte comando:

```bash
pip install -r references.txt
```

## Configuração das Chaves da API

### Binance API Key e Secret

Para configurar as chaves da API da Binance, siga os passos abaixo:

1. Faça login na sua conta da Binance.
2. Navegue até o seu painel de controle.
3. Clique em "API Management" no menu de configurações.
4. Crie uma nova chave API e dê um nome a ela.
5. Anote a "api_key" e a "api_secret" que são geradas. Você precisará delas para o seu bot.

### Telegram Token

Para obter o token do seu bot do Telegram, siga os passos abaixo:

1. Abra o aplicativo do Telegram e procure por "BotFather".
2. Inicie uma conversa com o BotFather e clique em "/newbot" para criar um novo bot.
3. Siga as instruções fornecidas pelo BotFather para nomear o seu bot.
4. Depois de criar o bot, o BotFather fornecerá um token para o seu bot. Este é o seu "telegram_token".

### Telegram Chat ID

O "chat_id" é o identificador único para a conversa onde você deseja que o bot envie mensagens. Para obter o "chat_id", siga os passos abaixo:

1. Se você quiser que o bot envie mensagens para você, inicie uma conversa com o bot no Telegram e envie qualquer mensagem para ele.
2. Em seguida, abra uma nova guia no seu navegador e acesse `https://api.telegram.org/bot<YourBOTToken>/getUpdates`. Substitua `<YourBOTToken>` pelo token do seu bot.
3. Você verá uma resposta JSON. O "chat_id" estará no campo "id" dentro do objeto "chat".

Por favor, substitua 'api_key', 'api_secret', 'telegram_token' e 'chat_id' pelos seus respectivos valores no código. Lembre-se de manter essas informações seguras, pois elas podem ser usadas para controlar o seu bot e acessar a sua conta da Binance.

## Iniciando o Bot

Depois de configurar as chaves da API e instalar as bibliotecas necessárias, você pode iniciar o bot. Siga as etapas abaixo:

1. **Ative o ambiente virtual (venv)**: Navegue até o diretório onde o ambiente virtual está localizado no terminal. Uma vez lá, você pode ativá-lo. No Windows, use o seguinte comando:

   ```bash
   venv\Scripts\activate
   ```

   No Linux ou macOS, use o seguinte comando:

   ```bash
   source venv/bin/activate
   ```

2. **Inicie o bot**: Depois de ativar o ambiente virtual, você pode iniciar o bot executando o arquivo 'cripto_bot.py'. Certifique-se de que você está no diretório correto que contém o arquivo 'cripto_bot.py'. Você pode iniciar o bot com o seguinte comando:

   ```bash
   python cripto_bot.py
   ```

Lembre-se de substituir 'venv' pelo nome do seu ambiente virtual, se for diferente. E certifique-se de que 'cripto_bot.py' é o nome correto do seu arquivo de script Python.

Agora, o bot deve estar rodando e verificando as condições das criptomoedas a cada 15 minutos. Ele enviará notificações para o Telegram quando as condições forem atendidas.