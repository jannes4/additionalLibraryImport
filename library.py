import shutil
import os

try:
  path = os.path.expanduser("~/Desktop") + '\\VALORANT.lnk'
  os.remove(path)
except:
  pass
