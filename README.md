
## This simple program is designed to remind Zhuoyi Shen of drinking water on time.



###Step 1 Analyze the program logic:

(1) Trigger event: Time (e.g. notifying Szy every 30 minutes)
(2) Fix the times for reminding or just set a forever loop (while true)
(3) Message/title
(4) Bundling all codes to make it an exe.


###Step 2 Which package we can use

For triggering event, I used plyer.notification function :

        notification.notify(
            title="**",
            message="",
            app_icon= "",
            # displaying time
            timeout=5

        )

###Step 3 Looping

Add a out loop to control the total times of reminders.

while counts <= 10:
    pass


    counts+=1

###Step 4 Pyinstaller

 Pyinstaller -F -w -i  xxx.ico xx.py --hidden-import plyer.platforms.win.notification


Reference:
 (1)https://stackoverflow.com/questions/56281839/issue-with-plyer-library-of-python-when-creating-a-executable-using-pyinstaller
 (2)https://www.lagou.com/lgeduarticle/73122.html
