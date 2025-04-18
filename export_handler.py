import json
import csv
from telegram import Update
from telegram.ext import CallbackContext

ORDERS_FILE = "data/orders.json"

def export_to_csv():
    try:
        with open(ORDERS_FILE, "r", encoding="utf-8") as f:
            orders = json.load(f)
    except:
        return None

    csv_path = "data/orders_export.csv"
    with open(csv_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["user", "product", "quantity", "price"])
        writer.writeheader()
        for order in orders:
            writer.writerow(order)
    return csv_path

async def export_orders(update: Update, context: CallbackContext):
    csv_file = export_to_csv()
    if csv_file:
        await update.message.reply_document(open(csv_file, "rb"))
    else:
        await update.message.reply_text("سفارشی برای خروجی یافت نشد.")