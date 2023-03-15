
import logging
from telegram import ForceReply, Update, InputMediaPhoto,Bot
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from main import get_cars
import asyncio
import json
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

db = json.load(open('registered_users.json','r'))
def write_to_db(db):
    json.dump(db, open('registered_users.json','w'),indent = 4)
# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Salam, {}. Zəhmət olmasa /avto funksiyasından istifadə edərək istədiyiniz maşın modelini qeyd edin və yeni paylaşılan elanlara baxın'.format(update.effective_user['first_name']))
    chat_id= str(update.effective_user['id'])
    if chat_id not in db['users']:
        db['users'][chat_id]=[]
        write_to_db(db)#sort_keys=True

async def avto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args:
        await update.message.reply_text('Xahiş olunur avtomobilin modelini qeyd edin \nMəsələn, /avto golf')
    else:
        try:
            car = ' '.join(context.args)
            data = get_cars(car)
            for i in range(data.ads_count):
                images = [InputMediaPhoto(i) for i in data.images[i]]
                await update.message.reply_media_group(media=images,caption=data.car[i])
        except KeyError:
            await update.message.reply_text('Yalnış model, yenidən sorğu göndərin')


async def registered_cars(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:


async def unregister_car(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Elanları görmək üçün istifadə edin Məsələn, /avto golf")

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = str(update.effective_user['id'])
    modeller = context.args
    db['users'][user_id].extend(context.args) #[s,s,s,s]
    write_to_db(db)
    await update.message.reply_text('Elave edildi')
    #await update._bot.send_message(chat_id=808173920,text='ddd')

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("5686031636:AAGlVULyOcEhn3b9l1CUstZbUZFhfTvCbK0").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("avto", avto))
    application.add_handler(CommandHandler("add", add))
    # on non command i.e message - echo the message on Telegram
    #application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()