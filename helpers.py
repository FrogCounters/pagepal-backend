import os
from env import CFG
from expertai.nlapi.cloud.client import ExpertAiClient

os.environ["EAI_USERNAME"] = CFG.mail[0]
os.environ["EAI_PASSWORD"] = CFG.password[0]

client = ExpertAiClient()


def analyse_text(text):
    taxonomy = 'emotional-traits'
    language= 'en'
    output = client.classification(body={"document": {"text": text}}, params={'taxonomy': taxonomy, 'language': language})

    if not output.categories:
        return ""
    else:
        return ",".join(list(map(lambda x: x.hierarchy[1], output.categories)))
