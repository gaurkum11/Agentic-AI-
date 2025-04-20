# **Agentic-AI-**

**Agentic-AI-** is a modular framework designed for building and managing AI agents capable of performing complex tasks through collaboration and tool integration. It provides a structured approach to define agents, assign tasks, and utilize tools, enabling the development of sophisticated AI-driven applications.

## **Features**

- **Agent Management**: Define and manage multiple AI agents with specific roles and capabilities.
- **Task Assignment**: Create and assign tasks to agents, facilitating organized workflows.
- **Tool Integration**: Incorporate various tools that agents can use to accomplish their tasks.
- **Crew Coordination**: Manage a crew of agents working together to complete complex objectives.

## **Installation**

To set up the project locally, follow these steps:

1. **Clone the Repository**

   ```sh
   git clone https://github.com/gaurkum11/Agentic-AI-.git
   cd Agentic-AI-
   ```

2. **Install Dependencies**

   It's recommended to use a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

   Then, install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

   *Note: If a `requirements.txt` file is not present, you can install dependencies using the provided `Pipfile`:*

   ```sh
   pip install pipenv
   pipenv install
   ```

## **Usage**

Here's a basic example of how to utilize the framework:

```python
from agents import Agent
from task import Task
from tool import Tool
from crew import Crew

# Define tools
search_tool = Tool(name="WebSearch", function=web_search_function)
calc_tool = Tool(name="Calculator", function=calculator_function)

# Create agents
agent_1 = Agent(name="Researcher", tools=[search_tool])
agent_2 = Agent(name="Analyst", tools=[calc_tool])

# Define tasks
task_1 = Task(description="Gather data on market trends", assigned_agent=agent_1)
task_2 = Task(description="Analyze financial data", assigned_agent=agent_2)

# Initialize crew
project_crew = Crew(agents=[agent_1, agent_2], tasks=[task_1, task_2])

# Execute tasks
project_crew.execute_all_tasks()
```

*Ensure that `web_search_function` and `calculator_function` are defined functions that perform the desired operations.*

## **Project Structure**

- `agents.py`: Defines the `Agent` class and related functionalities.
- `task.py`: Contains the `Task` class for task management.
- `tool.py`: Implements the `Tool` class for tool integration.
- `crew.py`: Manages the coordination of multiple agents and tasks.
- `output.md`: Placeholder for output or documentation.
- `Pipfile` & `Pipfile.lock`: Manage project dependencies.

## **Contributing**

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
