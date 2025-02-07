import os
from atemconnection import AtemConnection
from PIL import Image
from PATH import *

# Connect to the ATEM switcher
atem = AtemConnection(getIP())
atem.connect()

def atemExport1(path):
  # Ensure the image exists before uploading
  if os.path.exists(exported_image_path):
      # Open the PNG file
      with Image.open(exported_image_path) as img:
          width, height = img.size
          
          # Ensure image is in a compatible format and resolution
          if (width, height) != (1920, 1080):
              img = img.resize((1920, 1080))  # Resize to ATEM’s standard resolution
              
          # Convert image to bytes and upload to the ATEM media pool (slot 1)
          atem.upload_to_media_pool(img.tobytes(), slot=1, filename="SCOREBOX")

      print(f"Uploaded {exported_image_path} to ATEM media pool slot 1")

  else:
      print("Error: File not found!")

  def atemExport2(path):
  # Ensure the image exists before uploading
  if os.path.exists(exported_image_path):
      # Open the PNG file
      with Image.open(exported_image_path) as img:
          width, height = img.size
          
          # Ensure image is in a compatible format and resolution
          if (width, height) != (1920, 1080):
              img = img.resize((1920, 1080))  # Resize to ATEM’s standard resolution
              
          # Convert image to bytes and upload to the ATEM media pool (slot 1)
          atem.upload_to_media_pool(img.tobytes(), slot=2, filename="STATPOPUP")

      print(f"Uploaded {exported_image_path} to ATEM media pool slot 1")

  else:
      print("Error: File not found!")

# Disconnect from ATEM
atem.disconnect()