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