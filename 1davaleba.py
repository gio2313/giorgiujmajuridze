with open("davaleva.txt", "r") as file:
    content = file.readlines()

moreze = {}
a = input("airchiet operaciis tipi: dashifrva/ganshifrva: ")
b = input("sheiyvanet teqsti: ")

for i in content:
    shipri, aso = i.split(":")
    moreze[shipri] = aso
    moreze[aso] = shipri
if a == "dashifrva":
    for j in b:
        print(moreze.get(b))