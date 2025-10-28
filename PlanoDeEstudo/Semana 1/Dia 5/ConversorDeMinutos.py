#Converte minutos em horas

#Recebe os minutos a serem convertidos
minutos = int(input("Digite quantos minutos você quer converter: "))

#Calcula as horas inteiras(e os minutos se tiver)
horas_finais = minutos // 60
minutos_finais = minutos % 60

#Mostra o resultado
print(f"Os minutos convertidos resultam em {horas_finais}h{minutos_finais}m")