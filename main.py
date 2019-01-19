# import the necessary packages
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--delay", type=float, 
        help="Amount of time in seconds to delay the program before starting.")
ap.add_argument("-m", "--min-area", type=int, default=500, 
        help="Minimum area in pixels difference to be considered actual motion.")
ap.add_argument("-t", "--thresh", default=25, type=int,
        help="Level of threshold intensity.")
ap.add_argument("-v", "--video-path", 
        help="Path to video file. If not provided the default video recording device on your system will be used.")
args = vars(ap.parse_args())

print("Program starting.\n")

if args.get("video_path", None) is not None:
    try:
        print("Attempting to access the video at path: {}".format(args["video_path"]))
        video_stream = cv2.VideoCapture(args["video_path"])
        print("Successfully accessed video.")
    except:
        print("Could not access the specified video. Please make sure you are "
        + "providing an absolute path to file.")
else:
    try:
        print("Attempting to access the default video recording device.")
        video_stream = VideoStream(src=0).start()
        time.sleep(2.0)
        print("Successfully connected to the default recording device.")
    except:
        print("Could not access the default recording device. Please make sure "
        + "you have a device capable of recording video configured on your system.")
print()

if args.get("delay", None) is not None:
    print("Starting delay of: {} seconds".format(args["delay"]))
    time.sleep(args["delay"])
    print("Delay complete.")

# Init variable to hold first frame of video. This will be used as a reference.
# The motion detection algorithm utilizes the background of the initial frame
# to compare all consecutive frames to in order to detect motion
initial_frame = None

print("Starting motion detection")
print("Enter 'q' at any time to terminate")

# Main loop.
while True:
    # Set initial status to vacant.
    status = 'Area vacant.'

    # Grab current frame
    frame = video_stream.read()
    frame = frame if args.get("video_path", None) is None else frame[1]

    # If frame is none we have reached the end of the video
    if frame is None:
        break 
    
    # Preprocess frame:
    # Resize to have a width of 500px. Improves speed without sacrificing accuracy
    frame = imutils.resize(frame, width=600)
    # Convert to grayscale as the background subtraction algorithm utilizes 
    # black & white pixel data
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply guassian blur to smooth out image data and reduce irrelevant misleading 
    # data from noise, scratches, etc.
    blurred_frame = cv2.GaussianBlur(grayscale_frame, (21, 21), 0)

    if initial_frame is None:
        initial_frame = grayscale_frame
        continue
    
    # Calculate the absolute difference between the current frame and the comparison
    # frame (aka the initial frame)
    frame_delta = cv2.absdiff(initial_frame, grayscale_frame)
    # Compute the threshold of the frame delta
    thresholded_frame = cv2.threshold(frame_delta, args["thresh"], 255, cv2.THRESH_BINARY)[1]
    # Dialiate the threshold to fill in any gaps/holes that were created.
    dilated_frame = cv2.dilate(thresholded_frame, None, iterations=2)

    # Find the contours of the dilated version of the thresholded image
    contours = cv2.findContours(dilated_frame.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    # Loop over contours to search for changes
    for contour in contours:
        # If contour is smaller than the minimum specified area it does not represent
        #  significant motion and should thus be ignored
        if cv2.contourArea(contour) < args["min_area"]:
            continue
        
        # Draw a rectangle around any significant motion
        (x_pos, y_pos, width, height) = cv2.boundingRect(contour)

        cv2.rectangle(
            frame, 
            (x_pos, y_pos),
            (x_pos + width, y_pos + height),
            (0, 255, 0),
            2
        )

        status = 'Motion Detected!'
    
    # If area is vacant set font color to green, else set font color to red
    # Uses BGR color mapping
    font_color = (0, 255, 0) if status == 'Area vacant.' else (0, 0, 255)

    # Overlay room status onto image
    cv2.putText(
        frame, # Image to overlay text on
        f'Status: {status}', # Text to overlay
        (10, 20), # origin of text
        cv2.FONT_HERSHEY_SIMPLEX, # font face
        0.5, # font scale
        font_color,
        2 # thickness
    )

    cv2.imshow("Threshold", dilated_frame)
    cv2.imshow("Frame Delta", frame_delta)
    cv2.imshow("Main Feed", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break 
    
if args.get("video_path", None) is not None:
    video_stream.release()
else:
    video_stream.stop()

cv2.destroyAllWindows()
print("Program terminating")