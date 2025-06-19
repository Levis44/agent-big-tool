from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, MessagesState
from langchain_core.messages import SystemMessage

llm = ChatOpenAI(model="gpt-4o") 

# System message
sys_msg = SystemMessage(content="You are a helpful assistant tasked with writing performing arithmetic on a set of inputs.")

# Node
def assistant(state: MessagesState):
   return {"messages": [llm.invoke([sys_msg] + state["messages"])]}

# Build graph
builder = StateGraph(MessagesState)

builder.add_node("assistant", assistant)
builder.add_edge(START, "assistant")

graph = builder.compile()