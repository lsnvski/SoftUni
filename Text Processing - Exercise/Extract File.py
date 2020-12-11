
path = input().split("\\")
path = path[-1].split(".")


print(f'File name: {path[0]}\n'
      f'File extension: {path[1]}')
