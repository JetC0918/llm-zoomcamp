# Module 1: Introduction
## 1.1 Introduction to LLM and RAG

* LLM - Large Language Model
A language model that able to provide answer based on user's prompt 

* RAG - Retrieval Augmented Generation 
Retrieval = Search
Generation = LLLM
User's prompt will be directed to a knowledge base/database first to retrieve context, then will be feed to LLM to generate answer.

## 1.2 Preparing the Environment 

```bash
pip install tqdm notebook==7.1.2 openai elasticsearch pandas scikit-learn ipywidgets
```

## 1.3 - Retrieval and Search
<a href="./rag-intro.ipynb"> 
</a>

## 1.4 Generation with OpenAI
<a href="./rag-intro.ipynb"> 
</a>

* Invoking OpenAI API

```python
from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(
    model = 'gpt-4o',
    messages = [{"role":"user", "content":q}]
)
```

* Building the prompt

```python
prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database. 
Use only the facts from the CONTEXT when answering the QUESTION.
If the CONTEXT doesn't' contain the answer, output NONE


QUESTION:{question}
CONTEXT: {context}
""".strip()

prompt = prompt_template.format(question=q, context=context).strip()
```

* Getting the answer
```python
response = client.chat.completions.create(
    model = 'gpt-4o',
    messages = [{"role":"user", "content":prompt}]
)

response.choices[0].message.content
```

## 1.6 Searching with ElasticSearch
ElasticSearch - Data saved on disk, when start next time it will have all the data we needed

Running Elasticsearch with Docker on PowerShell:
```wsl
docker run -it `
    --rm `
    --name elasticsearch `
    -m 4GB `
    -p 9200:9200 `
    -p 9300:9300 `
    -e "discovery.type=single-node" `
    -e "xpack.security.enabled=false" `
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3

```

Index settings:

```python
{
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "text": {"type": "text"},
            "section": {"type": "text"},
            "question": {"type": "text"},
            "course": {"type": "keyword"} 
        }
    }
}
```

Query:

```python
{
    "size": 5,
    "query": {
        "bool": {
            "must": {
                "multi_match": {
                    "query": query,
                    "fields": ["question^3", "text", "section"],
                    # ^3 means 3 times more important
                    "type": "best_fields"
                }
            },
            "filter": {
                "term": {
                    "course": "data-engineering-zoomcamp"
                }
            }
        }
    }
}
```