import os
from waapi import WaapiClient
from tkinter import filedialog
import numpy as np

# Get files path
files = filedialog.askopenfilenames(
    initialdir ="C:/",
    filetypes =(("Text File", "*.txt"),("All Files","*.*")), 
    title = "choose your tab Delimited txt file"
    )

# Connect (default URL)
client = WaapiClient()

# RPC
for file in np.asarray(files):
    kwargs = {
        "importLanguage": "SFX", 
        "importOperation": "useExisting",
        "importFile": file,
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
