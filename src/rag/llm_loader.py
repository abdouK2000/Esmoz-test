"""
Loads the LLM to be used for the processing. 
"""
from conf.config_file import MODEL_PATH
from llama_cpp import Llama

class LLMHelper:
    """
    Helper class to define an interface for local LLM usage
    """

    def __init__(self):
        pass

    def load_model(self, model_path: str = MODEL_PATH):
        """
        Load the model specified in the environment variables.

        Args:
            model_path: The absolute path of the model
        """
        self.model = Llama(
            model_path=str(model_path),
            verbose=False,
            n_ctx=1024    # subject to change
        )

    def get_reponse(self, prompt) -> str:
        """
        Get chat completion response from the LLM
        
        Args: 
            prompt: Text used as a prompt for the LLM
        
        Returns:
            A string response answering the prompt.
        """

        response = self.model.create_chat_completion(
            messages=[
                {'role': 'system',
                 'content': 'Tu es un assistant qui répond logiquement et aux demandes des utilisateurs'
                },
                {"role": "user",
                "content": f"{prompt}"
                }
            ]
        )

        return response['choices'][0]['message']['content']
