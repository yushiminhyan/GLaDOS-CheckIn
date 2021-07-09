# GLaDOS-CheckIn

GLaDOS 自动签到与提示 —— 基于Github Action与Telegram Bot  
部分代码参考Repo：https://github.com/xiaomustudent/glados-checkin  

注：仅支持单个账号，不保证签到一定成功

---

## 邀请码：  
```
HB062-QS7DL-5R0XC-M2EA4
```
注：只有通过 https://github.com/glados-network/GLaDOS 进入GLaDOS才能填写邀请码

---

## 使用方法
1. Fork本项目
2. 在项目中打开Settings-Secrets-Actions，创建新的Secrets并将环境变量写入
3. 启用Action中的Workflow
4. 进行任意Push/Pull request以触发Action

注：执行一次Action以后会自动每日签到

## 环境变量：

| 命名 | 解释 |
| --- | --- |
|COOKIES|签到Cookies|
|BOT_TOKEN|Telegram Bot Token|
|CHAT_ID|Telegram Bot Chat Id|

### COOKIES
1. 打开签到网页
2. 打开网页控制台
3. 点击【签到】
4. 获取Network中对checkin的Request Header中的cookie中的所有内容
  
示例：_ga=GA1.2.XXX; _gid=XXX;XXX _gat_gtag_UA_104464600_2=1
  
### BOT_TOKEN
1. 关注Telegram中的[@BotFather](https://telegram.me/BotFather)
2. 根据@BotFather中提示的步骤创建机器人
3. 获取最终得到的机器人Token
  
示例：1000000000:AAAAbbbbCCCCddddEEEEffffGGGGhhhhIII
  
### CHAT_ID
1. 搜索并添加刚才创建的Telegram Bot
2. 向自己Telegram Bot发送一条简单的信息（不是命令）
3. 在浏览器中打开以下地址，并把<Telegram Bot Token>替换为自己机器人的Token
```
https://api.telegram.org/bot<Telegram Bot Token>/getUpdates
```
4. 根据自己发送的信息，获取返回JSON的 result\[0\].message.chat.id，即为CHAT_ID
5. (可选) 在浏览器中打开以下地址进行CHAT_ID测试，并把<Telegram Bot Token>替换为自己机器人的Token，<Telegram Chat Id>替换为CHAT_ID
```
https://api.telegram.org/bot<Telegram Bot Token>/sendMessage?chat_id=<Telegram Chat Id>&text=Test Message
```
  
示例：000000000