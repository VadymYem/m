import abc
import time

from aiogram.types import Message as AiogramMessage
from telethon.utils import get_display_name

from .. import loader, utils
from ..inline.types import InlineCall


@loader.tds
class MenuBotMod(loader.Module):
    """Simple menu for bot"""

    __metaclass__ = abc.ABCMeta

    strings = {
        "name": "ТестBot",
        "/donate": (
            "So you want to donate? Amazing!"
'Donate: https://authorche.pp.ua/donate<br><br>BTC:<code>bc1qmldjc72nym6usckrx4j4d0ynnuv6f0apgve0m4</code><br><br>ETH:<code>0xB5Cf698C9d1f57E810AC213353d4F7e2A8974b59</code><br><br>TON:<code>EQBvlPuI3MsK7NHZ0euU3_lwwrcLfptk3A0eHdO2OFQq63OY</code><br><br>TRX:<code>TM38RYdnxCPfuiqUVma88f4TCZesbeFoLW</code><br><br>BNB: <code>0xB5Cf698C9d1f57E810AC213353d4F7e2A8974b59</code> <br><br>LTC:<code>ltc1qyxqaqapgg4fdyep427s00lszhdxm8x0hcz4e66</code><br><br>USDT:<code>0xB5Cf698C9d1f57E810AC213353d4F7e2A8974b59</code><br><br>'
'You can subscribe to my <a href="https://www.instagram.com/vadym_yem">Instagram</a>.\n'
'<b>This project is entirely run by Author, and server, resources, hosting and services fees aren`t cheap, so I thank you for your support!</b>'
        ),
        "/help": (
         "✌️<b>Привіт, вітаю вас тут\n"
        "Це бот від  @Author_Che</b>:\n\n"
        "Скористайтеся /menu для перегляду функціоналу"  
        ),
        "/author":(
        "Власником боту є @Author_Che. Бот є повністю безкоштовним та не містить жодної реклами. Ціллю створення є бажання спростити користування месенджером Telegram. Також є і інші проекти: @wsinfo. Ви можете підтримати проект — /donate"
        ),
        "/bots":(
        "@authorche_nice_bot - багатофункціональний бот,\n"
        "@vycalc_bot - простий та зручний калькулятор,\n" 
        "@vyfb_bot - бот зворотнього зв'язку з Автором,\n"
        "@horn_star_bot - бот для генерації та розпізнавання QR-кодів,\n" 
        "@Guess_the_number_acbot - гра 'Вгадай число'.\n\n"
        "Також Автор пише простих ботів на замовлення. Якщо вам довподоби робота Автора, можете підтримати його через /donate"
        ),
        "/feedback":(
        "Зворотній зв`язок доступний лише в @vyfb_bot."
        ),
        "/menu": (
        "✌️<b>Привіт, вітаю в меню\n"
        "Команди які ви можете використовувати</b>:\n"
        "/author — <i>Посилання на власника боту</i>\n"
        "/donate — <b><i>Donate❤️</i></b>\n"
"/bots — <i>Список інших ботів від Автора</i>\n"
"/help — <i>Допомога</i>\n"
"/menu — <i>Переглянути функціонал бота</i>\n\n"
"<b>ℹ️ Доступні команди inline:</b>\n"
"🎹 <code>@authorche_nice_bot choice</code> - [аргументи, розділені комою] - Зробити вибір\n"
"🎹 <code>@authorche_nice_bot coin</code> - Орел чи Решка?\n"
"🎹 <code>@authorche_nice_bot random</code> - [Число] - Надіслати випадкове число менше вказаного\n"
"🎹 <code>@authorche_nice_bot info</code> - Подивитися інформацію про бота.\n"
"🎹 <code>@authorche_nice_bot hide</code> - Створює спойлери, які доступні тільки окремим користувачам (hide @usеrname message)\n"
"🎹 <code>@authorche_nice_bot weather</code> - Подивитися погоду(weather місто)\n"
"🎹 <code>@authorche_nice_bot lr</code> - Створити гарне приховане повідомлення (lr text)\n"
"🎹 <code>@authorche_nice_bot ping</code> - Перевірка швидкості роботи бота\n"
"🎹 <code>@authorche_nice_bot tl</code> - Для розробників телеграму"
        ),
    }
    
    async def client_ready(self):
        self._name = utils.escape_html(get_display_name(self._client.acbot_me))
        

        self.__doc__ = (
            "Menu for bot\n"
        )

    async def aiogram_watcher(self, message: AiogramMessage):
        if message.text == "/donate":
            await message.answer(
                self.strings("/donate").format(self._name),
            )
        elif message.text == "/menu":
            await message.answer(self.strings("/menu"))
        elif message.text == "/help":
            await message.answer(self.strings("/help"))
        elif message.text == "/bots":
            await message.answer(self.strings("/bots"))
        elif message.text == "/author":
            await message.answer(self.strings("/author"))
        elif message.text == "/feedback":
            await message.answer(self.strings("/feedback"))
