####Similarity Finder Application#########
##### install  required libraries
####### pip install tf-keras
#####    pip install sentence-transformers

from sentence_transformers import SentenceTransformer, util

# Load the pre-trained BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')  # A lightweight model; for higher accuracy, use 'all-mpnet-base-v2'

# Input paragraphs
paragraph1 = """Artificial Intelligence is transforming the world. It is used in healthcare, finance, and many other industries."""
paragraph2 = """AI is revolutionizing industries like finance and healthcare, significantly impacting the global economy."""

# Step 1: Compute embeddings
embedding1 = model.encode(paragraph1, convert_to_tensor=True)
embedding2 = model.encode(paragraph2, convert_to_tensor=True)

# Step 2: Compute Cosine Similarity
similarity = util.cos_sim(embedding1, embedding2).item()

# Step 3: Convert to percentage
similarity_percentage = similarity * 100
print(f"Similarity: {similarity_percentage:.2f}%")
