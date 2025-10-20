O código original tinha esses problemas:

SRP: ProcessadorDePedidos fazia pedido, pagamento e notificação ao mesmo tempo.

OCP: Para adicionar novo pagamento ou notificação, precisava mudar a classe.

DIP: Dependia de implementações concretas, não de abstrações.