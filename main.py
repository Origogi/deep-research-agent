from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.ui import Console

model = OpenAIChatCompletionClient(model="gpt-4o-mini")

clarity_agent = AssistantAgent(
    model_client=model,
    system_message=""
)

tone_agent = AssistantAgent(
    model_client=model,
    system_message=""
)

persuasion_agent = AssistantAgent(
    model_client=model,
    system_message=""
)

synthesizer_agent = AssistantAgent(
    model_client=model,
    system_message=""
)

critic_agent = AssistantAgent(
    model_client=model,
    system_message=""
)