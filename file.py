from pathlib import Path

# path = Path('ecommerce')
# print(path.exists())
# pathEmail = Path('email')
# print(pathEmail.mkdir())
# print(pathEmail.rmdir())
home = Path() ## Home
# for file in home.glob('*.*'): # all file
for file in home.glob('*'): # all file
    print(file)