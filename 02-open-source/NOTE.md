## 2. Open-Source LLMs

## 2.3 FLAN-T5
* Model: `google/flan-t5-xl` 
* About 10GB, took sometime to generate answer

Links:

* https://huggingface.co/google/flan-t5-xl
* https://huggingface.co/docs/transformers/en/model_doc/flan-t5

## 2.4 Phi 3 Mini
* Model: `microsoft/Phi-3-mini-128k-instruct` 
* Smaller in size, answer generated faster than FLAN-t5


Links:

* https://huggingface.co/microsoft/Phi-3-mini-128k-instruct


## 2.5 Mistral-7B and HuggingFace Hub Authentication

* Model: `mistralai/Mistral-7B-v0.1`
* Notebook: [huggingface-mistral-7b.ipynb](huggingface-mistral-7b.ipynb)
* Largest in size (~13GB), answer generated fast
 
## 2.7 Ollama - Running LLMs on a CPU

* The easiest way to run an LLM without a GPU is using [Ollama](https://github.com/ollama/ollama)
* Notebook [ollama.ipynb](ollama.ipynb)

For Linux:

```bash
curl -fsSL https://ollama.com/install.sh | sh

ollama start
ollama pull phi3
ollama run phi3
```

[Prompt example](prompt.md)

Connecting to it with OpenAI API:

```python
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)
```

Docker

```bash
docker run -it \
    -v ollama:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama
```

Pulling the model

```bash
docker exec -it ollama bash
ollama pull phi3
```

## 2.8 Ollama & Phi3 + Elastic in Docker-Compose

