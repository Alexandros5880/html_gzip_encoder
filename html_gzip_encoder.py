import gzip
import sys

filepath = "hotspot_main.html.gz"

def create_gzip_file(filepath, gzipfile):
  with open(filepath, mode='r') as f_in:
    str = f_in.read()
    with gzip.open(gzipfile, 'wb') as gzip_file:
      gzip_file.write(str.encode('utf-8'))

def print_decode_gzip_file_to_hex(gzip_file):
  with gzip.open(gzip_file, mode='r') as infile:
    bytes_result = infile.read()
    text = bytes_result.decode('utf-8')
    hex_array = []
    for c in text:
      hex_array.append("0x" + c.encode('utf-8').hex())
    print("Len: ", len(hex_array))
    print("\nArray:\n")
    line_size = 17
    index = 0
    for c in hex_array:
      index += 1
      if index == line_size:
        index = 0
        print(c, end=",\n")
      else:
        print(c, end=", ")
        
def print_decode_gzip_file_to_string(gzipfile, filepath):
  with gzip.open(gzipfile, mode='r') as infile:
    bytes_result = infile.read()
    text = bytes_result.decode('utf-8')
    print("Len: ", len(text))
    print("\nText:\n")
    print(text)
    with open(filepath, mode='w') as f_out:
      f_out.write(text)
    
if __name__=='__main__':
  option = sys.argv[1]
  if option == 'e':
    text_file = sys.argv[2]
    gzip_file = sys.argv[3]
    create_gzip_file(text_file, gzip_file)
    print_decode_gzip_file_to_hex(gzip_file)
  elif option == 'd':
    gzip_file = sys.argv[2]
    text_file = sys.argv[3]
    print_decode_gzip_file_to_string(gzip_file, text_file)