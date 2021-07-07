from tensorflow.keras.models import load_model
import cv2
import numpy as np


class FilterClassifier:

    def get_result(self, source = []):
        """
        This method used for predict image
        that image contains adult content or not
        this method takes 1 argument :
        
        1. source | List of Image path | String
        """

        images = []

        # read image
        for path in source:

            read_img = cv2.imread(path)

            # resize image to 128 * 128 pixel
            dim = (128, 128)
            resize_image = cv2.resize(read_img, dim)

            # convert image to gray
            gray_img = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY) / 255.

            images.append(gray_img)
        
        # load neural network model
        model = load_model("safe_content/adult_filter")

        # predict the image
        # if result is 1 that means the image contains adult content
        # if result is 0 that means the image not containts adult contetn

        pred = model.predict(np.array(images))

        return np.argmax(pred, axis=1)