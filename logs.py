from azureml.core import Workspace
from azureml.core.webservice import Webservice

# Requires the config to be downloaded first to the current working directory
ws = Workspace.from_config()

# Set with the deployment name
name = "votingensemblemodels"

# load existing web service
service = Webservice(name=name, workspace=ws)

# Enable app insight
service.update(enable_app_insights=True)

# Get service log
logs = service.get_logs()

for line in logs.split('\n'):
    print(line)
