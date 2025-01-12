# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

fruits = ["pera", "uva", "Maça", "laranja"]

def alphabetical_order_fruits(list):
    list.sort(key=str.lower)
    return list

print(alphabetical_order_fruits(fruits))