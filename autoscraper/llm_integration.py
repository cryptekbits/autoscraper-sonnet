import anthropic
import os

def analyze_content_with_llm(content, url):
    """
    Analyzes the content using Anthropic's LLM to extract relevant details and format them in Markdown.

    Parameters:
    ----------
    content : str
        The content to be analyzed.
    url : str
        The URL of the page being analyzed.

    Returns:
    --------
    str
        A string containing the formatted Markdown content.
    """
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""
    You are an expert web content analyzer and technical writer. Analyze the following webpage content and create a concise, well-structured Markdown summary. Include the most important information, key concepts, and any relevant code snippets or examples.

    URL: {url}

    Content:
    {content}

    Please format your response as follows:
    1. Start with a level 2 header (##) containing the page title or a summary of the main topic.
    2. Provide a brief overview of the page content.
    3. List the key points or concepts using bullet points.
    4. Include any relevant code snippets, properly formatted in Markdown code blocks.
    5. If there are any important warnings, notes, or tips, include them using blockquotes (>).

    Your response should be in valid Markdown format, ready to be written directly to a .md file.
    """

    response = client.messages.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="claude-3-5-sonnet-20240620",
        max_tokens=4096
    )

    return response.content[0].text.strip()
