from pyzeebe import ZeebeTaskRouter
import robot
import listener
from robot.libraries.BuiltIn import BuiltIn


router = ZeebeTaskRouter()

@router.task(task_type="randomDestination")
async def my_task():
    l = listener.getVariablesListener()
    robotOutput = robot.run("task.robot", listener=l)
    country = l.variables["${country}"]
    destination = l.variables["${destination}"].strip()
    description = l.variables["${description}"]
    return {"country": country, "destination": destination, "description": description, "robotResult": robotOutput}
