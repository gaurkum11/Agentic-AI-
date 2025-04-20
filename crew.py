from crewai import Crew,Process
from agents import researcher, writer, proof_reader
from task import research_task, writer_task, proof_reader_task

crew = Crew(
    agents=[researcher, writer, proof_reader],
    tasks=[research_task, writer_task, proof_reader_task],
    process=Process.sequential
)

topic = "AI in Finance"
result = crew.kickoff(inputs={"topic" : topic})
print(result)

import time
from litellm import RateLimitError

try:
    result = crew.kickoff(inputs={"topic": topic})
except RateLimitError as e:
    print("Rate limit hit, waiting 60 seconds...")
    time.sleep(60)  # or the time suggested in the error message
    result = crew.kickoff(inputs={"topic": topic})

print(result)
