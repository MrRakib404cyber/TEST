import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from PY6 import RIKI
 
        RIKI()
 
 
 
elif bit == "32bit":
 
        from PY3 import RIKI
 
 
        RIKI()
 
 
 
