import re
import discord

def sanitize_message(msg):
  pattern = r'<a*:[a-zA-Z0-9_]+:[0-9]+>'    # カスタム絵文字/カスタムアニメーション絵文字のパターン
  msg = re.sub(pattern, '', msg)   # 置換処理
  msg = discord.utils.remove_markdown(msg)

  # チャンネル名に使えない記号を置換する
  for w in list('!"#$%&\'()*+,./:;<=>?@[\]^`{|}~ 　'):
    msg = msg.replace(w, '')   # 置換処理

  # 大文字アルファベットも使用禁止にする
  for w in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    msg = msg.replace(w, w.lower())   # 置換処理
  return msg
