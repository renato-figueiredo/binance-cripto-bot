import pandas as pd
import pandas_ta as ta
from binance.client import Client
import telebot
import time

api_key = 'Escreva aqui'
api_secret = 'Escreva aqui'
telegram_token = 'Escreva aqui'
chat_id = 'Escreva aqui'

# Substitua 'api_key' e 'api_secret' pelas suas chaves da API da Binance
client = Client(api_key, api_secret)

# Substitua 'telegram_token' pelo token do seu bot do Telegram
bot = telebot.TeleBot(telegram_token)

def check_rsi_mfi(symbol, interval):
    # Obtenha os dados do kline
    klines = client.get_klines(symbol=symbol, interval=interval)

    # Converta para DataFrame do pandas
    df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])

    # Converta as colunas para float
    df['high'] = pd.to_numeric(df['high'])
    df['low'] = pd.to_numeric(df['low'])
    df['close'] = pd.to_numeric(df['close'])
    df['volume'] = pd.to_numeric(df['volume'])

    # Calcule o RSI
    rsi = ta.rsi(df['close'], length=14)

    # Calcule o MFI
    mfi = ta.mfi(df['high'], df['low'], df['close'], df['volume'], length=14)

    return rsi.iloc[-1], mfi.iloc[-1]

def send_telegram_message(message):
    # Substitua 'chat_id' pelo ID do chat do Telegram onde você deseja receber as notificações
    bot.send_message(chat_id, message)

# Verifique todas as criptomoedas ativas a cada 15 minutos
while True:
    for symbol in client.get_all_tickers():
        # Verifique apenas as criptomoedas que são negociadas com USDT
        if 'USDT' in symbol['symbol']:
            # Verifique o gráfico de 1 hora
            rsi_hour, mfi_hour = check_rsi_mfi(symbol['symbol'], Client.KLINE_INTERVAL_1HOUR)
            # Verifique o gráfico de 15 minutos
            rsi_15min, mfi_15min = check_rsi_mfi(symbol['symbol'], Client.KLINE_INTERVAL_15MINUTE)

            # Verifique os parâmetros para ambos os intervalos de tempo
            if rsi_hour > 70 and mfi_hour > 80 and rsi_15min > 70 and mfi_15min > 80:
                send_telegram_message(f"{symbol['symbol']}: Faça uma ação de mercado chamada 'short' (Encontrado no gráfico de 1 hora e de 15 minutos)")
            elif rsi_hour < 20 and mfi_hour < 20 and rsi_15min < 20 and mfi_15min < 20:
                send_telegram_message(f"{symbol['symbol']}: Faça uma ação de mercado chamada 'long' (Encontrado no gráfico de 1 hora e de 15 minutos)")
            elif rsi_hour > 70 and mfi_hour > 80:
                send_telegram_message(f"{symbol['symbol']}: Faça uma ação de mercado chamada 'short' (Encontrado no gráfico de 1 hora)")
            elif rsi_hour < 20 and mfi_hour < 20:
                send_telegram_message(f"{symbol['symbol']}: Faça uma ação de mercado chamada 'long' (Encontrado no gráfico de 1 hora)")
            elif rsi_15min > 70 and mfi_15min > 80:
                send_telegram_message(f"{symbol['symbol']}: Faça uma ação de mercado chamada 'short' (Encontrado no gráfico de 15 minutos)")
            elif rsi_15min < 20 and mfi_15min < 20:
                send_telegram_message(f"{symbol['symbol']}: Faça uma ação de mercado chamada 'long' (Encontrado no gráfico de 15 minutos)")
    
    # Pausa de 15 minutos
    time.sleep(15 * 60)
