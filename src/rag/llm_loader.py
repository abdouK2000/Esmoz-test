"""
Loads the LLM to be used for the processing. 
"""

from pathlib import Path

from conf.config_file import MODEL_PATH
from llama_cpp import Llama


def load_model(model_path: str = MODEL_PATH):
    """
    Load the model specified in the environment variables.

    Args:
        model_path: The absolute path of the model

    Returns:

    """

    model = Llama(
        model_path=model_path,
        verbose=False,
        n_ctx=1024    # subject to change
    )

    return model


if __name__ == "__main__":
    print("import ok")
