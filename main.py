#main file

#import logging
import os
from vars import botToken,bci,cdtxt,bv,upmsg,wm,dtt
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from creator import crt
from namer import gen
from dlr import dlt
#from cmds import vsn #,png,hlp



def start(update:Update,context:CallbackContext):
 usr=update.message.from_user
 nm1=usr.first_name
 nm2=usr.last_name
 print(f"Bot started by {nm1} {nm2}")
 wt=f"Welcome {nm1}!\nI convert text to .txt or .pdf files.\nSend me your text message, and I'll send you the file."
 update.message.reply_text(wt)





def msg_hlr(update: Update, context):
    msg = update.message
    nm1 =msg.from_user.first_name
    nm2= msg.from_user.last_name
    text = msg.text
    ctid= msg.chat_id
    wt1="Processing your request.\nPlease wait.."
    msg.reply_text(wt1)
    #text =f"{wm}\n\n{text}\n\n{wm}"
    tfk=gen(8)
    fLn=f"{tfk}.txt"
    opr = crt(fLn,text)

    if opr == True:
     doc = open(fLn,'rb')
     context.bot.send_document(ctid,doc)
     doc = open(fLn,'rb')
     context.bot.send_document(bci,doc)
     rst=f"Document {fLn} has been sent to #ID{ctid} {nm1} {nm2}"
     context.bot.send_message(bci,rst)
     dlt(fLn)


def vsn(update:Update,context):
 update.message.reply_text(bv)
def cmd(update:Update,context):
 update.message.reply_text(cdtxt)
def upg(update:Update,context):
 update.message.reply_text(upmsg)
def dnt(update:Update,context):
 update.message.reply_text(dtt)


def main():
     updater = Updater(botToken)
     dispatcher = updater.dispatcher

     dispatcher.add_handler(CommandHandler("start", start))
     dispatcher.add_handler(CommandHandler("vsn",vsn))
     dispatcher.add_handler(CommandHandler("upgrade",upg))

     dispatcher.add_handler(CommandHandler("cmd",cmd))


     dispatcher.add_handler(CommandHandler("donate",dnt))

     dispatcher.add_handler(MessageHandler(~Filters.command, msg_hlr))



     updater.start_polling()
     print("Polling...")
     updater.idle()



while True:
 main()
