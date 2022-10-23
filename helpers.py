import os
from env import mail, password
from expertai.nlapi.cloud.client import ExpertAiClient

os.environ["EAI_USERNAME"] = mail
os.environ["EAI_PASSWORD"] = password

client = ExpertAiClient()


def analyse_text(text):
    taxonomy = 'emotional-traits'
    language= 'en'
    output = client.classification(body={"document": {"text": text}}, params={'taxonomy': taxonomy, 'language': language})

    if not output.categories:
        return ""
    else:
        return ",".join(list(map(lambda x: x.hierarchy[1], output.categories)))
