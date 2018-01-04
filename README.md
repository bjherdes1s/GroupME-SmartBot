# GroupME SmartBot

## Introduction
I set out to become more familiar with JSON, specifically POST requests containing JSON data to the 
GroupME and TP-Link API's. The GroupME bot was the easy part. There is an online form at https://dev.groupme.com/bots where you can create
your own bot easily and assign it to a group of your choosing. From here, your bot can be assigned to a callback server. This callback
server should process chats and trigger the HS100 smart plug on or off, depending on the chat message received.

To be used in conjuction with Heroku and deployed with git Heroku tools. 
Without a hosting platform or port forwarding on your own home web server,
your capabilities will be minimal with this GroupME SmartBot. 

### Hardware/Software Necessary

1. TP-Link HS100 Smart Plug
2. A GroupME Account
3. Heroku Tools
4. TP-Link Kasa App for Mobile
5. A Backup/Extraction software for copying the .db (sqlite) and .plist (property list) files of your Kasa mobile app to PC for analysis.

### Purposes of this project

1. Bot reads/analyzes GroupME chat messages in specific group.
2. If message equals a specific trigger and is from a unique user, perform further action.
3. Further action, in my case, is the turning 'on' or 'off' of the TP-Link HS100 smart plug. 
4. Logs of the API calls should be visible in the Heroku App management dashboard.

## DEMO

*Also see the screenshots folder I am including for convenience.*

### Make it your own
1. Change any mention of 'YOUR_BOT_ID_HERE' to your GroupME bot's ID. Another option is to make a heroku config environment variable.
2. Change any mention of 'YOUR_TOKEN_HERE' to your TP-Link access token normally used by the Kasa app. You may have to extract these from a .plist or .db file from the Kasa mobile application.
3. Change any mention of 'YOUR_DEVICEID_HERE' to your smartplug DeviceID. You can find this in your Kasa app's .db file or with an appropriate cURL POST.

*I have included the curlOn.py and curlOff.py scripts, which are just func1() and func2() from the app.py. Having these separately may help in troubleshooting 
the conversation between heroku hosted app and the TP-Link REST API.*

Hope you enjoy,

Contact: [brytonjherdes@gmail.com]
