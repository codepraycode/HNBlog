from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST Framework's default exception handler first,
    # to get the standard error response
    
    response = exception_handler(exc, context)
    
    if response is not None:
        
        # check exception has a dict item
        if hasattr(exc.detail, 'items'):
            # remove the initial value
            response.data = {}
            errors = {}
            for key, value in exc.detail.items():
                # append errors into list
                errors[key] = " ".join(value)
            
            # Add property errors to the response
            response.data['errors'] = errors
        
        # Server status code in the response
        response.data['status_code'] = response.status_code
    
    return response