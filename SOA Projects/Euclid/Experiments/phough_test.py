from skimage.transform import probabilistic_hough
from skimage.filter import canny
from skimage import io
import matplotlib.pyplot as plt


def derive_sie(p1, p2):
    # Derives the slope-intercept form equation given two points on a line
    # The points should be a tuple in the form (x, y) where x and y are floats
    # Returns (gradient, y-intercept) to form the y = mx + c equation.
    try:
        gradient = (float(p2[1])-p1[1])/(p2[0]-p1[0])
    except:
        gradient = 0
    y_intercept = p1[1]-(gradient*p1[0])
    return (gradient, y_intercept)

def find_y(x, si):
    # Finds the y value of a slope-intercept equation given the value of x
    # and the slope-intercept (si) in the form (gradient, y_intercept).
    # Returns a float value.
    y = si[0]*x+si[1]
    return y

def find_x(y, si):
    # Finds the x value of a slope-intercept equation given the value of y
    # and the slope-intercept (si) in the form (gradient, y_intercept).
    # Returns a float value.
    x = (y-si[1])/si[0]
    return x

def expand_line(sie, max_x, max_y):
    if sie[0] != 0:
        # Point 1
        p1_y = find_y(0, sie)
        if p1_y < 0:
            p1_x = find_x(0, sie)
            p1 = (p1_x, 0)
        elif p1_y > max_y:
            p1 = (find_x(max_y, sie), max_y)
        else:
            p1 = (0, p1_y)
        # Point 2
        p2_y = find_y(max_x, sie)
        if p2_y > max_y:
            p2_x = find_x(max_y, sie)
            p2 = (p2_x, max_y)
        elif p2_y < 0:
            p2 = (find_x(0, sie), 0)
        else:
            p2 = (max_x, p2_y)
        line = (p1, p2)
    else:
        # Gradient = 0 implies a horizontal line
        line = ((0, sie[0]), (max_x, sie[0]))
    return line


def main():
    image = io.imread("../Resources/perspective-quadrilateral-src-img.jpg", as_grey=True)
    edges = canny(image, sigma=3)
    lines = probabilistic_hough(edges, line_length=75, threshold=50)

    plt.imshow(edges)

    cols = len(image[0])
    for line in lines:
        eq = derive_sie(line[0], line[1])
        p1, p2 = expand_line(eq, len(image[0]), len(image))
        print line
        print p1, p2
        print ""
        plt.plot((p1[0], p2[0]), (p1[1], p2[1]), color='green')

    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
