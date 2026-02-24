from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "IPhone 13", +79051004567),
    Smartphone("Samsung", "Galaxy S25", +79001004565),
    Smartphone("Xiaomi", "15 Ultra", +79051454567),
    Smartphone("HONOR", "Magic 8 Pro", +79004009876),
    Smartphone("Tecno", "Camon", +79654568976)

]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
