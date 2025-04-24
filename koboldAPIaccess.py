# outdated # Switched to OOBA##
import requests
import json

class SubmitToKoboldAPI:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_input": ("STRING", {"default": "Enter your prompt to analyze here, or change this to an input and add text node(s)"}),
                "api_endpoint": ("STRING", {"default": "http://<kobold_IP_or_HOSTNAME>:5001/api/v1/generate"}),  # Default API endpoint - change this!
                "rep_pen": ("FLOAT", {"default": 1.08, "min": 0.0, "max": 2.0, "step": 0.01}), # Added min/max/step for better control
                "rep_pen_range": ("FLOAT", {"default": 360, "min": 0, "max": 1000, "step": 1}), # Added min/max/step
                "rep_pen_slope": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 1.0, "step": 0.01}), # Added min/max/step
                "temperature": ("FLOAT", {"default": 0.87, "min": 0.0, "max": 1.0, "step": 0.01}), # Added min/max/step
                "tfs": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}), # Added min/max/step
                "top_a": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01}), # Added min/max/step
                "top_k": ("INT", {"default": 90, "min": 0, "max": 2048, "step": 1}), # Changed to INT, added min/max/step
                "top_p": ("FLOAT", {"default": 0.94, "min": 0.0, "max": 1.0, "step": 0.01}), # Added min/max/step
                "typical": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}), # Added min/max/step
            },
        }

    RETURN_TYPES = ("STRING",)  # Output is text
    RETURN_NAMES = ("api_response",)
    OUTPUT_NODE = True
    FUNCTION = "submitToLLMAPI"

    def submitToLLMAPI(self, api_endpoint, text_input, rep_pen, rep_pen_range, rep_pen_slope, temperature, tfs, top_a, top_k, top_p, typical):
        payload = {
            "prompt": text_input,
            "quiet": False,  # Consider making this an input parameter
            "rep_pen": rep_pen,
            "rep_pen_range": rep_pen_range,
            "rep_pen_slope": rep_pen_slope,
            "temperature": temperature,
            "tfs": tfs,
            "top_a": top_a,
            "top_k": top_k,
            "top_p": top_p,
            "typical": typical
        }

        headers = {'Content-type': 'application/json'}

        try:
            response = requests.post(api_endpoint, json=payload, headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes

            try: # Nested try-except for JSON decoding errors
                api_response = response.json()
                print("API Response Content:", api_response)  # Debugging: Print the full JSON

                if "results" in api_response and len(api_response["results"]) > 0 and "text" in api_response["results"][0]:
                    api_response_text = api_response["results"][0]["text"]
                    trimmed_text = api_response_text.strip()
                    return (trimmed_text,)
                else:
                    error_message = f"Unexpected JSON response format: {api_response}"
                    print(error_message)
                    return (error_message,)

            except json.JSONDecodeError as e:
                error_message = f"Error decoding JSON response: {e}. Response text: {response.text}"
                print(error_message)
                return (error_message,)


        except requests.exceptions.RequestException as e:
            error_message = f"Error during API request: {e}. Response text: {getattr(response, 'text', 'N/A')}" # Include response text if available
            print(error_message)
            return (error_message,)


NODE_CLASS_MAPPINGS = {
    "Submit to Kobold API": SubmitToKoboldAPI
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Submit to Kobold API": "Submit to Kobold API Node"
}
