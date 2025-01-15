import random
from io import BytesIO

from PIL import Image, ImageOps

from .border_request_message import BorderParameters  # Correct import
from .core.tool import Tool


class BorderTool(Tool):

    def __init__(self) -> None:
        pass
  

    def apply(self, parameters: BorderParameters):  # Correct type hint
        """
        Apply a border to the input image and save the result.

        Args:
            parameters (BorderParameters): Border parameters including input/output URIs, border size, and border color.
        """
    
        # Open the input image
        input_image = Image.open(parameters.inputImageURI).convert("RGBA")

        border_width = random.randint(10, 100)

            # Randomize the border color (each of R, G, B between 0 and 255)
        border_color = (
            random.randint(0, 255),  # Red
            random.randint(0, 255),  # Green
            random.randint(0, 255)   # Blue
        )

        bordered_image = ImageOps.expand(
            input_image,
            border=border_width,
            fill=border_color
        )
        
   
        final_image = bordered_image.convert("RGB")
        final_image.save(parameters.outputImageURI)