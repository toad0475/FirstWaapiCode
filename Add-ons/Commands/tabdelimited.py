import os
from waapi import WaapiClient
from tkinter import filedialog
import numpy as np

# get Import files
file =  filedialog.askopenfilenames(initialdir ="C:/",title = "choose your tab Delimited txt file")

# Connect (default URL)
client = WaapiClient()

# RPC
for i in np.asarray(file):
    kwargs = {
        "importLanguage": "SFX", 
        "importOperation": "useExisting",
        "importFile": i, #os.getcwd()+"\\Test1\\Tabimport.txt",
        "autoAddToSourceControl": True }
    result = client.call("ak.wwise.core.audio.importTabDelimited", kwargs)

    print(result)

# Disconnect
client.disconnect()




'''
# Subscribe
handler = client.subscribe(
    "ak.wwise.core.object.created",
    lambda object: print("Object created: " + str(object))
)

# Bind a different callback at any time
def my_callback(object):
    print("Different callback: " + str(object))

handler.bind(my_callback)

# Unsubscribe
handler.unsubscribe()
'''
