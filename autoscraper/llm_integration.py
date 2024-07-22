import anthropic
import os
def analyze_content_with_llm(content):
    """
    You are a software engineer researching API docs for understanding the API
    Analyzes the content using Anthropic's LLM to identify important topics.

    Parameters:
    ----------
    content : str
        The content to be analyzed.

    Returns:
    --------
    list
        A list of important topics identified by the LLM.
    """
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""
    Analyze the following content and identify the most important topics or concepts:

    {content}

    Important topics:
    1.
    """

    response = client.messages.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="claude-3-5-sonnet-20240620",
        max_tokens=2048
    )

    # Extract topics from the response
    topics = response.content[0].text.strip().split("\n")[1:]  # Skip the first line which is "1."
    topics = [topic.strip().lstrip("0123456789. ") for topic in topics]

    return topics
