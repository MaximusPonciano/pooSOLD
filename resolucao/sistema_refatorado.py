class Pedidos:
    def processar(self, pedido, tipo_pagamento):
        print(f"Processando o pedido #{pedido['id']} no valor de R$ {pedido['valor']:.2f}...")
        PagamentoMetodo().processar(pedido, tipo_pagamento)
        pedido['status'] = 'concluido'
        print("Pedido concluído com sucesso!\n")
        Notificacao().enviar(pedido)


class Notificacao:
    def enviar(self, pedido):
        print(f"Enviando e-mail de confirmação para {pedido['cliente_email']}...")


class PagamentoMetodo:
    def processar(self, pedido, tipo_pagamento):
        pagamento = None
        if tipo_pagamento == "cartao_credito":
            pagamento = PagamentoCartao()
        elif tipo_pagamento == "boleto":
            pagamento = PagamentoBoleto()
        elif tipo_pagamento == "pix":
            pagamento = PagamentoPix()
        else:
            print("Tipo de pagamento inválido!")
            return

        pagamento.processar(pedido)


class Pagamento:
    def processar(self, pedido):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses")


class PagamentoCartao(Pagamento):
    def processar(self, pedido):
        print(f"Pagando R$ {pedido['valor']:.2f} com cartão de crédito...")


class PagamentoBoleto(Pagamento):
    def processar(self, pedido):
        print(f"Gerando boleto no valor de R$ {pedido['valor']:.2f}...")


class PagamentoPix(Pagamento):
    def processar(self, pedido):
        print(f"Pagando R$ {pedido['valor']:.2f} via Pix...")


if __name__ == "__main__":
    meu_pedido = {
        'id': 123,
        'valor': 150.75,
        'cliente_email': 'cliente@exemplo.com',
        'status': 'pendente'
    }

    pedidos = Pedidos()
    pedidos.processar(meu_pedido, "pix")

    print("-" * 20)

    meu_pedido_2 = meu_pedido.copy()
    meu_pedido_2['id'] = 456
    pedidos.processar(meu_pedido_2, "boleto")
