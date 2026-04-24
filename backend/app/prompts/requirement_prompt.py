def build_requirement_prompt(user_prompt: str) -> str:
    return f"""
    You are a senior backend systems engineer.
    Your task is to analyze the user's system design request and convert it into a structured requirements document.
    Return ONLY valid JSON.
    Do not include markdown.
    Do not include explanation text before or after the JSON.
    The JSON must follow this exact structure:
    {{
      "system_name": "string",
      "actors": ["string"],
      "functional_requirements": ["string"],
      "non_functional_requirements": ["string"],
      "scale_assumptions": ["string"],
      "constraints": ["string"],
      "open_questions": ["string"]
    }}
    User request:
    "{user_prompt}"
    """