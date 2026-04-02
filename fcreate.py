import os
def fcreate():
  folder_name = input('Enter folder name >> ')
  file_name = input('Enter file name >> ')
  file_path = os.path.join(folder_name, file_name)
  text = input('Enter text >> ')
  os.makedirs(folder_name, exist_ok=True)
  with open(file_path, 'w', encoding='utf-8') as f:
      f.write(text)
