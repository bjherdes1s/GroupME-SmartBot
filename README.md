# GroupME SmartBot

## Introduction
I set out to become more familiar with JSON, specifically POST requests containing JSON data to the 
GroupME and TP-Link API's. The GroupME bot was the easy part. There is an online form at the [GroupME Developers Page](dev.groupme.com/bots) where you can even create
your own bot easily and assign it to a group of your choosing. From here, your bot can be assigned to a callback server. This callback
server should process chats and trigger the HS100 smart plug on or off, depending on the chat message received.

To be used in conjuction with Heroku and deployed with git Heroku tools. 
Without a hosting platform or port forwarding on your own home web server,
your capabilities will be minimal with a groupme bot. 

### Hardware/Software Necessary

1. TP-Link HS100 Smart Plug
2. A GroupME Account
3. Heroku Tools
4. TP-Link Kasa App for Mobile

### Purposes of this project

1. Bot reads/analyzes GroupME chat messages in specific group.
2. If message equals a specific trigger and is from a unique user, perform further action.
3. Further action, in my case, is the turning 'on' or 'off' of the TP-Link HS100 smart plug. 
4. Logs of the API calls should be visible in the Heroku App management dashboard.

*For a full implementation of this project, the GROUPME and TP-Link REST API's must be utilized, 
specifically for the Kasa App-like POST request.*



Contact: [brytonjherdes@gmail.com]
