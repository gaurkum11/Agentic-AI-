
from crewai import Task
from agents import researcher, use_case_generator, proposal_writer, resource_collector
from tool import google_search_tool

#

# research_task = Task(
#     description=("""
#     Identify the next big trend in the topic: {topic}. Focus on identifying pros and cons and the overall narrative.
#     Your final report should clearly and explicitly articulate the key points, market opportunities and potential risks
#     associated with the given topic.
#     """),
#     expected_output="A comprehensive 3 paragraph long report on the latest information on the given topic: {topic}.",
#     tools=[google_search_tool],
#     agent = researcher
# )

research_task = Task(
    description="""
    Conduct market research on  company : {company}.
      Identify:
    - Key business segments (e.g., supply chain, customer support).
    - Current challenges and automation opportunities.
    - Competitor AI adoption trends.
    """,
    expected_output="A structured report on industry trends, challenges, and AI opportunities.",
    agent=researcher,
    tools=[google_search_tool]
)

# writer_task = Task(
#     description=("""
#     Compose an insightful article on the topic: {topic}. Focus on the latest trends and how its impacting the industry.
#     This article should be digestible, easy to understand, engaging and positive.
#     """),
#     expected_output="A 4 paragraph long article on the topic: {topic}, formatted as markdown.",
#     tools=[google_search_tool],
#     agent = writer,
#     async_execution=False
# )

use_case_task = Task(
    description="""
    Generate AI/GenAI use cases for company : {company} focusing on:
    - Process automation (e.g., document processing).
    - Customer experience (e.g., chatbots).
    - Predictive analytics (e.g., demand forecasting).
    """,
    expected_output="List of 5-10 high-impact AI use cases with justifications.",
    agent=use_case_generator,
    tools=[google_search_tool]
)

# proof_reader_task = Task(
#     description=("""
#     Finalise an insightful article on the topic: {topic} which is already written by the writer. Focus on the information and how it is structured.
#     It should not have any mistakes and should be very easy to digest. Make sure to put sources of the information where they come from.
#     Also write 3 sources for further studying of the topic. This article should be digestible, easy to understand, engaging and positive.
#     """),
#     expected_output="A 4 paragraph long article on the topic: {topic}, formatted as markdown with all the relevant sources",
#     tools=[google_search_tool],
#     agent = proof_reader,
#     async_execution=False,
#     output_file="newsletter.md"
# )

resource_task = Task(
    description="""
    Find datasets, models, and tools for the proposed AI use cases for the company : {company}.
    Sources: Kaggle, Hugging Face, GitHub.
    Save links in a Markdown file.
    """,
    expected_output="Clickable resource links (datasets, models, tools) in Markdown.",
    agent=resource_collector,
    tools=[google_search_tool]
)

proposal_task = Task(
    description="""
    Compile the top AI use cases into a business proposal for the  company : {company}.
    Include:
    - Business impact
    - Implementation feasibility
    - Resource references
    """,
    expected_output="Professional AI adoption proposal (Markdown/PDF).",
    agent=proposal_writer,
    output_file="ai_proposal.md"
)
