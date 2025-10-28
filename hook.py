name = 'CyberBot'
description = 'Autonomous Red Team agent plugin simulating APT behaviors'
 
async def enable(services):
    from app.autonomous_agent import AutonomousAgent
    agent = AutonomousAgent(services)
    await agent.initialize()
