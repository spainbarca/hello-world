def operation(quantity, balance, type='deposit'):

    def deposit(quantity, balance):
        return quantity + balance
    
    def retire(quantity, balance):
        if quantity<= balance:
            return balance - quantity
        else:
            return None
    
    #print(deposit(10,20))
    #print(retire(70,80))

    if type == 'deposit':
        return deposit(quantity, balance)
    elif type == 'retire':
        return retire(quantity, balance)

resultado = operation(10, 30, 'retire')
print(resultado)