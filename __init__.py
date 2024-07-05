from .civitai_lora_loader import CivitAI_LORA_Loader
from .civitai_checkpoint_loader import CivitAI_Checkpoint_Loader
from .civitai_api_key import CivitAI_API_Key_From_Env

NODE_CLASS_MAPPINGS = {
    "CivitAI_Lora_Loader": CivitAI_LORA_Loader,
    "CivitAI_Checkpoint_Loader": CivitAI_Checkpoint_Loader,
    "CivitAI_API_Key_From_Env": CivitAI_API_Key_From_Env
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CivitAI_Lora_Loader": "CivitAI Lora Loader",
    "CivitAI_Checkpoint_Loader": "CivitAI Checkpoint Loader",
    "CivitAI_API_Key_From_Env": "CivitAI API Key From Env"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']