#!/usr/bin/env python3
import os
#import glob
#from typing import List
#from dotenv import load_dotenv
#from multiprocessing import Pool
#from tqdm import tqdm


persist_directory = os.environ.get('PERSIST_DIRECTORY')
source_directory = os.environ.get('SOURCE_DIRECTORY', 'source_documents')
embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME')

#print above variables
print(persist_directory)
print(source_directory)
print(embeddings_model_name)