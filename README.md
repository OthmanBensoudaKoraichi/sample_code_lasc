# Design

Each case includes **3 to 5 PDF documents**, typically containing up to 100 pages—some have only a few pages, while others have significantly more. These documents primarily contain text, but they may also include **tables**, **credit card statements**, and other structured data.

### Our goals are to:

- **Extract key information** (e.g., *Who is the plaintiff?*)
- **Verify specific conditions** (e.g., *Is the plaintiff a debt buyer?*)
- **Check for the absence of critical documents** (e.g., *Does the case include Declaration 1788?*)

Although the schema below displays only **three nodes**, the actual system will run **dozens of parallel processes**. Note that the code currently runs a serial process.

## Dev Setup (optional)
### Quickstart

1. Create and activate your virtual environment
```
conda create -n myapp python=3.10 -y
source activate myapp
```
2. Intall uv `pip install uv` (Read about the uv package manager [here](https://docs.astral.sh/uv/guides/projects/#managing-dependencies))

3. activate your virtual environment
```
uv sync
source .venv/bin/activate
```
### Additional Dev Notes
- to add a dependency, simply run 
```
uv add <package>
```
- Read about the uv package manager [here](https://docs.astral.sh/uv/guides/projects/#managing-dependencies)



## Pipeline Overview

1. **OCR** – Convert scanned PDFs into machine-readable text  
2. **Chunking & Vectorization** – Split the text and embed it into vector space  
3. **RAG (Retrieval-Augmented Generation)** – Query the vector database for insights

![Schema](https://github.com/user-attachments/assets/6b7b2381-2e7d-491f-b6a5-36f46df70ca4)

