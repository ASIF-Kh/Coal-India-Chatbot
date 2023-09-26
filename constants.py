
from chromadb.config import Settings
# Define the Chroma settings
CHROMA_SETTINGS = Settings(
        persist_directory="db",
        anonymized_telemetry=False
)

embeddings_model_name = "all-MiniLM-L6-v2" 
persist_directory = "db" 
model_type = "GPT4All" 
model_path = "models/ggml-model-gpt4all-falcon-q4_0.bin"
model_n_ctx = 1000
model_n_batch = 8
target_source_chunks = 4
source_directory = "source_documents"
chunk_size = 500
chunk_overlap = 50