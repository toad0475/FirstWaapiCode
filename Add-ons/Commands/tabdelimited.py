import os
from waapi import WaapiClient


# Connect (default URL)
client = WaapiClient()

# RPC
kwargs = {
    "importLanguage": "SFX", 
    "importOperation": "useExisting",
    "importFile": os.getcwd()+"\\Test1\\Tabimport.txt" }
result = client.call("ak.wwise.core.audio.importTabDelimited", kwargs)



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