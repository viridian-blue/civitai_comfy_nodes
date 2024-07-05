import os

class CivitAI_API_Key_From_Env:
    """
    Load the CivitAI API key from an environment variable
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "env_var": ("STRING", {"default": "CIVITAI_API_KEY", "placeholder": "ENV variable name or literal value"}),
            }
        }
    
    RETURN_TYPES = ("CIVITAI_API_KEY",)
    FUNCTION = "get_api_key"

    CATEGORY = "CivitAI"

    def get_api_key(self, env_var):
        try:
            api_key = os.environ[env_var]
        except KeyError:
            raise ValueError(f"Environment variable {env_var} not found")
        return (api_key,)

