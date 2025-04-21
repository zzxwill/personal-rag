# How to Create and Query a Personal Knowledge Base

This guide explains how to create your own searchable knowledge base from HTML files.

## Step 1: Collect HTML Files

- Download the HTML file [Prompt engineering: overview and guide](https://cloud.google.com/discover/what-is-prompt-engineering) and some htmls from [www.zhouzhengxi.com](https://www.zhouzhengxi.com)
- Place all HTML files in the `sources` folder

## Step 2: Create the Vector Database

Run the embedding script to convert your HTML files into a searchable database:

```bash
```bash
➜  personal-rag git:(master) ✗ python embedding.py
✅ Loaded Stand on Tiptoes.html: 16 characters
✅ Loaded Prompt Engineering for AI Guide _ Google Cloud.html: 57895 characters
✅ Loaded Spend $0.05 to Change the Voice of a Song.html: 16 characters
✅ Loaded Try Stable Diffusion.html: 16 characters
✅ Loaded 4 documents.
✅ After splitting, got 132 chunks.

First chunk content sample (first 100 chars): 
Stand on Tiptoes...

✅ Embedding model loaded successfully.
✅ Created vector database with 132 documents.
🎉 Vector database saved successfully to folder html_faiss_index!
```

What this does:
- Loads all HTML files from the `sources` folder
- Extracts the text content from each file
- Splits text into smaller chunks
- Creates vector embeddings for each chunk
- Saves everything in the `html_faiss_index` folder

## Step 3: Search Your Knowledge Base

Run the query script to search your knowledge base:

```bash
```bash
➜  personal-rag git:(master) ✗ python query.py
Loading embedding model and vector database...

✅ Vector database loaded successfully!
--------------------------------------------------
Personal RAG Query System
Type 'exit' or 'quit' to end the session
--------------------------------------------------

Enter your question: what is stand on tiptoes

Found 5 relevant results:
--------------------------------------------------
Result 1 (Relevance: 89.46%):
Content: Stand on Tiptoes
Source: sources/Stand on Tiptoes.html
--------------------------------------------------
Result 2 (Relevance: 89.46%):
Content: Stand on Tiptoes
Source: sources/Spend $0.05 to Change the Voice of a Song.html
--------------------------------------------------
Result 3 (Relevance: 89.46%):
Content: Stand on Tiptoes
Source: sources/Try Stable Diffusion.html
--------------------------------------------------
Result 4 (Relevance: 15.5%):
Content: and Collaboration Change the way teams work with solutions designed for humans and built for impact. Google Workspace Collaboration and productivity tools for enterprises. Google Workspace Essentials Secure video meetings and modern collaboration for teams. Cloud Identity Unified platform for IT admins to manage user devices and apps. Chrome Enterprise ChromeOS, Chrome Browser, and Chrome devices built for business. Security Detect, investigate, and respond to online threats to help protect
Source: sources/Prompt Engineering for AI Guide _ Google Cloud.html
--------------------------------------------------
Result 5 (Relevance: 15.11%):
Content: Startups and SMB See all solutions Industry Solutions Reduce cost, increase operational agility, and capture new market opportunities. Retail Analytics and collaboration tools for the retail value chain. Consumer Packaged Goods Solutions for CPG digital transformation and brand growth. Financial Services Computing, data management, and analytics tools for financial services. Healthcare and Life Sciences Advance research at scale and empower healthcare innovation. Media and Entertainment
Source: sources/Prompt Engineering for AI Guide _ Google Cloud.html
--------------------------------------------------

Enter your question: 
Please enter a valid question.

Enter your question: 
Please enter a valid question.

Enter your question: stable diffusion

Found 5 relevant results:
--------------------------------------------------
Result 1 (Relevance: 15.45%):
Content: and back ends. Workflows Workflow orchestration for serverless products and API services. API Gateway Develop, deploy, secure, and manage APIs with a fully managed gateway. Storage Cloud Storage Object storage that’s secure, durable, and scalable. Block Storage High-performance storage for AI, analytics, databases, and enterprise applications. Filestore File storage that is highly scalable and secure. Persistent Disk Block storage for virtual machine instances running on Google Cloud. Cloud
Source: sources/Prompt Engineering for AI Guide _ Google Cloud.html
--------------------------------------------------
Result 2 (Relevance: 13.33%):
Content: policies and defense against web and DDoS attacks. Cloud CDN and Media CDN Content delivery network for serving web and video content. Cloud DNS Domain name system for reliable and low-latency name lookups. Cloud Load Balancing Service for distributing traffic across applications and regions. Cloud NAT NAT service for giving private instances internet access. Cloud Connectivity Connectivity options for VPN, peering, and enterprise needs. Network Connectivity Center Connectivity management to
Source: sources/Prompt Engineering for AI Guide _ Google Cloud.html
--------------------------------------------------
Result 3 (Relevance: 12.34%):
Content: platform. Cloud Deploy Fully managed continuous delivery to GKE and Cloud Run. Cloud Deployment Manager Service for creating and managing Google Cloud resources. Cloud SDK Command-line tools and libraries for Google Cloud. Cloud Scheduler Cron job scheduler for task automation and management. Cloud Source Repositories Private Git repository to store, manage, and track code. Infrastructure Manager Automate infrastructure management with Terraform. Cloud Workstations Managed and secure
Source: sources/Prompt Engineering for AI Guide _ Google Cloud.html
--------------------------------------------------
Result 4 (Relevance: 11.63%):
Content: Service Serverless, minimal downtime migrations to Cloud SQL. Bare Metal Solution Fully managed infrastructure for your Oracle workloads. Memorystore Fully managed Redis and Memcached for sub-millisecond data access. Developer Tools Artifact Registry Universal package manager for build artifacts and dependencies. Cloud Code IDE support to write, run, and debug Kubernetes applications. Cloud Build Continuous integration and continuous delivery platform. Cloud Deploy Fully managed continuous
Source: sources/Prompt Engineering for AI Guide _ Google Cloud.html
--------------------------------------------------
Result 5 (Relevance: 11.6%):
Content: Mandiant Incident Response Chrome Enterprise Premium Assured Workloads Google Security Operations Mandiant Consulting See all security and identity products Serverless Cloud Run Cloud Functions App Engine Workflows API Gateway Storage Cloud Storage Block Storage Filestore Persistent Disk Cloud Storage for Firebase Local SSD Storage Transfer Service Parallelstore Google Cloud NetApp Volumes Backup and DR Service Web3 Blockchain Node Engine Blockchain RPC Save money with our transparent approach
Source: sources/Prompt Engineering for AI Guide _ Google Cloud.html
--------------------------------------------------
```

- Type any question or keywords
- The system finds the most relevant text from your HTML files
- Results are displayed with relevance scores
- Type 'exit' or 'quit' to end

## How It Works

1. The system uses AI embeddings to convert text into numerical vectors
2. Similar content has similar vector representations
3. When you search, your question is converted to a vector
4. The system finds text chunks with the closest matching vectors
5. Results are ranked by similarity score

## Tips

- Add more HTML files to expand your knowledge base
- Be specific with your search queries
- Use keywords related to your content
- Run `embedding.py` again whenever you add new files
