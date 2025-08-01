# LangGraph Exercise Report

## Code File: `decision_agent.py`

See the full code inside the file. It defines the AgentState and three nodes: an evaluator and two handlers.

## Dependencies

**`requirements.txt`:**
langchain
langchain-core
langgraph
pydantic


## Installed via:  

pip install -r requirements.txt


## AgentState
This is the shared memory between all nodes. It includes:

input_value (int): The user’s numeric input

evaluation_result (str): Result of threshold check ("high"/"low")

final_message (str): Final output message from handler

## Node Functions
evaluate_number(state)
Checks if input_value > 50

Sets evaluation_result to "high" or "low"

handle_high_value(state)
Returns: {"final_message": "The value is high!"}

handle_low_value(state)
Returns: {"final_message": "The value is low."}

## Conditional Routing
decide_path(state)
Reads evaluation_result

Routes to high_handler or low_handler

## Results

Input: 75
json
Copy code
{
  "input_value": 75,
  "evaluation_result": "high",
  "final_message": "The value is high!"
}

Input: 25
json
Copy code
{
  "input_value": 25,
  "evaluation_result": "low",
  "final_message": "The value is low."
}

## Key Learnings
LangGraph lets you build decision-based workflows easily

TypedDict defines persistent state shared across nodes

Conditional edges make branching logic intuitive

LangGraph is powerful for building agents that go beyond sequential chains

## Challenges
Minor confusion with add_conditional_edges() mapping, resolved by reading LangGraph examples.

Made sure state updates were returned properly from each node.

## Summary
This was a powerful introduction to LangGraph. Even in a basic example, you can clearly see how complex logic can be structured declaratively. Conditional flow, shared memory, and modular node design are all very intuitive using LangGraph.