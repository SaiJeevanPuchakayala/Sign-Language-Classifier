# Sign-Language-Classifier

![ASL](/Images/asl.png)

Some of the major problems faced by a person who are unable to speak is they cannot express their emotion as freely in this world. Utilize that voice recognition and voice search systems in smartphone(s).Audio results cannot be retrieved. They are not able to utilize (Artificial Intelligence/personal Butler) like google assistance, or Apple's SIRI etc because all those apps are based on voice controlling. There is a need for such platforms for such kind of people. American Sign Language (ASL) is a complete, complex language that employs signs made by moving the hands combined with facial expressions and postures of the body. It is the go-to language of many North Americans who are not able to talk and is one of various communication alternatives used by people who are deaf or hard-of-hearing. While sign language is very essential for deaf-mute people, to communicate both with normal people and with themselves, is still getting less attention from the normal people. The importance of sign language has been tending to ignored, unless there are areas of concern with individuals who are deaf-mute. One of the solutions to talk with the deaf-mute people is by using the mechanisms of sign language. 

#### Hand gesture is one of the methods used in sign language for non-verbal communication. It is most commonly used by deaf & dumb people who have hearing or talking disorders to communicate among themselves or with normal people. 

Various sign language systems have been developed by many manufacturers around the world but they are neither flexible nor cost-effective for the end users.

#### Our project aims to create a web application, a OpenCV model to recognize signs realtime camera feed and train a model which when given a image of hand gestures of American Sign Language shows the output for that particular sign in the text format on the screen.

We implemented 27 alphabet symbols, 1-9 numerical digits as shown below 

![ASL signs](/Images/signs.png)


### Web Application Recognition

![ASL Web App](/Images/webApp.png)


### Live Camera Feed Recognition

![Sign Y recognition](/Images/cameraFeed1.png)

![Sign B recognition](/Images/cameraFeed2.png)


### TechStack:

- Python 3.9.1
- IDE (Jupyter) 6.1.4
- Keras 2.7.0
- Tensorflow 2.7.0
- NumPy 1.19.2
- Matplotlib 3.3.2
- Gradio Framework (For Web Application)
- OpenCV (For recognizing signs in realtime camera feed)

### Requirements

 - Camera (not less than 3 mega pixels)
 - CPU    (2.7 Ghz Multi-core Processor)
 - Python version >= 3.8 

### Datasets Used

1. https://www.kaggle.com/ayuraj/asl-dataset
2. https://www.kaggle.com/datamunge/sign-language-mnist

## Important Notes

- Model Trainning Process is Done seperately using Google Colab.
- To get the best efficiency from this application please make sure to run it in a bright place with plain background.
