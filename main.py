from DAO import DAO
from LLMAPI import LLMAPI

database = DAO()
chat = LLMAPI()


user_question = input("what question do you have about the bakery inventory?\n")
LLM_init_response = chat.question_to_sql(user_question)

Database_response = database.get_db_info(LLM_init_response)
LLM_response = chat.sql_to_answer(Database_response)

print(LLM_response)

database.close_connection()
