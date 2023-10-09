#Traductor de abreviaturas actuales!

meme_dict = {
            "cringe": "Algo vergonzoso o raro",
            "lol": "Podria significarse la abreviacion del juego League Of Legends o una forma para dar a entender algo gracioso",
            "btw": "Se usa para abreviar la palabra By The Way, que en español significa por cierto, y no se utiliza de una forma en especial, tan solo es una abreviacion para no escribir completa la palabra", 
            "omg": "OMG significa Oh my god, que en español significa Oh mi dios, se puede utilizar como para cuando algo te sorprende, asusta, impacta etc etc etc",
            "cya": "Cya es una abreviacion de la palabra see ya, que en español es como un nos vemos",
            "thx": "Significa Thanks, y en español es Gracias",
            "diy": "En ingles es do It Yourself que en español significa hazlo tu mismo",
            "idk": "En ingles es I dont know, que en español significa No lo se",
            "bf": "En ingles Bf significa Best Friends que en español signfiica mejor amigo, o tambien se puede representar como Boyfriend, osea Novio en español",
            "XD": "Represanta a una risa o carcajada, mas bien XD es como una cara riendose",
            "aka": "Aka significa en ingles Also known as, que en español significa Tambien conocido como",
            "nvm": "Nvm en ingles significa Never mind, que en español se puede interpretar como un ya fue, no importa, no te preocupes, tranqui etc etc etc",
            }
            
preg = input("Escribe la palabra que no entiendas! (Con minuscula!) (Si quieres saber el significado de XD ponlo en mayuscula)")



if preg in meme_dict.keys():
    print(meme_dict[preg])
else:
    print("Lamentablemente no hemos podido encontrar la palabra que estas buscando, si deseas encontrarla busca en otra parte.")
