import json
import random
from io import BytesIO
import string

from PIL import Image, ImageOps

from .border_request_message import BorderParameters  # Correct import
from .core.tool import Tool
from .image_uri_utils import data_uri_to_image_file, image_to_data_uri

class BorderTool(Tool):

    def __init__(self) -> None:
        pass
  

    def apply(self, parameters: BorderParameters):  # Correct type hint
        """
        Apply a border to the input image and save the result.

        Args:
            parameters (BorderParameters): Border parameters including input/output URIs, border size, and border color.
        """
                
        # Extract input parameters
        message_id = parameters["messageId"]
        user_id = parameters["user_id"]
        project_id = parameters["project_id"]
        input_image_uri = parameters["inputImageURI"]
        border_width = int(parameters["configValue"])
        border_color = parameters["configColor"]
        try:
            fake_image_file = data_uri_to_image_file(input_image_uri)
            
            # Open the input image
            input_image = Image.open(fake_image_file).convert("RGBA")
            
            # string #hex to tuple RGB
            border_color = tuple(int(border_color[i:i+2], 16) for i in (0, 2, 4))
            
            bordered_image = ImageOps.expand(
                input_image,
                border=border_width,
                fill=border_color
            )
            
    
            final_image = bordered_image.convert("RGB")
            
            #get the output image URI
            output_image = BytesIO()
            final_image.save(output_image, format="PNG")
            output_image.seek(0)
            output_image_uri = image_to_data_uri(output_image)
            
            # Build success response
            response = {
                "messageId": ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32)),
                "user_id": user_id,
                "project_id": project_id,
                "status": "success",
                "error": {},
                "output": {
                    "type": "image",
                    "imageURI": output_image_uri,
                },
                "metadata": {
                    "microservice": "ColoredBorderTool"
                }
            }
            
        except Exception as e:
            # Build error response
            response = {
                "messageId": ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(32)),
                "user_id": user_id,
                "project_id": project_id,
                "status": "error",
                "output": {},
                "error": {
                    "message": str(e)
                },
                "metadata": {
                    "microservice": "ColoredBorderTool"
                }
            }
            
        return json.dumps(response)