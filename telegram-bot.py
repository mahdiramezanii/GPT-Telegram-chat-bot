from telegram.ext import *
import openai

API_KEY="*****************************************"

OPEN_AI="*********************************************"




openai.api_key ="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"

models = {
    "model1": {
        "model": "GPT-3",
        "max_tokens": 5,
        "temperature": 0.7
    },
    "model2": {
        "model": "text-davinci-003",
        "max_tokens": 1000,
        "temperature": 0.1
    }
}


def ask(question, model_name):
    model = models[model_name]["model"]
    max_tokens = models[model_name]["max_tokens"]
    temperature = models[model_name]["temperature"]
    prompt = f"Model prompt >>> {question} Answer:"
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
    )
    message = completions.choices[0].text.strip()

    return message


def generate_text(prompt):
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message.strip()
    




def help_command(update,command):


    return update.message.reply_text("کمکی در کار نیست")


def start_command(update,conext):

    
    return update.message.reply_text("سلام و درو به ربات تلگرام انجمن علمی کامپیوتر خوش اومدین،این ربات از ربات بسیار قدرتمند CHAT-GPT-3.5 قدرت گرفته است.(این ربات توسط مهدی رمضانی ساخته شده است)")

def message(update,context):
    

    res=ask(update.message.text,"model2")
   

    update.message.reply_text(res, reply_to_message_id=update.message.message_id)


    return update.message.reply_text(res, reply_to_message_id=update.message.message_id)



dp=ApplicationBuilder().token(API_KEY).build()

dp.add_handler(CommandHandler("start",start_command))
dp.add_handler(CommandHandler("help",help))
dp.add_handler(CommandHandler("gpt",message))




dp.run_polling(5)
dp.idle()
