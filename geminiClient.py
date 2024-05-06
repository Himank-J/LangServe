import json
from loguru import logger
from schema import invoiceSchema
from kor import create_extraction_chain
from langserve.schema import CustomUserType
from langchain_google_genai import ChatGoogleGenerativeAI

class Parser(CustomUserType):
    text: str

class GeminiModel():

    def __init__(self):
        
        self.__chatllm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            convert_system_message_to_human=True,
            google_api_key = "<key here>",
            max_retries=1,
            temperature=0.1,
            max_output_tokens=2048
        )
    
    def getGeminiResponseKor(self, parser: Parser):

        text = parser.text
        output = {
            "version": "gemini-pro",
            "tags": {},
            "usage": {},
            "isFormatted": False
        }
        try:
            chain = create_extraction_chain(self.__chatllm, invoiceSchema, encoder_or_encoder_class='json')
            prompt_characters = len(chain.prompt.format_prompt(text=text).to_string())
            result = chain.predict(text=text)
            if 'data' in result:
                if 'gpt_data_tagging' in result['data']:
                    tags = result['data']['gpt_data_tagging']
                    isFormatted = True
                    output['tags'] = tags
                    output['isFormatted'] = isFormatted
            
            if len(output['tags']) > 0:
                completion_characters = len(json.dumps(output['tags']))
            else:
                output['isFormatted'] = False
                completion_characters = 0

            prompt_cost = (prompt_characters*0.010)/1000
            completion_cost = (completion_characters*0.031)/1000
            usage = {
                "completion_characters": completion_characters,
                "prompt_characters": prompt_characters,
                "total_characters" : prompt_characters+completion_characters,
                "total_cost": "Rs. " + "{:.3f}".format(round((prompt_cost+completion_cost), 3))
            }
            output['usage'] = usage
            return output
        
        except Exception as e:
            logger.error('geminipro getGeminiResponseKor error: '+str(e))
            return output