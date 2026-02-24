from address import Address
from mailing import Mailing

to_address = Address (428003, "Cheboksary", "Kadykova", 15, 47)
from_address = Address (603000, "Nizhny Novgorod", "Pokrovskaya", 50, 7)
cost = 1500
track = '12345678'

mailing = Mailing (to_address, from_address, 1500, '12345678')

print(mailing)