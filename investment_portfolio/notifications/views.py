import telepot
import logging
import json

from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponseForbidden, HttpResponseBadRequest, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from .models import Bot, Chat, Message, User as TelegramUser
from annoying.functions import get_object_or_None

# Create your views here.
'''
from xml.etree import cElementTree
import requests
def parse_planetpy_rss():
    """Parses first 10 items from http://planetpython.org/rss20.xml
    """
    response = requests.get('http://planetpython.org/rss20.xml')
    parsed_xml = cElementTree.fromstring(response.content)
    items = []
    for node in parsed_xml.iter():
        if node.tag == 'item':
            item = {}
            for item_node in list(node):
                if item_node.tag == 'title':
                    item['title'] = item_node.text
                if item_node.tag == 'link':
                    item['link'] = item_node.text
            items.append(item)
    return items[:10]
logger = logging.getLogger('telegram.bot')
TOKEN = '359099786:AAH3vhHAHqt1E1_V4FNzVIbczFoTKMGwWlU'
'''
TelegramBot = telepot.Bot('359099786:AAH3vhHAHqt1E1_V4FNzVIbczFoTKMGwWlU')


def _display_help():
    return render_to_string('tmb/help.md')

def _display_planetpy_feed():
    return render_to_string('tmb/feed.md', {'items': parse_planetpy_rss()})

def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None

def in_storage(unique_code):
    return TelegramUser.objects.filter(unique_code=unique_code).exists()

def get_username_from_storage(unique_code): 
    telegramuser = get_object_or_None(TelegramUser, unique_code=unique_code)
    if telegramuser:
        telegramuser.is_authorized = True
        telegramuser.save()
    return telegramuser if in_storage(unique_code) else None

def save_chat_id(chat_id, username, type):
    chat, created = Chat.objects.get_or_create(chat_id=chat_id)
    chat.type = type
    chat.user = username
    chat.save()
    return chat

def save_message(chat_id, message):
    message, created = Message.objects.get_or_create(message_id=message['message_id'])
    chat, created = Chat.objects.get_or_create(chat_id=chat_id)
    message.chat_id = chat
    message.save()
    return message


class CommandReceiveView(View):
    def post(self, request, bot_token):
        bot = get_object_or_404(Bot, api_key=bot_token)
        body_unicode = request.body.decode('utf-8')
        payload = json.loads(json.dumps(body_unicode))

        try:
            payload = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return HttpResponseBadRequest('Invalid request body')        
        else:
            chat_id = payload['message']['chat']['id']
            type = payload['message']['chat']['type']
            text = payload['message']['text']  # command
            message = payload['message']

        unique_code = extract_unique_code(text)
        if unique_code:
            username = get_username_from_storage(unique_code)
            if username:
                save_chat_id(chat_id, username, type)

                reply = "Привет {0}, аутентификация успешно пройдена!".format(username)
            else:
                reply = 'К сожалению, я не могу вас аутентифицировать :('    
        else:
            reply = 'Мне нечего Вам ответить. Я предназначен только для аутентификации и информирования.' 
        bot.sendMessage(bot, chat_id, reply)
        save_message(chat_id, message)
        
        return JsonResponse({}, status=200)
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CommandReceiveView, self).dispatch(request, *args, **kwargs)


def telegram_auth(request):
    user = get_object_or_404(User, id=request.user.id)
    telegram_user, created = TelegramUser.objects.get_or_create(user=user)
    bot = Bot.objects.first()
    try:
        unique_code = telegram_user.unique_code
        return redirect('https://telegram.me/{}?start={}'.format(bot.username, unique_code))
    except Exception as e:
        return HttpResponse(e)