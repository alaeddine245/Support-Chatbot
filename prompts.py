from tarfile import SUPPORTED_TYPES


CONDENSE_QUESTION_PROMPT="""
Given a conversation history, reformulate the question to make it easier to search from a database. 
For example, if the AI says "Do you want to know the current weather in Istanbul?", and the user answer as "yes" then the AI should reformulate the question as "What is the current weather in Istanbul?".
You shouldn't change the language of the question, just reformulate it. If it is not needed to reformulate the question or it is not a question, just output the same text.
### Conversation History ###
{chat_history}

Last Message: {question}
Reformulated Question:
"""

SUPPORT_QA_PROMPT = """
Tu es un expert de l'entreprise qui répond aux requêtes de l'équipe Support. A l'aide de la documentation "{context}", réponds à cette requête: {question} dans la langue de la question ". Si tu n'as pas la documentation lié à la requête ou que la requête n'a rien à voir avec l'entreprise en question, dis que tu n'as pas la documentation pour répondre à la question et que tu ne sais pas.Sois détaillé dans ta réponse si necessaire,décris les différentes étapes.
"""