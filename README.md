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


## **Project Structure**

- `agents.py`: Defines the `Agent` class and related functionalities.
- `task.py`: Contains the `Task` class for task management.
- `tool.py`: Implements the `Tool` class for tool integration.
- `crew.py`: Manages the coordination of multiple agents and tasks.
- `output.md`: Placeholder for output or documentation.
- `Pipfile` & `Pipfile.lock`: Manage project dependencies.



