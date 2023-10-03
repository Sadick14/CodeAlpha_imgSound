import os
import gtts
import pytesseract
import playsound

class FileNotFoundException(Exception):
      """Exception raised when the image file cannot be found."""
def __init__(self, image_path):
    super().__init__(f"Image file not found: {image_path}")

def text_to_speech(image_path):

  if not os.path.isfile(image_path):
    raise FileNotFoundException(image_path)

  # Extract text from the image.
  text = pytesseract.image_to_string(image_path)

  try:
      tts = gtts.gTTS(text, lang='en')
  except AssertionError as e:
    # Handle the error "No text to speak".
    print(e.args[0])
    return
  else:
    tts.save('speech.mp3')
    playsound.playsound('speech.mp3')

if __name__ == '__main__':
  image_path = input("Enter image file path: ")

  try:
    text_to_speech(image_path)
  except FileNotFoundException as e:
    print("Error: The image file '%s' could not be found." % image_path)
    exit()
