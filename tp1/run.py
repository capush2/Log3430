import os

if os.path.exists(".coverage"):
  os.remove(".coverage")

os.system("coverage run -m --source=. --branch unittest")
os.system("coverage report")