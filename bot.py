from aiogram.types import Message, FSInputFile, InlineKeyboardButton, \
    InlineKeyboardMarkup, InputMediaPhoto


class MainMenu:
    """
    Основной класс - главное меню
    Содержит в себе все основные функции для сущностей бота: меню и сценарии
    """
    def __init__(self):
        self.picture = 'img/pic1.jpg'
        self.text = 'Добро пожаловать'
        self.buttons = [
            [InlineKeyboardButton(text="Профиль", callback_data="profile")],
            [InlineKeyboardButton(text="Настройки", callback_data="settings")]
        ]


    async def start(self, message: Message):
        """
        Отправляет сообщение с главным меню после запуска бота
        """
        buttons = InlineKeyboardMarkup(
            inline_keyboard=self.buttons
        )
        photo = FSInputFile(self.picture)
        await message.answer_photo(
            photo=photo,
            caption=self.text,
            reply_markup=buttons
        )


    async def change_media(self, message: Message):
        """
        Редактирует существующего сообщения:
        меняет фото, подпись и кнопки
        """
        content = InputMediaPhoto(media=FSInputFile(self.picture), caption=self.text)
        buttons = InlineKeyboardMarkup(inline_keyboard=self.buttons)

        await message.edit_media(media=content)
        await message.edit_reply_markup(reply_markup=buttons)



class ProfileScene(MainMenu):
    """
    Класс, наследуемый от класса меню
    Содержит в себе помимо унаследованных свои необходимые
    бизнес-логике методы
    """
    def __init__(self, picture: str, text: str):
        super().__init__()
        self.picture = picture
        self.text = text
        self.buttons = [
            [InlineKeyboardButton(text="Изменить имя в боте", callback_data="change_name")],
            [InlineKeyboardButton(text="Вернуться в главное меню", callback_data="main_menu")],
        ]

    async def edit_profile(self, message: Message):
        user = User()
        await user.change_profile_name()

class User:
    def __init__(self):
        pass

    async def change_profile_name(self):
        pass

    async def exit(self):
        pass