from telegram import Update
from telegram.ext import CallbackContext

PRODUCTS_FILE = "data/products.txt"

def load_products():
    try:
        with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    except:
        return []

async def search_products(update: Update, context: CallbackContext):
    if context.args:
        query = " ".join(context.args).lower()
        products = load_products()
        result = [p for p in products if query in p.lower()]
        if result:
            await update.message.reply_text("\n".join(result))
        else:
            await update.message.reply_text("کالایی یافت نشد.")
    else:
        await update.message.reply_text("لطفاً نام کالا را وارد کنید. مثال: /search شامپو")