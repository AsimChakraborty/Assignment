# import requests
# from bs4 import BeautifulSoup
# import autogen

# # Fetch and parse the Wikipedia page
# def fetch_wikipedia_content(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         content = soup.find(id="bodyContent").get_text()
#         return content
#     else:
#         raise Exception("Failed to fetch the Wikipedia page")

# # Initialize Autogen framework
# class QnAAgent(autogen.Agent):
#     def __init__(self, content):
#         self.content = content
#         super().__init__()
       

#     def answer_question(self, question):
#         # This function should use the Autogen framework's capabilities to process the question
#         # and search for answers within the Wikipedia content.
#         return self.process_question(question)
    
#     def process_question(self, question):
#         # Here you would implement the logic to search through self.content for the answer
#         # For simplicity, let's use a basic keyword search
#         if question.lower() in self.content.lower():
#             start_index = self.content.lower().find(question.lower())
#             end_index = start_index + 500  # Provide 500 characters as context
#             return self.content[start_index:end_index]
#         else:
#             return "Sorry, I couldn't find the answer to your question."




# import requests
# from bs4 import BeautifulSoup

# # Fetch and parse the Wikipedia page
# def fetch_wikipedia_content(url):
#     try:
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.content, 'html.parser')
#         content = soup.find(id="bodyContent").get_text()
#         return content
#     except requests.exceptions.Timeout:
#         raise Exception("The request timed out. Please try again later.")
#     except requests.exceptions.RequestException as e:
#         raise Exception(f"An error occurred: {e}")

# class QnAAgent:
#     def __init__(self, content):
#         self.content = content

#     def answer_question(self, question):
#         return self.process_question(question)
    
#     def process_question(self, question):
#         # Implement a basic keyword search
#         if question.lower() in self.content.lower():
#             start_index = self.content.lower().find(question.lower())
#             end_index = start_index + 500  # Provide 500 characters as context
#             return self.content[start_index:end_index]
#         else:
#             return "Sorry, I couldn't find the answer to your question."






import requests
from bs4 import BeautifulSoup

# Fetch and parse the Wikipedia page
def fetch_wikipedia_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find(id="bodyContent").get_text()
        return content
    except requests.exceptions.Timeout:
        raise Exception("The request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        raise Exception(f"An error occurred: {e}")

class QnAAgent:
    def __init__(self, content):
        self.content = content

    def answer_question(self, question):
        return self.process_question(question)
    
    def process_question(self, question):
        question = question.lower()
        content_lower = self.content.lower()

        # Keywords for common questions
        if "capital" in question:
            if "capital" in content_lower:
                return self.extract_information("capital", content_lower)
        elif "population" in question:
            if "population" in content_lower:
                return self.extract_information("population", content_lower)
        elif "culture" in question:
            if "culture" in content_lower or "tradition" in content_lower:
                return self.extract_information("culture", content_lower)
            
        elif "official" in question:
            if "official" in content_lower:
                return self.extract_information("official", content_lower)    
        elif "languages" in question:
            if "languages" in content_lower:
                return self.extract_information("languages", content_lower)  
        elif "borders" in question:
            if "borders" in content_lower:
                return self.extract_information("borders", content_lower)          

        return "Sorry, I couldn't find the answer to your question."

    def extract_information(self, keyword, content_lower):
        keyword_index = content_lower.find(keyword)
        if keyword_index == -1:
            return "Sorry, I couldn't find the answer to your question."

        # Extract a chunk of text around the keyword
        start_index = max(0, keyword_index - 100)
        end_index = min(len(content_lower), keyword_index + 500)
        return self.content[start_index:end_index]




# using spacy

# import requests
# from bs4 import BeautifulSoup
# import spacy

# # Load spaCy's English model
# nlp = spacy.load("en_core_web_sm")

# # Fetch and parse the Wikipedia page
# def fetch_wikipedia_content(url):
#     try:
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.content, 'html.parser')
#         content = soup.find(id="bodyContent").get_text()
#         return content
#     except requests.exceptions.Timeout:
#         raise Exception("The request timed out. Please try again later.")
#     except requests.exceptions.RequestException as e:
#         raise Exception(f"An error occurred: {e}")

# class QnAAgent:
#     def __init__(self, content):
#         self.content = content
#         self.doc = nlp(content)

#     def answer_question(self, question):
#         return self.process_question(question)
    
#     def process_question(self, question):
#         question = question.lower()

#         # Determine the type of question and get relevant information
#         if "capital" in question:
#             return self.extract_information("capital")
#         elif "population" in question:
#             return self.extract_information("population")
#         elif "culture" in question or "tradition" in question:
#             return self.extract_information("culture")
#         elif "Republic" in question:
#             return self.extract_information("Republic")
#         elif "languages" in question:
#             return self.extract_information("languages")
#         elif "borders" in question:
#             return self.extract_information("borders")
        
#         return "Sorry, I couldn't find the answer to your question."

#     def extract_information(self, keyword):
#         keyword_lower = keyword.lower()
#         for ent in self.doc.ents:
#             if keyword_lower in ent.text.lower():
#                 return ent.text

#         # Fallback to context extraction around keywords
#         content_lower = self.content.lower()
#         keyword_index = content_lower.find(keyword.lower())
#         if keyword_index == -1:
#             return "Sorry, I couldn't find the answer to your question."

#         start_index = max(0, keyword_index - 100)
#         end_index = min(len(self.content), keyword_index + 500)
#         return self.content[start_index:end_index]
