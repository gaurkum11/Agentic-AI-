# from crewai import Crew,Process
# from agents import researcher, writer, proof_reader
# from task import research_task, writer_task, proof_reader_task

# crew = Crew(
#     agents=[researcher, writer, proof_reader],
#     tasks=[research_task, writer_task, proof_reader_task],
#     process=Process.sequential
# )

# topic = "AI in Finance"
# # result = crew.kickoff(inputs={"topic" : topic})
# # print(result)

# import time
# from litellm import RateLimitError

# try:
#     result = crew.kickoff(inputs={"topic": topic})
# except RateLimitError as e:
#     print("Rate limit hit, waiting 60 seconds...")
#     time.sleep(60)  # or the time suggested in the error message
#     result = crew.kickoff(inputs={"topic": topic})

# print(result)


import time
import gradio as gr
from litellm import RateLimitError
from crewai import Crew, Process
from agents import researcher, use_case_generator, resource_collector, proposal_writer
from task import research_task, resource_task,proposal_task, use_case_task

# Define the Crew
crew = Crew(
    agents=[researcher, use_case_generator, resource_collector, proposal_writer],
    tasks=[research_task,use_case_task,resource_task,proposal_task],
    process=Process.sequential
)

# Function to wrap the crew logic
def generate_newsletter(company):
    try:
        result = crew.kickoff(inputs={"company": company})
    except RateLimitError as e:
        print("Rate limit hit, waiting 60 seconds...")
        time.sleep(60)
        result = crew.kickoff(inputs={"company": company})
    return result

# Gradio Interface
demo = gr.Interface(
    fn=generate_newsletter,
    inputs=gr.Textbox(label="Enter Topic", placeholder="e.g. AI in Finance"),
    outputs=gr.Textbox(label="Generated Newsletter", lines=20),
    title="🧠 AI Newsletter Generator",
    description="Give it a topic and let your AI crew research, write, and proofread a newsletter!"
)

# Launch the app
if __name__ == "__main__":
    demo.launch()
