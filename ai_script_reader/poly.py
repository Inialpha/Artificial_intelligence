import cv2
import numpy as np

width = 200
height = 200
color = (0, 0, 0)
thickness = 2

def create_canvas():
    # Create a blank white image
    canvas = np.full((width, height, 3), 255, dtype=np.uint8)
    return canvas

def draw_note(canvas):
    # Define points for the triangle
    triangle_points = np.array([[100, 140], [120, 170], [80, 170]], np.int32)
    triangle_points = triangle_points.reshape((-1, 1, 2))
    cv2.fillPoly(canvas, [triangle_points], color=(0, 0, 0))

    # Drew vertical line
    line_start = (120, 170)
    line_stop = (120, 10)
    cv2.line(canvas, line_start, line_stop, color, thickness)

    return canvas

def draw_lines(canvas):
    start, stop = 0, 200
    line_pos = [170, 140, 110, 80, 50]
    
    for pos in line_pos:
        cv2.line(canvas, (start, pos), (stop, pos), color, thickness)

    return canvas


def display(canvas):
    # Save and display the image
    cv2.imwrite("do.png", canvas)
    cv2.imshow("Triangle", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    canvas = create_canvas()
    canvas = draw_lines(canvas)
    canvas = draw_note(canvas)

    display(canvas)
