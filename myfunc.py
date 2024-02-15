import json

def lambda_handler(event, context):
    # TODO implement
    print(event)
    print("hi")
    myhash=None
    try:
        shouldendsessions=False
        myexpr = event["request"]["type"]
        
        print(myexpr)
        match myexpr:
            case "LaunchRequest":
                speak = "bienvenue dans ma pote virtuel "
            case _:
                try:
                    myotherexpr = event["request"]["intent"]["name"]
                except:
                    myotherexpr = "Erreur"
                match myotherexpr:
                    case "Erreur":
                        speak="désolé je ne comprends pas ce que vous me demandez"
                    case "AMAZON.StopIntent":
                        shouldendsessions=True
                        speak = "ok ! si tu dois partir maintenant, à bientôt!"
                    case "AMAZON.HelpIntent":
                        speak = "demande moi pourquoi je suis toujours bien coiffée ce que j'aime manger ou si une personne est mon amie"
                    case "AMAZON.NavigateHomeIntent":
                        speak = "demandez moi quelque chose"
                    case "AMAZON.FallbackIntent":
                        speak = "j'ai pas compris"
                    case "AMAZON.CancelIntent":
                        speak = "ok"
                    case "FriendIntent":
                        potea=""
                        poteb=""
                        potec=""
                        poted=""
                        try:
                            potea = event["request"]["intent"]["slots"]["potea"]["slotValue"]["value"]
                        except:
                            potea = ""
                        try:
                            poteb = event["request"]["intent"]["slots"]["poteb"]["slotValue"]["value"]
                        except:
                            poteb = ""
                        try:
                            potec = event["request"]["intent"]["slots"]["potec"]["slotValue"]["value"]
                        except:
                            potec = ""
                        try:
                            poted = event["request"]["intent"]["slots"]["poted"]["slotValue"]["value"]
                        except:
                            poted = ""
                        speak = "j'ai beaucoup d'amies, je suis comme "
                        x=[potea,poteb,potec,poted]
                        z=[]
                        for y in x:
                            if y != "":
                                z.append(y)
                        a=0
                        for x in z:
                            if a == (len(z) - 1):
                                speak += " et"
                            else:
                                speak += ", "
                            speak += " "+x
                            a+=1
                    case "HelloWorldIntent":
                        speak = "bonjour, je suis ta pote virtuelle, que voudrais tu me demander ?"
                    case "PrettyIntent":
                        speak = "bien sûr, je t'impressionne, tu ne me connais pas?"
                    case "SadIntent":
                        speak = "même quand mes yeux coulent comme des diamants,  j'ai encore envie de faire la fête"
                    case "PartyIntent":
                        speak = "je veux toujours faire la fête toujours sortir"
                    case "CityIntent":
                        speak = " j'habite à "
                        try:
                            hey = event["request"]["intent"]["slots"]["ville"]["resolutions"]["resolutionsPerAuthority"][0]["values"]["value"]["name"]
                        except:
                            hey = event["request"]["intent"]["slots"]["ville"]["slotValue"]["value"]
                        speak += hey
                        speak += " et j'aime la ville"
                    case "PartiesIntent":
                        speak = " je suis jamais decoiffée"
                        try:
                            hey = event["request"]["intent"]["slots"]["partie"]["resolutions"]["resolutionsPerAuthority"][0]["values"]["value"]["name"]
                        except:
                            hey = event["request"]["intent"]["slots"]["partie"]["slotValue"]["value"]
                        speak += " et je ne sais pas pourquoi mes "
                        speak += hey
                        speak += " sont toujours comme ça"
                    case "NeedIntent":
                        speak = "je le fais pour de faux"
    except Exception as e:
        speak = "Désolée , il y a eu une erreur "
    if not myhash:
    	myhash= {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "SSML",
                "ssml": "<speak>"+speak+"</speak>"
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "SSML",
                    "ssml": "<speak>J'ai pas compris, comment ?</speak>"
                }
            },
            "shouldEndSession": shouldendsessions
        },
        "userAgent": "ask-node/2.3.0 Node/v8.10.0",
        "sessionAttributes": {}
    	}
    return myhash
