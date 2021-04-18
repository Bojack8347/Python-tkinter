import time

import plyer
from plyer import notification
###Author: Tian Qin 4/17/2021
###Version 1
if __name__ == "__main__":
    Frequency__drink_water = 0
    while Frequency__drink_water <=10:

        notification.notify(
            title="**Please Drink Water now!!",
            message=" The U.S. National Academies of Sciences, Engineering, and Medicine determined that"
                    " an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for"
                    " men. About 11.5 cups (2.7 liters) of fluids a day for women",
            app_icon= "water_bottle.ico",
            # displaying time
            timeout=5
        )
        # waiting time
        Frequency__drink_water +=1
        time.sleep(60*30)






