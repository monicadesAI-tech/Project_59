#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Drink Water Notification Reminder App

# pip install plyer

# In[ ]:


import time
from plyer import notification #pip install plyer
# You can invoke these from windows task scheduler also.


if __name__=="__main__":
    while True:
        notification.notify(title = "Please Drink Water Now",
                            message = "Drinking Water Helps Maintain the Balance of Body Fluids.",
                            app_icon = r"C:\Users\Monica\Desktop\Projects\Python Projects 1\game\water-glass.ico",
                            timeout = 5)
        time.sleep(60*60)
    
#It may improve memory and mood.
#It may reduce headaches and migraines.
#It may help prevent constipation.
#It may help to prevent kidney stones.


# In[ ]:




