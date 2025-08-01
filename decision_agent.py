from typing import TypedDict
from langgraph.graph import StateGraph, END


# 1. Define the shared graph state
class AgentState(TypedDict):
    input_value: int
    evaluation_result: str
    final_message: str


# 2. Node to evaluate if input is high or low
def evaluate_number(state: AgentState) -> dict:
    input_value = state["input_value"]
    threshold = 50
    if input_value > threshold:
        return {"evaluation_result": "high"}
    else:
        return {"evaluation_result": "low"}


# 3. Handler for high values
def handle_high_value(state: AgentState) -> dict:
    return {"final_message": "The value is high!"}


# 4. Handler for low values
def handle_low_value(state: AgentState) -> dict:
    return {"final_message": "The value is low."}


# 5. Router function based on evaluation result
def decide_path(state: AgentState) -> str:
    if state["evaluation_result"] == "high":
        return "high_handler"
    else:
        return "low_handler"


# 6. Build the graph
graph = StateGraph(AgentState)
graph.add_node("evaluator", evaluate_number)
graph.add_node("high_handler", handle_high_value)
graph.add_node("low_handler", handle_low_value)

graph.set_entry_point("evaluator")
graph.add_conditional_edges("evaluator", decide_path, {
    "high_handler": "high_handler",
    "low_handler": "low_handler"
})
graph.add_edge("high_handler", END)
graph.add_edge("low_handler", END)

# 7. Compile and run
compiled_graph = graph.compile()

# Test with high input
result_high = compiled_graph.invoke({"input_value": 75})
print("Result for high input:", result_high)

# Test with low input
result_low = compiled_graph.invoke({"input_value": 25})
print("Result for low input:", result_low)
