"""
Auto-generated classes from the SHACL graph in analysis.ttl.

This file was generated using the `case_models.py` script.
"""

from pydantic import Field

from caselib.uco import action, core


class Analysis(action.Action):
    """
    An analysis is an action of detailed examination of something in order to
    understand its nature, context or essential features.
    """


class AnalyticResultFacet(core.Facet):
    """
    An analytic result facet is a grouping of characteristics unique to the
    results of an analysis action.
    """


class ArtifactClassification(core.UcoInherentCharacterizationThing):
    """
    An artifact classification is a single specific assertion that a particular
    class of a classification taxonomy applies to something.
    """

    classificationConfidence: float | None = None
    class_: str | list[str] = []


class AnalyticResult(core.Assertion):
    """
    An analytic result is a characterization of the understanding resulting from
    an analysis action.
    """

    originatingAnalysis: Analysis | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    resultContent: core.UcoObject | list[core.UcoObject] | None = []


class ArtifactClassificationResultFacet(AnalyticResultFacet):
    """
    An artifact classification result facet is a grouping of characteristics
    unique to the results of an artifact classification analysis action.
    """

    classification: ArtifactClassification | list[ArtifactClassification] | None = []
