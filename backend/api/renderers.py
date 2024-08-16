from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnList, ReturnDict

class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Access the response object from the renderer context
        response = renderer_context.get('response', None)
        
        # Determine if the response is an error based on the status code
        if response is not None and 400 <= response.status_code < 600:
            response_data = {
                'status': 'error',
                'errors': data  # In error case, the data is the errors
            }
        else:
            response_data = {
                'status': 'success',
                'data': data  # In success case, the data is the actual data
            }
        
        # Render the final response using the parent class's render method
        return super(CustomJSONRenderer, self).render(response_data, accepted_media_type, renderer_context)
