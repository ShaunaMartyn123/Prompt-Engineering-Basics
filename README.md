# Prompt-Engineering-Basics
Basic Gemini prompt engineering with structured output.

## How It Works
Zero-Shot Prompting: In this technique, the model is given a question with no prior examples. It must generate an answer based solely on its knowledge.
Few-Shot Prompting: The model is provided with a few examples to guide it in answering the question. This helps the model understand the format and context.
Chain-of-Thought Prompting: The model is asked to reason through a problem step by step before providing the final answer.

## Example Prompts
Zero-Shot: "What is the capital of France?"
Few-Shot: "The capital of Germany is Berlin. The capital of Spain is Madrid. What is the capital of France?"
Chain-of-Thought: "To determine the capital of France, follow these steps:
Identify France as a country in Europe.
Look at the major cities in France.
The capital city is the political and economic center.
Based on this, what is the capital of France?"
