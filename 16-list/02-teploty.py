import random

teploty=[]
n_dni=30
for i in range(n_dni):
    teploty.append(random.randint(10,30))
for i in range(n_dni):
    print(f"{i+1}.den - {teploty[i]}°C")

# avg_tep=sum(teploty)/n_dni
# print(avg_tep)

sucet=0
for i in range(n_dni):
    sucet+=teploty[i]

avg_tep=sucet/n_dni
print(f"priemerna teplota v mesiaci je {avg_tep}°C")

for i in range(30):
    if teploty[i]<avg_tep:
        print(f"dni z podpriemernou teplotou: {i+1}.den")