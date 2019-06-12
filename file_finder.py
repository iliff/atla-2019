'''
Imports and Globals
-------------------
- [`shutil`](https://docs.python.org/3.7/library/shutil.html) is short for shell utilities.
- [`os`](https://docs.python.org/3.7/library/os.html?highlight=os#module-os) we used it earlier, here we are going to use it two different methods
- Global variables
* They _should never be mutated_ Don't do it!
* Use them when you are setting constants
* Accessing them in different codes
* We are setting them as variables here because they are part of the config These will be different for different OSs
'''

from shutil import copy2
import os
import sys

# Run dir and ls on mac and windows see what the results are
JPEGS_DIR = os.path.join('.', 'sample_directory', 'jpegs')
PDFS_DIR = os.path.join('.', 'sample_directory', 'sub_dir', 'pdfs')
EBOOKS_DIR = os.path.join('.', 'sample_directory', 'ebooks')


'''
Walking directory paths 
-----------------------

- Using os.walk to walk directory paths 
- Assigning variables that you don't need. 
- base names and extensions 

'''
def get_path_names(ext, path):
    print(ext)
    path_dict = {}
    for dirpath, _, fnames in os.walk(path):
        for f in fnames:
            ftup = os.path.splitext(f)
            if ftup[1] == ext:
                path_dict[ftup[0]] = dirpath
    return path_dict


def file_copier(file_name, dir_dict, ext, temp_dir):
  try:
    copy2(os.path.join(dir_dict[file_name], file_name + '.' + ext), temp_dir)
  except (FileNotFoundError, KeyError) as e:
    print(e.args)
    print('File Not Found: {}.{}'.format(file_name, ext))



'''
Putting it all together 
-----------------------
- using nested dictionaries 
- sys as a system tool 
- .items() as a method for iterating through dictionaries 

'''

def main():
  files_dir = {
      'pdf': get_path_names('.pdf', PDFS_DIR),
      'jpeg': get_path_names('.jpeg', JPEGS_DIR),
      'ebook': get_path_names('.ebook', EBOOKS_DIR)
  }
  try:
      temp_dir = sys.argv[2]
  except IndexError:
      os.makedirs('temp', exist_ok=True)
      temp_dir = 'temp'
  with open(sys.argv[1]) as files:
    for fn in files:
      fn = fn.strip() # removing whitespace around the file name
      for ext, dir_dict in files_dir.items():
        file_copier(fn, dir_dict, ext, temp_dir)
  print('Finished')


