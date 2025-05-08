from openai import OpenAI

class LLMAPI:
    def __init__(self):
        self.client = OpenAI()
        with open("instruction_prompt.txt", "r", encoding="utf-8") as file:
            self.instructions = file.read()

    def question_to_sql(self, question):
        response = self.client.responses.create(
            model="gpt-4o-mini",
            instructions=self.instructions,
            input=question
        )

        return response.output_text

    def sql_to_answer(self, sql):
        response = self.client.responses.create(
            model="gpt-4o-mini",
            instructions=self.instructions,
            input=sql
        )

        return response.output_text
