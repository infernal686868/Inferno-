import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, MessageHandler, filters, CallbackQueryHandler
from modules import order_handler, export_handler, product_handler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "YOUR_BOT_TOKEN"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("سلام! برای ثبت سفارش /order را بزنید. برای جستجوی کالا /search را بزنید.")

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("order", order_handler.start_order))
    application.add_handler(CommandHandler("search", product_handler.search_products))
    application.add_handler(CommandHandler("export", export_handler.export_orders))
    application.add_handler(CallbackQueryHandler(order_handler.handle_order_buttons))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, order_handler.handle_order_details))
    application.run_polling()

if __name__ == '__main__':
    main()