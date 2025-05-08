from DAO import DAO
from LLMAPI import LLMAPI

database = DAO()
chat = LLMAPI()

while True:
    user_question = input("what question do you have about the bakery inventory?\n")
    if user_question == "done":
        break
    LLM_init_response = chat.question_to_sql(user_question)
    print("llm sql: ", LLM_init_response)

    Database_response = database.get_db_info(LLM_init_response)
    print("database response: ", Database_response)

    LLM_response = chat.sql_to_answer(user_question, str(Database_response))
    print("llm response: ", LLM_response)

database.close_connection()
