from operator import ne
import os
cwd = os.getcwd()
print(f'CWD: {cwd}')

## Make directory
# os.mkdir("TheCure")
# print(os.listdir())

## Make path:
# path = os.path.join('TheCure','Disintegration', 'Plainsong')
# os.makedirs(path)

## Rename file or directory
# os.makedirs(os.path.join('TheCure','Seventeen Seconds'))
# print(os.listdir("TheCure"))

# old_name = os.path.join('TheCure','Seventeen Seconds')
# new_name = os.path.join('TheCure','SeventeenSeconds')
# os.rename(old_name,new_name)

# print(os.listdir("TheCure"))

## Remove directory
os.rmdir(os.path.join('TheCure','SeventeenSeconds'))
# 'TheCure/SeventeenSeconds' is removed, because it was empty

os.rmdir(os.path.join('TheCure','Disintegration'))
# OSError: [Errno 39] Directory not empty: 'TheCure/Disintegration'