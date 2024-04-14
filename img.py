import cv2
import numpy as np

# Create a blank white canvas
width, height = 800, 600
canvas = np.ones((height, width, 3), dtype=np.uint8) * 255

# Draw a person sitting at the computer desk
cv2.rectangle(canvas, (200, 200), (600, 500), (0, 0, 0), -1)  # Desk
cv2.rectangle(canvas, (250, 300), (550, 500), (200, 200, 200), -1)  # Monitor
cv2.circle(canvas, (400, 250), 30, (0, 0, 255), -1)  # Head
cv2.line(canvas, (400, 250), (400, 350), (0, 0, 0), 2)  # Body
cv2.line(canvas, (400, 350), (350, 450), (0, 0, 0), 2)  # Left leg
cv2.line(canvas, (400, 350), (450, 450), (0, 0, 0), 2)  # Right leg
cv2.line(canvas, (400, 300), (350, 300), (0, 0, 0), 2)  # Left arm
cv2.line(canvas, (400, 300), (450, 300), (0, 0, 0), 2)  # Right arm

# Add Python logo to the monitor
python_logo = cv2.imread("python_logo.png")  # Replace with an actual Python logo image
python_logo = cv2.resize(python_logo, (300, 200))
canvas[220:420, 260:560] = python_logo

# Display the image
cv2.imshow("Person Coding in Python", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
