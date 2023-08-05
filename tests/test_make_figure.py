import sys
sys.path += ['.']

from latexutils.make_figure import make_image, make_tabular_image
import numpy as np

if __name__ == '__main__':


    latex_image = make_image('image.png', caption='My image', label='img1', preable=False)
    print(latex_image)


    images = np.array(
            [["fig1.png"],["fig2.png"]]
        )

    latex_images = make_tabular_image(images, caption='My image', label='img1', preable=False)
    print(latex_images)
