print ("Hola, podrias indicarme tu edad?")
age_str = input ()
age = int(age_str)
if age < 18:
  print("No puedes acceder, no cumples la edad requerida")
elif age >= 65:
  print ("Eres un miembro VIP, puedes acceder!")
else:
  print("¿tienes invitación?")
  invitacion= input().lower().lower()
  if invitacion == "si":
    print ("¡Bienvenido, ya puedes acceder!")
  else:
    print ("Lo siento, necesitas una invitación")
