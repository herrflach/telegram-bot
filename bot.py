from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

# 🔒 Safety Check (wichtig für Railway)
if not TOKEN:
    raise RuntimeError("BOT_TOKEN fehlt in den Environment Variables")


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            "Hallo! 🦆\n\n"
            "Ich bin der Bot für die Bambule Preparty am 09.05.2025 und begleite dich Schritt für Schritt. :)\n\n"
            "Wenn du starten möchtest, antworte einfach mit /weiter."
        )


# /weiter
async def weiter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            "Schön, dass du dabei sein möchtest!\n\n"
            "Im Rahmen des Bambule wollen wir einen Raum schaffen, in dem wir uns frei entfalten und fallen lassen können. "
            "Dafür ist es wichtig, dass wir einander achten, unterstützen und respektieren.\n\n"
            "Wir stehen mit unseren Werten für Feminismus, Toleranz, Solidarität und Antikapitalismus. "
            "Du bist willkommen – egal, woher du kommst, ob du einen Glauben hast oder wie du dich (a)sexuell orientierst.\n\n"
            "Dementsprechend stellen wir uns beim Bambule aktiv gegen all jene Positionen, mit denen Menschenfeinde uns das Leben schwer machen: "
            "sei es Rassismus, Sexismus, Queerfeindlichkeit, Ableismus, religiöse Diskriminierung oder andere Formen der Ausgrenzung und Entfremdung.\n\n"
            "Beim Bambule werden wir diese Grundüberzeugungen auf den Dancefloors, auf der Bühne und in der Organisation leben, durchsetzen und hochhalten.\n\n"
            "Wir erwarten von allen, die Teil des Bambule-Kosmos sind, dass sie diese Grundwerte teilen, respektieren und mittragen.\n\n"
            "Mit '/verstanden' bestätigst du für dich und die Menschen, die du mitbringst, "
            "dass ihr diese Grundsätze gelesen habt, sie akzeptiert und aktiv unterstützt."
        )


# /verstanden
async def verstanden(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            "Danke, dass du zu einem respektvollen und achtsamen Miteinander beiträgst.\n\n"
            "Wir möchten darauf hinweisen, dass die Preparty aufgrund neuer Organisationsstrukturen vom diesjährigen Bambule Festival losgelöst ist.\n\n"
            "Das Bambule-Team ist auf 21 Organisatorinnen gewachsen. Wir sind viele fleißige Hände, die auch viele Freundinnen haben, "
            "die sie zum Festival einladen möchten.\n\n"
            "Das bedeutet, dass nicht alle aus den vergangenen Jahren und alle Gäste unserer Preparty automatisch auf der Gästeliste für das kommende Festival stehen können.\n"
            "Das tut uns sehr leid, ist organisatorisch jedoch nicht anders zu regeln, da wir für alle Orga-Mitglieder die gleichen Privilegien gewährleisten möchten.\n\n"
            "Umso mehr freuen wir uns darauf, bei der Preparty gemeinsam mit euch eine schöne Zeit zu verbringen und das Zusammensein zu feiern.\n\n"
            "Wenn du die Informationen zur Kenntnis genommen hast, kannst du dies bitte mit\n"
            "/akzeptieren bestätigen."
        )


# /akzeptieren
async def akzeptieren(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            "Geschafft! 💫\n\n"
            "Hier ist alles weitere, was du brauchst:\n"
            "• Telegram-Gruppe: https://t.me/+_caJP_eu_41jZjdi\n"
            "• Gästeliste: https://docs.google.com/forms/d/e/1FAIpQLSfZbUQFMCx8It2QzV2owH7LzjBe1J21PeFjyKiiXFEHXm2BbA/viewform?usp=publish-editor"
        )


# Bot starten
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("weiter", weiter))
app.add_handler(CommandHandler("verstanden", verstanden))
app.add_handler(CommandHandler("akzeptieren", akzeptieren))

app.run_polling()
