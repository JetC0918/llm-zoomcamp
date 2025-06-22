## [Qdrant](https://qdrant.tech/)
- Open source embedding vector database that support multimodal

### [Points](https://qdrant.tech/documentation/concepts/points/)
- A folder/ collection of all the details of a piece of information
- Can hold multiple vectors in a point (text vector, image vector, etc)
- The attached data is called Payload

### [Payload](https://qdrant.tech/documentation/concepts/payload/)
- An additional vector table build to fasten the search based on specific field
```python
client.create_payload_index(
    collection_name=collection_name,
    field_name="course",
    field_schema="keyword" # exact matching on string metadata fields
)
```
- A vector table will be created based on the ['course'] of the search, for fast lookup for the ['course'] key
- "keyword" schema = exact matching of the data (if the query is about data-enginnering-zoomcamp, it will only search inside data-enginnering-zoomcamp related db)

### Using Qdrant
- Setup Docker
```bash
docker pull qdrant/qdrant

docker run -p 6333:6333 -p 6334:6334 \
   -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
   qdrant/qdrant
```

- Import library
```python
from qdrant_client import QdrantClient, models
```

- Initialize client
```python
client = QdrantClient("http://localhost:6333") #connecting to local Qdrant instance
```

- Declaring Variables
```python
VECTOR_SIZE = 512 # Depends on model
COLLECTION_NAME = "my_documents" 
model_handle = "jinaai/jina-embeddings-v2-small-en"
```

- Create collection
```python
qd_client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=models.VectorParams(
        size=VECTOR_SIZE,                 
        distance=models.Distance.COSINE),
)
```

- Create points for each data in the documents
```python
points = [] 

for i, doc in enumerate(documents): 
    text =   doc['text']
    vector = models.Document(text=text, model=model_handle) #embed text locally with "jinaai/jina-embeddings-v2-small-en" from FastEmbed 
    point = models.PointStruct(
        id=i,
        vector= vector,
        payload= doc
    )
    points.append(point)
 
```

- Upsert the points into collection (database)
```python
qd_client.upsert(
    collection_name=COLLECTION_NAME,
    points=points
)
```

- Embed Text using fastemd
```python
from fastembed import TextEmbedding
```

- Search for neasert point using cosine similarity
```python
question = 'I just discovered the course. Can I join now?' 

responses = qd_client.query_points(
            collection_name=COLLECTION_NAME,
            query=models.Document( #embed the query text locally with "jinaai/jina-embeddings-v2-small-en"
                text=question,
                model=model_handle 
            ),
            limit=1, # top closest matches
            with_payload=True #to get metadata in the results
        )
```