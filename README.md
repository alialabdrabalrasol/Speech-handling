# Speech-handling

## This project uses some of IBM cloud services which are speech to text and text to speech with the help of python.

# Speech to Text

## The service is firstly created on cloud.ibm.com/catalog that is Speech to text. Once created, both api key and region are captured then used inside a live speech detection program that is transcibe.py for a period of time which is used as -t to denote time and a number which denotes the period. Throughout running time , speech is captured through a microphone then speech is written as a text. Finally text gets saved in a .txt file.

# Text to Speech

## The service is firstly created on cloud.ibm.com/catalog that is Text to speech. Once created, both api key and url of the service is captured. a text is then typed inside a .txt file and saved. Then the service is started and the text is read through generating an mp3 file which reads words writted inside the .txt file. after Text2Speech.py is run.
