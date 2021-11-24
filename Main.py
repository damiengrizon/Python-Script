liste = []
for i in range(10):
    liste.append(str(i+1))

f = open("nombres.txt", "w")
#f.writelines(liste)
f.write("\n".join(liste))
f.close
