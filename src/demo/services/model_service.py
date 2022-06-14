from io import BytesIO

from PIL import Image, ImageOps
import numpy as np
import torch
from torchvision.transforms import ToTensor

from .model import CNN


class ModelService:
    def __init__(self):
        self._model = self._load_model()

    @staticmethod
    def _load_model() -> torch.nn.Module:
        model = CNN()
        model.load_state_dict(torch.load('demo/services/model.tch'))
        return model

    def predict(self, image: BytesIO) -> dict[int, float]:
        image = self._preprocess_image(image)
        self._model.eval()
        with torch.no_grad():
            prediction, _ = self._model(image)
        return self._process_result(prediction)

    @staticmethod
    def _preprocess_image(image: BytesIO) -> torch.tensor:
        image = Image.open(image)
        image = ImageOps.grayscale(image)  # grayscale

        if image.size != (28, 28):  # resizing
            image = image.resize((28, 28))

        transform = ToTensor()
        image = transform(image)  # tensor transform
        return image.unsqueeze(1)  # Add additional dim: [1, 28, 28] -> [1, 1, 28, 28]

    def _process_result(self, result: torch.tensor) -> dict[int, float]:
        result = self._relu(result).squeeze().numpy()
        result = self._softmax(result)
        return {key: value for key, value in enumerate(result.tolist())}

    @staticmethod
    def _sigmoid(z: np.array) -> np.array:
        return 1 / (1 + np.exp(-z))

    @staticmethod
    def _relu(z: np.array) -> np.array:
        return np.maximum(0, z)

    @staticmethod
    def _softmax(z: torch.tensor) -> np.array:
        return np.exp(z) / sum(np.exp(z))
