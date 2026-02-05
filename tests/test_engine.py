import asyncio

from agentkit.engine.runner import AgentRunner, Task


def test_agent_runner_executes_tasks():
    runner = AgentRunner(max_concurrency=2)

    async def echo_handler(payload):
        await asyncio.sleep(0)
        return {"echo": payload["value"]}

    runner.register_handler("echo", echo_handler)

    results = asyncio.run(runner.run([Task(name="echo", payload={"value": 1})]))
    assert results[0]["result"]["echo"] == 1
