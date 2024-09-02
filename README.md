# ubot: University Student Assistant Chatbot with Rasa's CALM: Conversational AI with Language Models

To run the chatbot, there are several setup requirements and run commands:
1. Initialise and activate a virtual environment on your machine in a specific directory (here called ‘ubot-env’):
python -m venv ubot-env
.\ubot-env\Scripts\activate

2. Set up necessary keys as environmental variables:
- Rasa Pro key: RASA_PRO_LICENSE
- OpenAI key for initial setup (default LLM provider): OPENAI_API_KEY
- Hugging Face API token: HUGGINGFACEHUB_API_TOKEN

3. Install Rasa CALM locally as per the following documentation:
- https://rasa.com/docs/rasa-pro/installation/python/installation
- https://rasa.com/docs/rasa-pro/tutorial

4. Install the Hugging Face Hub package:
pip install huggingface_hub

5. Download chatbot from one of the repositories

6. Run Rasa CALM by using the following commands in two separate terminals:
- Action server:
rasa run actions
- Talk to bot in terminal:
rasa run
- Talk to bot in browser:
rasa inspect

Note: check .gitignore to understand what files are not uploaded. This includes:
- Rasa source code: Should be installed when installing Rasa. As part of this project, changes were made to the source code to resolve some issues with features in experimental stage at the time of this project. However, it is not recommended to make changes to the source code locally. Instead, these changes were proposed to Rasa themselves as a GitHub contribution, so the issues stemming primarily from different versions of the components (e.g., Hugging Face Hub and Inference / Client API) should be fixed in later Rasa CALM versions.
- virtual environment (contains packages)
- files containing credentials (Rasa Pro license, Hugging Face API, etc.)
