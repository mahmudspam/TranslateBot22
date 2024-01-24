from googletrans import Translator, LANGCODES


tr = Translator()


async def translate_text(text: str, lang: str):
    # print(LANGCODES)
    return tr.translate(text, dest=lang).text

