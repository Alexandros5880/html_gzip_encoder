import gzip
import sys

# Example:  python html_gzip_encoder.py hotspot_main.html hotspot_main.html.gz

filepath = "hotspot_main.html.gz"

def create_gzip_file(filepath, gzipfile):
  with open(filepath, mode='r') as f_in:
    str = f_in.read()
    with gzip.open(gzipfile, 'wb') as gzip_file:
      gzip_file.write(str.encode('utf-8'))

def print_decode_gzip_file_to_hex(filepath):
  with gzip.open(filepath, mode='r') as infile:
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
        
def print_decode_gzip_file_to_string(filepath):
  with gzip.open(filepath, mode='r') as infile:
    bytes_result = infile.read()
    text = bytes_result.decode('utf-8')
    print("Len: ", len(text))
    print("\nText:\n")
    line_size = 17
    index = 0
    print(text)
    
if __name__=='__main__':
  htmlfile = sys.argv[1]
  gzipfile = sys.argv[2]
  create_gzip_file(htmlfile, gzipfile)
  print_decode_gzip_file_to_hex(gzipfile)