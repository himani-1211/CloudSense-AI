from app.cloud.providers.aws_provider import AWSProvider
from app.cloud.providers.azure_provider import AzureProvider
from app.cloud.providers.gcp_provider import GCPProvider


class CloudProviderFactory:

    @staticmethod
    def get_provider(provider: str):

        provider = provider.lower()

        if provider == "aws":
            return AWSProvider()

        elif provider == "azure":
            return AzureProvider()

        elif provider == "gcp":
            return GCPProvider()

        raise ValueError(f"Unsupported cloud provider: {provider}")