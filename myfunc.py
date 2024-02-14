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
                speak = "bienvenue dans ma poupee "
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
                    case "AMAZON.CancelIntent":
                        speak = "ok"
                    case "FriendIntent":
                        speak = "j'ai beaucoup d'amies"
                    case "PartyIntent":
                        speak = "je veux toujours faire la fête toujours sortir"
                    case "PartiesIntent":
                        speak = " je suis jamais decoiffée"
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
