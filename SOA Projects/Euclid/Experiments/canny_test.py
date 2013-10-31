from skimage import io, filter
import matplotlib.pyplot as plt

card=io.imread("../Resources/perspective-quadrilateral-src-img.jpg", as_grey=True)
edge = filter.canny(card, sigma=3)
plt.imshow(edge, cmap=plt.cm.gray)
plt.axis("off")
plt.show()

