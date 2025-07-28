# intern_gpt/app.py
from langchain_core.runnables import RunnableLambda, RunnableMap, RunnablePassthrough
from langgraph.graph import END, StateGraph
from retriever_setup import retriever
from prompt_templates import qa_prompt
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

def query_rewriter_node(state):
    question = state["question"]
    rewritten = f"What does this mean regarding internship policy: {question}?"
    return {"rephrased_query": rewritten, **state}

def retriever_node(state):
    query = state["rephrased_query"]
    docs = retriever.invoke(query)
    return {"docs": docs, **state}

def prompt_node(state):
    question = state["rephrased_query"]
    docs = state["docs"]
    context = "\n\n".join([d.page_content for d in docs])
    response = llm.invoke(qa_prompt.format(context=context, question=question))
    return {"answer": response.content, **state}

# Define the DAG
graph = StateGraph()
graph.add_node("rewrite", RunnableLambda(query_rewriter_node))
graph.add_node("retrieve", RunnableLambda(retriever_node))
graph.add_node("prompt", RunnableLambda(prompt_node))

# Edges
graph.set_entry_point("rewrite")
graph.add_edge("rewrite", "retrieve")
graph.add_edge("retrieve", "prompt")
graph.add_edge("prompt", END)

# Compile the graph
runnable = graph.compile()

if __name__ == "__main__":
    user_question = input("Ask InternGPT: ")
    final_state = runnable.invoke({"question": user_question})
    print("\nAnswer:\n", final_state["answer"])