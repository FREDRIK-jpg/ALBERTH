list_vokal = ["A", "I", "U", "E", "O"]
nama = "Fredrik A Tamunete"
vokal = 0

for huruf in nama:
   for huruf_vokal in list_vokal:
      if huruf.upper() == huruf_vokal:
         vokal += 1
         pass
print(vokal)