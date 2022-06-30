import discord
import os 

#Sécurité : 
os.system("color 17")
print("Tool dmall by wshl")




dmfriend = discord.Client()

licence = "wshl"
auth = str(input("Mettez votre licence qui vous a été fournis ici >>> "))

#Début du programme : 
if auth == licence :
  print("DMALL Tool By wshl")
  token = str(input("Mettez votre token discord ici >>> "))
  message = str(input("Message à envoyer à vos amis >>> "))

#Début du programme :
  @dmfriend.event
  async def on_connect() :
      print(f"Conexion à"+token)
      print("-----------------------------------------")
      print(dmfriend.user.name)
      print(dmfriend.user.id)
      print("-----------------------------------------")
      print(f"Je commence à envoyer le message : "+message)
      print("-----------------------------------------")

      for user in dmfriend.user.friends :
        try :
            await user.send(message)
            print(f"Message envoyés avec succès à : {user.name}")
        except :
            print(f"Erreur lors de l'envoi du message à : {user.name}")
            print(f"{user.name} n'a pas été dm")
  dmfriend.run(token, bot = False)
else :
    print("Erreur ! Verifiez votre licence ou contactez wshl sur discord")

    
