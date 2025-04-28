class CarteraCripto:
    def __init__(self, usuario, saldo_btc=0.0):
        self.__usuario = usuario
        self.__saldo_btc = saldo_btc

    def consultar_saldo(self):
        return f"Saldo actual de {self.__usuario}: {self.__saldo_btc:.8f} BTC"

    def comprar_btc(self, monto_usd, precio_actual_btc):
        if monto_usd > 0 and precio_actual_btc > 0:
            btc_comprado = monto_usd / precio_actual_btc
            self.__saldo_btc += btc_comprado
            return f"Compra realizada: {btc_comprado:.8f} BTC agregados a la cartera."
        return "Monto o precio inválido."

    def vender_btc(self, monto_btc, precio_actual_btc):
        if monto_btc > self.__saldo_btc:
            return "No se pueden vender más BTC de los disponibles."
        if monto_btc > 0 and precio_actual_btc > 0:
            monto_usd = monto_btc * precio_actual_btc
            self.__saldo_btc -= monto_btc
            return f"Venta realizada: Has recibido {monto_usd:.2f} USD por {monto_btc:.8f} BTC."
        return "Monto o precio inválido."

# Ejemplo de uso:
mi_cartera = CarteraCripto("Usuario123", 0.05)
print(mi_cartera.consultar_saldo())
print(mi_cartera.comprar_btc(500, 30000))  # Compra con USD y precio actual BTC
print(mi_cartera.consultar_saldo())
print(mi_cartera.vender_btc(0.01, 32000))  # Venta con precio actual BTC
print(mi_cartera.consultar_saldo())