hora_extra = int(input("Digite suas horas extras:"))
hora_falta = int(input("Digite suas horas faltadas:"))
if hora_extra > (hora_falta * 1.5):
    print("Bonus de R$ 500.00")
else: print("Sem bonus.")