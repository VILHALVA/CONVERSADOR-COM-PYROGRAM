from pyrogram import Client, filters
from WORD import keywords

# Usando a sessão salva "my_account.session"
app = Client("my_account")

@app.on_message(filters.private)
async def reply_message(client, message):
    text = message.text.lower()  
    
    # Verifica se alguma palavra-chave está presente na mensagem e envia a resposta correspondente
    for keyword, response in keywords.items():
        if keyword in text:
            await message.reply(response)
            return
    
    # Se nenhuma palavra-chave for encontrada, envia uma mensagem padrão
    await message.reply("EU NÃO ENTENDO QUE DIZES")

app.run()
