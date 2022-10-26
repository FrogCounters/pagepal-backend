import os
from env import mail, password
from expertai.nlapi.cloud.client import ExpertAiClient

os.environ["EAI_USERNAME"] = mail
os.environ["EAI_PASSWORD"] = password

client = ExpertAiClient()


def analyse_text(text):
    detector = 'hate-speech'
    taxonomy = 'emotional-traits'
    language= 'en'

    output = client.classification(body={"document": {"text": text}}, params={'taxonomy': taxonomy, 'language': language})

    # output = client.detection(body={"document": {"text": text}}, params={'detector': detector, 'language': language})

    # i = 1
    # for extraction in output.extractions:
    #     print("Record #{}:".format(i))
    #     for field in extraction.fields:
    #         print("{} = {}".format(field.name, field.value))
    #     i = i + 1

    # for category in output.categories:
    #     print(category.id_, category.hierarchy, sep="\t")

    if not output.categories:
        return ""
    else:
        return ",".join(list(map(lambda x: x.hierarchy[1], output.categories))) + ","


# analyse_text("I HATE YOU SO MUCH. get loss. you are so bad fat and ugly.")