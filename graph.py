import uuid
from langchain.embeddings import init_embeddings
from langchain_openai import ChatOpenAI
from langgraph_bigtool import create_agent
from tools import HOME_AUTOMATION_TOOLS as tools
from langgraph.store.memory import InMemoryStore
from langchain_core.messages import HumanMessage, SystemMessage

def run_demo():
    llm = ChatOpenAI(model="gpt-4o")

    # Create registry of tools. This is a dict mapping
    # identifiers to tool instances.
    tool_registry = {
        str(uuid.uuid4()): tool
        for tool in tools
    }

    embeddings = init_embeddings("openai:text-embedding-3-small")

    store = InMemoryStore(
        index={
            "embed": embeddings,
            "dims": 1536,
            "fields": ["description"],
        }
    )
    for tool_id, tool in tool_registry.items():
        store.put(
            ("tools",),
            tool_id,
            {
                "description": f"{tool.name}: {tool.description}",
            },
        )

    # Build graph
    builder = create_agent(llm, tool_registry)
    agent = builder.compile(store=store)

    queries = [
            "Turn off the lights in the kitchen",
            "Set the thermostat to 70 degrees",
            "Lock the front door",
            "What's happening in the living room?",
            "It's a little dirty, can you vacuum the living room?",
            "I'm cold, can you turn on the heat?"
    ]
        
    for i, query in enumerate(queries, 1):
        print(f"Query {i}: {query}")
        print("-" * 100)
        
        # Process the query
        result = agent.invoke({
            "messages": [
                SystemMessage(content="You are a helpful assistant tasked with controlling the home automation system."),
                HumanMessage(content=query)
            ]
        })
        
        for m in result['messages']:
            m.pretty_print()
        print("-" * 100)

if __name__ == "__main__":
    run_demo()