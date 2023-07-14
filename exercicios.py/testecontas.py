# programa criado para ser usado na instanciação dos objetos das duas classes e gerar transações realizadas nas contas dos clientes

from conta import Cliente, Conta

# Criação de um cliente
cliente1 = Cliente('123456789', 'João', 'Rua A, 123')

# Criação de uma conta
conta1 = Conta(cliente1, '001', 1000.0)

# Realiza operações na conta
conta1.depositar(500.0)
conta1.sacar(200.0)

# Gera saldo
conta1.gerarsaldo()