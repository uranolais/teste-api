import json

Quantidade_de_Pedidos = int(input("Digite a quantidade de pedidos: "))
Prato = [0] * Quantidade_de_Pedidos
Bebida = [0] * Quantidade_de_Pedidos
pedidos = {"pedidos": []}

for i in range(Quantidade_de_Pedidos):
    Prato[i] = input("Digite o nome do prato : ")
    Bebida[i] = input("Digite o nome da bebida: ")

for j in range(Quantidade_de_Pedidos):
    pedidos["pedidos"].append(
        {
            "Prato": Prato[j],
            "Bebida": Bebida[j]
        }
    )


with open("Pedidos.json", "w") as arquivo:     
    json.dump(pedidos, arquivo, indent=4)