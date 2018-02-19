from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, ephem, datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    updater = Updater("546330958:AAF5Ah2_KBeZ8T83USCJUc2Rhe1IDiGsuwE")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet_answer))

    updater.start_polling()
    updater.idle()

def talk_to_me(bot, update):
    user_text = update.message.text 
    update.message.reply_text(user_text)
    
def greet_user(bot, update):    
    update.message.reply_text('Hello!')

def planet_answer(bot,update):

    planets = { "mercury": ephem.Mercury, "venus": ephem.Venus,
            "mars": ephem.Mars, "jupiter": ephem.Jupiter, 
            "saturn": ephem.Saturn, "uranus": ephem.Uranus,
            "neptune": ephem.Neptune, "pluto": ephem.Pluto}

    
    planet = update.message.text 
    planet = planet.lower().replace('/planet ','')
    now = datetime.date.today()
    
    get_method = planets.get(planet)
    get_constellation = get_method(now)
    const = ephem.constellation(get_constellation)
    update.message.reply_text(const[1])



main()