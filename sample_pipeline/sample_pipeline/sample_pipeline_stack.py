from aws_cdk import (
    Stack,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    aws_codebuild as codebuild,

)
from constructs import Construct
from .builders import Builder


class SamplePipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Pipeline from GitHub to ECR
        pipeline = codepipeline.Pipeline(
            self, "Pipeline",
            pipeline_name="sample-pipeline",
            stages=[]
        )

        repo_owner = 'terusaku'
        repo_name = 'etc_docs'
        # GitHub Source
        source_output = codepipeline.Artifact()
        pipeline.add_stage(
            stage_name="CheckoutSource",
            actions=[
                codepipeline_actions.GitHubSourceAction(
                    action_name="GitHubRepo",
                    owner=repo_owner,
                    repo=repo_name,
                    oauth_token=codepipeline.SecretValue.secrets_manager('github-pat/api-v4'),
                    output=source_output,
                    branch='develop',
                ),
            ]
        )

