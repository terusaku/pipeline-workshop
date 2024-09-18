from constructs import Construct
import aws_cdk as cdk
from aws_cdk import (
    aws_codebuild as codebuild,
)


class Builder(Construct):

    @property
    def build_project(self):
        return self._build_project

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Build project on CodeBuild to make Docker Image
        self._build_project = codebuild.PipelineProject(
            self, "SampleDocker",
        )
