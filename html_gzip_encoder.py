import gzip
import sys
from io import StringIO, BytesIO

filepath = "hotspot_main.html.gz"

def string_to_bytes(input_str: str) -> bytes:
    """
        Read the given string, encode it in utf-8, gzip compress
        the data and return it as a byte array.
    """
    bio = BytesIO()
    bio.write(input_str.encode("utf-8"))
    bio.seek(0)
    stream = BytesIO()
    compressor = gzip.GzipFile(fileobj=stream, mode='w')
    while True:  # until EOF
        chunk = bio.read(8192)
        if not chunk:  # EOF?
            compressor.close()
            return stream.getvalue()
        compressor.write(chunk)

def bytes_to_string(input_bytes: bytes) -> str:
    """
        Decompress the given byte array (which must be valid
        compressed gzip data) and return the decoded text (utf-8).
    """
    bio = BytesIO()
    stream = BytesIO(input_bytes)
    decompressor = gzip.GzipFile(fileobj=stream, mode='r')
    while True:  # until EOF
        chunk = decompressor.read(8192)
        if not chunk:
            decompressor.close()
            bio.seek(0)
            return bio.read().decode("utf-8")
        bio.write(chunk)
    return None

def create_gzip_file(filepath, gzipfile):
  with open(filepath, mode='r') as f_in:
    str = f_in.read()
    with gzip.open(gzipfile, 'wb') as gzip_file:
      gzip_file.write(str.encode('utf-8'))

def decode_gzip_file_to_hex(gzip_file):
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
        
def decode_gzip_file_to_string(gzipfile, filepath):
  with gzip.open(gzipfile, mode='r') as infile:
    bytes_result = infile.read()
    text = bytes_result.decode('utf-8')
    print("Len: ", len(text))
    print("\nText:\n")
    print(text)
    with open(filepath, mode='w') as f_out:
      f_out.write(text)

def decode_text_gzip_file_to_string(gzipfile, filepath):
  with open(gzipfile, mode='r') as f_in:
    text = f_in.read().replace('0x', '').replace('\n ', '').replace(' ', '').replace(',', '')
    byte_string = bytes.fromhex(text) 
    text = bytes_to_string(byte_string)
    print(text)
    with open(filepath, mode='w') as f_out:
      f_out.write(text)
      
    
 
if __name__=='__main__':
  option = sys.argv[1]
  if option == 'e':
    text_file = sys.argv[2]
    gzip_file = sys.argv[3]
    create_gzip_file(text_file, gzip_file)
    decode_gzip_file_to_hex(gzip_file)
  elif option == 'd':
    gzip_file = sys.argv[2]
    text_file = sys.argv[3]
    decode_gzip_file_to_string(gzip_file, text_file)
  elif option == 'r':
    gzip_text_file = sys.argv[2]
    text_file = sys.argv[3]
    decode_text_gzip_file_to_string(gzip_text_file, text_file)