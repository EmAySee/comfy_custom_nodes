# comfy_custom_nodes
Just a place to keep my code for nodes

koboldAPIaccess.py : This code defines a custom ComfyUI node to interact with the KoboldAI API. 

KoboldCPP ComfyUI Custom Node
Overview

This custom ComfyUI node, Kobold Custom_Node, allows you to seamlessly integrate with KoboldCPP directly within your ComfyUI workflows. It provides a user-friendly interface to send text prompts to your KoboldCPP instance and receive generated text outputs.

This node is particularly useful for:

    Text Generation in ComfyUI: Incorporate language models powered by KoboldCPP into your image generation or other ComfyUI workflows.
    Prompt Analysis and Refinement: Use KoboldCPP to analyze or refine prompts before passing them to other ComfyUI nodes.
    Creative Textual Tasks: Leverage KoboldCPP's capabilities for creative writing, story generation, and more, directly within ComfyUI.

Features

    Direct KoboldCPP Integration: Sends API requests to your running KoboldCPP instance.
    Configurable API Endpoint: Easily specify the IP address and port of your KoboldCPP API.
    Comprehensive Parameter Control: Exposes key KoboldCPP generation parameters directly in the ComfyUI node interface, including:
        Text Input (Prompt): Input your text prompt directly or connect it from other ComfyUI text nodes.
        Sampling Parameters: Control generation behavior with parameters like rep_pen, rep_pen_range, rep_pen_slope, temperature, tfs, top_a, top_k, top_p, and typical.
    String Output: Returns the generated text from KoboldCPP as a string, ready to be used by other ComfyUI nodes.
    Error Handling: Includes basic error handling for API request failures, providing informative error messages.

I actually just have this file in the root of my comfy nodes for now until i create more.

Installation

    Navigate to your ComfyUI custom nodes directory:
    Bash

ComfyUI/custom_nodes

Create a new directory (optional but recommended for organization):
Bash

    mkdir comfyui_koboldcpp_nodes
    cd comfyui_koboldcpp_nodes

    Save the Python code:
        Create a new file named __init__.py (or any .py file name you prefer, e.g., kobold_node.py) inside the comfyui_koboldcpp_nodes directory.
        Copy and paste the provided Python code into this file.

    Restart ComfyUI: Ensure ComfyUI is restarted to recognize the new custom node.

Usage

    Start KoboldCPP: Make sure you have KoboldCPP running and accessible at the specified API endpoint.
    Launch ComfyUI: Open your ComfyUI interface.
    Add the "Submit to Kobold API Node": In your ComfyUI workflow, right-click and select "Add Node" -> "Custom Nodes" -> "Submit to Kobold API Node".
    Configure the Node:
        text_input: Enter your prompt directly into the "text_input" field, or connect a "Text" node (or any node outputting a string) to this input.
        api_endpoint: Verify or update the API endpoint to match your KoboldCPP instance. The default is http://<kobold_IP_or_HOSTNAME>:5001/api/v1/generate. Replace <kobold_IP_or_HOSTNAME> with the actual IP address or hostname of your KoboldCPP server. If KoboldCPP is running locally, it's likely http://127.0.0.1:5001/api/v1/generate or http://localhost:5001/api/v1/generate.
        Sampling Parameters: Adjust the sampling parameters (rep_pen, rep_pen_range, rep_pen_slope, temperature, tfs, top_a, top_k, top_p, typical) as desired to control the text generation behavior. Refer to the KoboldCPP documentation for details on these parameters.
    Connect to other Nodes: Connect the api_response output of the "Submit to Kobold API Node" to other ComfyUI nodes that accept string inputs, such as:
        Text Nodes: To display or further process the generated text.
        Other Custom Nodes: To use the generated text as input for other tasks in your workflow.
    Execute your Workflow: Run your ComfyUI workflow. The "Submit to Kobold API Node" will send your prompt to KoboldCPP, and the generated text will be passed to the connected nodes.

Parameters Details
Parameter	Type	Default Value	Description
text_input	STRING	"Enter your promt to anaylze here, or change this to an input and add text node(s)"	The text prompt that will be sent to KoboldCPP for text generation.
api_endpoint	STRING	http://<kobold_IP_or_HOSTNAME>:5001/api/v1/generate	The URL of your KoboldCPP API endpoint. Important: Replace <kobold_IP_or_HOSTNAME> with your KoboldCPP server address.
rep_pen	FLOAT	1.08	Repetition penalty, controls how much the model should avoid repeating tokens.
rep_pen_range	FLOAT	360	Range for repetition penalty.
rep_pen_slope	FLOAT	0.7	Slope for repetition penalty.
temperature	FLOAT	0.87	Sampling temperature, controls the randomness of the output. Lower values are more deterministic, higher values are more random.
tfs	FLOAT	1	Tail Free Sampling, another sampling method.
top_a	FLOAT	0	Top-A sampling.
top_k	FLOAT	90	Top-K sampling, keeps only the top K most likely tokens.
top_p	FLOAT	0.94	Top-P (nucleus) sampling, keeps tokens with cumulative probability mass of P.
typical	FLOAT	1	Typical sampling.

Output:

    api_response (STRING): The text generated by KoboldCPP in response to your prompt. In case of an API error, this output will contain an error message.

Requirements

    ComfyUI: You need to have ComfyUI installed and working.
    KoboldCPP: You must have KoboldCPP running and accessible via HTTP API.
    requests Python Library: The requests library is required. ComfyUI environments usually come with requests pre-installed. If not, you can install it using pip:
    Bash

    pip install requests

Example Workflow

(Optional: You can add a simple example workflow description or even a screenshot of a basic ComfyUI workflow using this node here.)

For example, a simple workflow could consist of:

    Text Node: Containing your prompt.
    Submit to Kobold API Node: Connected to the Text Node for input, configured with your KoboldCPP endpoint.
    Preview Text Node: Connected to the api_response output of the Kobold API Node to display the generated text.

This setup will send your prompt to KoboldCPP and display the generated output in the Preview Text Node.

Author

(Optional: Me and Gemini worked to write this (gemini.google.com) .)
