#хэш-таблицы
# Подсчёт количества букв
text = "hello"
hash_table = {}
for ch in text:
    hash_table[ch] = hash_table.get(ch, 0) + 1
print(hash_table)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
from collections import dict
