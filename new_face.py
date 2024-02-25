import cv2
import os

folder='images'

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize video capture from default camera
cap = cv2.VideoCapture(0)

registered_faces=[]
for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder,filename), cv2.IMREAD_GRAYSCALE)
    registered_faces.append(img)
print(len(registered_faces))
i=0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Loop through detected faces
    for (x, y, w, h) in faces:
        # Crop the face region from the frame
        face = gray[y:y+h, x:x+w]

        # Compare the detected face to registered faces
        match = False
        for reg_face in registered_faces:
            # Use template matching to compare faces
            result = cv2.matchTemplate(face, reg_face, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(result)
            if max_val > 0.8:
                match = True
                break

        # If no match is found, add the face to the dataset
        
        if not match:
            # Display the detected face in a window
            cv2.imshow('Detected Face', face)
            
            # Wait for key press to add the face to the dataset
            key = cv2.waitKey(0)
            if key == ord('s'):
                # Save the face to the dataset
                registered_faces.append(face)
                #img_name='register_new/registered_face_'+ str(i)+'.jpg'
                admin=input('enter the name ')
                img_name='register_new/'+admin+'.jpg'

                cv2.imwrite(img_name, face)
                i=i+1

    # Display the original frame in a window
    cv2.imshow('Video', frame)

    # Wait for key press to exit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()
