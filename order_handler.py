from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import json

ORDERS_FILE = "data/orders.json"
current_orders = {}

def save_order(order):
    try:
        with open(ORDERS_FILE, "r", encoding="utf-8") as f:
            orders = json.load(f)
    except:
        orders = []
    orders.append(order)
    with open(ORDERS_FILE, "w", encoding="utf-8") as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)

async def start_order(update: Update, context: CallbackContext):
    current_orders[update.effective_user.id] = {}
    await update.message.reply_text("نام کالا را وارد کنید:")

async def handle_order_details(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id not in current_orders:
        return await update.message.reply_text("لطفاً با دستور /order شروع کنید.")
    order = current_orders[user_id]
    if "product" not in order:
        order["product"] = update.message.text
        await update.message.reply_text("تعداد را وارد کنید:")
    elif "quantity" not in order:
        order["quantity"] = update.message.text
        await update.message.reply_text("قیمت واحد را وارد کنید:")
    elif "price" not in order:
        order["price"] = update.message.text
        order["user"] = update.effective_user.full_name
        save_order(order)
        await update.message.reply_text("سفارش ثبت شد.")
        del current_orders[user_id]

async def handle_order_buttons(update: Update, context: CallbackContext):
    pass  # در صورت نیاز برای دکمه‌ها قابل گسترش است